"""
Evaluation Module for SHL Assessment Recommendation System

Computes Mean Recall@K and other metrics for evaluating recommendation quality.
"""
import os
import json
import csv
import logging
from typing import List, Dict, Tuple, Set
from recommendation_engine import RecommendationEngine

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Evaluator:
    """
    Evaluates the recommendation system using labeled data.
    
    Metrics:
    - Recall@K: Fraction of relevant items retrieved in top K
    - Mean Recall@K: Average Recall@K across all queries
    """
    
    def __init__(self, engine: RecommendationEngine = None):
        """Initialize evaluator with a recommendation engine."""
        self.engine = engine or RecommendationEngine()
    
    def compute_recall_at_k(
        self,
        recommended_urls: List[str],
        relevant_urls: Set[str],
        k: int = 10
    ) -> float:
        """
        Compute Recall@K for a single query.
        
        Recall@K = (Number of relevant items in top K) / (Total relevant items)
        
        Args:
            recommended_urls: List of recommended assessment URLs (ordered by relevance)
            relevant_urls: Set of ground truth relevant URLs
            k: Number of top recommendations to consider
            
        Returns:
            Recall@K score between 0 and 1
        """
        if not relevant_urls:
            return 0.0
        
        # Get top K recommendations
        top_k = set(recommended_urls[:k])
        
        # Count relevant items in top K
        relevant_in_top_k = len(top_k & relevant_urls)
        
        # Compute recall
        recall = relevant_in_top_k / len(relevant_urls)
        
        return recall
    
    def compute_mean_recall_at_k(
        self,
        queries_with_labels: List[Dict],
        k: int = 10
    ) -> Tuple[float, List[Dict]]:
        """
        Compute Mean Recall@K across all queries.
        
        Args:
            queries_with_labels: List of dicts with 'query' and 'relevant_urls' keys
            k: Number of recommendations to consider
            
        Returns:
            Tuple of (mean_recall, list of per-query results)
        """
        if not queries_with_labels:
            return 0.0, []
        
        results = []
        total_recall = 0.0
        
        for item in queries_with_labels:
            query = item['query']
            relevant_urls = set(item['relevant_urls'])
            
            # Get recommendations
            recommendations = self.engine.recommend_balanced(query, max_results=k)
            recommended_urls = [r['url'] for r in recommendations]
            
            # Compute recall
            recall = self.compute_recall_at_k(recommended_urls, relevant_urls, k)
            total_recall += recall
            
            results.append({
                'query': query,
                'recall_at_k': recall,
                'recommended_count': len(recommended_urls),
                'relevant_count': len(relevant_urls),
                'relevant_in_top_k': len(set(recommended_urls[:k]) & relevant_urls)
            })
        
        mean_recall = total_recall / len(queries_with_labels)
        
        return mean_recall, results
    
    def evaluate_from_csv(
        self,
        train_csv_path: str,
        k: int = 10
    ) -> Dict:
        """
        Evaluate using labeled train data from CSV file.
        
        Expected CSV format:
        - Column 1: Query
        - Column 2+: Relevant assessment URLs
        
        Args:
            train_csv_path: Path to the labeled training CSV
            k: Number of recommendations to consider
            
        Returns:
            Dictionary with evaluation results
        """
        queries_with_labels = []
        
        with open(train_csv_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader, None)  # Skip header if present
            
            for row in reader:
                if len(row) < 2:
                    continue
                
                query = row[0].strip()
                relevant_urls = [url.strip() for url in row[1:] if url.strip()]
                
                if query and relevant_urls:
                    queries_with_labels.append({
                        'query': query,
                        'relevant_urls': relevant_urls
                    })
        
        logger.info(f"Loaded {len(queries_with_labels)} labeled queries from {train_csv_path}")
        
        mean_recall, per_query_results = self.compute_mean_recall_at_k(queries_with_labels, k)
        
        return {
            'mean_recall_at_k': mean_recall,
            'k': k,
            'num_queries': len(queries_with_labels),
            'per_query_results': per_query_results
        }
    
    def generate_predictions(
        self,
        test_queries: List[str],
        output_csv_path: str,
        k: int = 10
    ):
        """
        Generate predictions for test queries and save to CSV.
        
        Output CSV format:
        Query, Assessment_url
        Query 1, Recommendation 1 (URL)
        Query 1, Recommendation 2 (URL)
        ...
        Query 2, Recommendation 1 (URL)
        
        Args:
            test_queries: List of test query strings
            output_csv_path: Path to save predictions CSV
            k: Number of recommendations per query
        """
        with open(output_csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Query', 'Assessment_url'])
            
            for query in test_queries:
                recommendations = self.engine.recommend_balanced(query.strip(), max_results=k)
                
                for rec in recommendations:
                    writer.writerow([query, rec['url']])
        
        logger.info(f"Saved predictions to {output_csv_path}")
    
    def generate_predictions_from_csv(
        self,
        test_csv_path: str,
        output_csv_path: str,
        k: int = 10
    ):
        """
        Read test queries from CSV and generate predictions.
        
        Args:
            test_csv_path: Path to CSV containing test queries
            output_csv_path: Path to save predictions CSV
            k: Number of recommendations per query
        """
        test_queries = []
        
        with open(test_csv_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader, None)  # Skip header
            
            for row in reader:
                if row and row[0].strip():
                    test_queries.append(row[0].strip())
        
        logger.info(f"Loaded {len(test_queries)} test queries from {test_csv_path}")
        
        self.generate_predictions(test_queries, output_csv_path, k)


def load_train_data_json(filepath: str) -> List[Dict]:
    """Load labeled training data from JSON format."""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def print_evaluation_results(results: Dict):
    """Pretty print evaluation results."""
    print("\n" + "="*60)
    print("EVALUATION RESULTS")
    print("="*60)
    print(f"Mean Recall@{results['k']}: {results['mean_recall_at_k']:.4f}")
    print(f"Number of queries: {results['num_queries']}")
    print("\nPer-query breakdown:")
    print("-"*60)
    
    for r in results['per_query_results']:
        query_preview = r['query'][:50] + "..." if len(r['query']) > 50 else r['query']
        print(f"  Query: {query_preview}")
        print(f"    Recall@{results['k']}: {r['recall_at_k']:.4f}")
        print(f"    Relevant in top K: {r['relevant_in_top_k']}/{r['relevant_count']}")
        print()


# Sample labeled data for testing/development
SAMPLE_LABELED_DATA = [
    {
        "query": "I am hiring for Java developers who can also collaborate effectively with my business teams.",
        "relevant_urls": [
            "https://www.shl.com/solutions/products/product-catalog/view/java-8/",
            "https://www.shl.com/solutions/products/product-catalog/view/technology-professional-8-0-job-focused-assessment/",
            "https://www.shl.com/solutions/products/product-catalog/view/opq32/",
            "https://www.shl.com/solutions/products/product-catalog/view/team-dynamics/"
        ]
    },
    {
        "query": "Looking to hire mid-level professionals who are proficient in Python, SQL and JavaScript.",
        "relevant_urls": [
            "https://www.shl.com/solutions/products/product-catalog/view/python-new/",
            "https://www.shl.com/solutions/products/product-catalog/view/sql/",
            "https://www.shl.com/solutions/products/product-catalog/view/javascript/",
            "https://www.shl.com/solutions/products/product-catalog/view/software-engineer/"
        ]
    },
    {
        "query": "I am hiring for an analyst and want applications to screen using Cognitive and personality tests",
        "relevant_urls": [
            "https://www.shl.com/solutions/products/product-catalog/view/verify-g-plus/",
            "https://www.shl.com/solutions/products/product-catalog/view/numerical-reasoning/",
            "https://www.shl.com/solutions/products/product-catalog/view/opq32/",
            "https://www.shl.com/solutions/products/product-catalog/view/data-analyst/",
            "https://www.shl.com/solutions/products/product-catalog/view/critical-thinking/"
        ]
    },
    {
        "query": "Need a customer service representative who is empathetic and good at problem solving",
        "relevant_urls": [
            "https://www.shl.com/solutions/products/product-catalog/view/customer-service-sjt/",
            "https://www.shl.com/solutions/products/product-catalog/view/call-center-skills/",
            "https://www.shl.com/solutions/products/product-catalog/view/emotional-intelligence/",
            "https://www.shl.com/solutions/products/product-catalog/view/problem-solving/"
        ]
    },
    {
        "query": "Looking for a project manager with strong leadership and communication skills",
        "relevant_urls": [
            "https://www.shl.com/solutions/products/product-catalog/view/project-management/",
            "https://www.shl.com/solutions/products/product-catalog/view/leadership-assessment/",
            "https://www.shl.com/solutions/products/product-catalog/view/communication-assessment/",
            "https://www.shl.com/solutions/products/product-catalog/view/manager-plus/"
        ]
    }
]


if __name__ == "__main__":
    # Run evaluation using sample data
    print("Initializing recommendation engine...")
    engine = RecommendationEngine()
    evaluator = Evaluator(engine)
    
    print(f"\nTotal assessments in database: {engine.get_assessment_count()}")
    
    # Evaluate using sample labeled data
    print("\nRunning evaluation on sample labeled data...")
    mean_recall, per_query_results = evaluator.compute_mean_recall_at_k(
        SAMPLE_LABELED_DATA, k=10
    )
    
    results = {
        'mean_recall_at_k': mean_recall,
        'k': 10,
        'num_queries': len(SAMPLE_LABELED_DATA),
        'per_query_results': per_query_results
    }
    
    print_evaluation_results(results)
    
    # Generate sample predictions
    print("\nGenerating sample predictions...")
    test_queries = [q['query'] for q in SAMPLE_LABELED_DATA]
    output_path = os.path.join(os.path.dirname(__file__), 'data', 'sample_predictions.csv')
    evaluator.generate_predictions(test_queries, output_path, k=10)
    
    print(f"\nSample predictions saved to: {output_path}")
