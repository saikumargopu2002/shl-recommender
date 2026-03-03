"""
Script to generate predictions on the test set.

Usage:
    python generate_predictions.py --test-file test_queries.csv --output predictions.csv
    
Or with direct queries:
    python generate_predictions.py --queries "Query 1" "Query 2" --output predictions.csv
"""
import argparse
import csv
import os
import sys
from typing import List

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from recommendation_engine import RecommendationEngine


def load_queries_from_csv(filepath: str) -> List[str]:
    """Load queries from a CSV file."""
    queries = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader, None)  # Skip header
        
        for row in reader:
            if row and row[0].strip():
                queries.append(row[0].strip())
    
    return queries


def generate_predictions(
    engine: RecommendationEngine,
    queries: List[str],
    output_path: str,
    max_results: int = 10
):
    """Generate predictions and save to CSV."""
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Query', 'Assessment_url'])
        
        for query in queries:
            print(f"\nProcessing: {query[:50]}...")
            recommendations = engine.recommend_balanced(query, max_results=max_results)
            
            print(f"  Found {len(recommendations)} recommendations")
            
            for rec in recommendations:
                writer.writerow([query, rec['url']])
    
    print(f"\n✓ Predictions saved to: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description='Generate SHL assessment predictions for test queries'
    )
    
    parser.add_argument(
        '--test-file',
        type=str,
        help='Path to CSV file containing test queries'
    )
    
    parser.add_argument(
        '--queries',
        nargs='+',
        help='List of queries to process'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default='predictions.csv',
        help='Output CSV file path (default: predictions.csv)'
    )
    
    parser.add_argument(
        '--max-results',
        type=int,
        default=10,
        help='Maximum recommendations per query (default: 10)'
    )
    
    args = parser.parse_args()
    
    # Get queries
    queries = []
    
    if args.test_file:
        if not os.path.exists(args.test_file):
            print(f"Error: Test file not found: {args.test_file}")
            sys.exit(1)
        queries = load_queries_from_csv(args.test_file)
        print(f"Loaded {len(queries)} queries from {args.test_file}")
    
    elif args.queries:
        queries = args.queries
        print(f"Processing {len(queries)} queries from command line")
    
    else:
        # Use sample test queries
        queries = [
            "I am hiring for Java developers who can also collaborate effectively with my business teams.",
            "Looking to hire mid-level professionals who are proficient in Python, SQL and JavaScript.",
            "I need to assess candidates for a data analyst position requiring both technical skills and analytical thinking.",
            "We're looking for a customer service manager who can lead a team and handle difficult customers.",
            "Searching for software engineers with DevOps experience and strong communication skills.",
            "Need assessments for entry-level sales representatives who will work with enterprise clients.",
            "Looking for a product manager who can bridge technical and business teams.",
            "Hiring for QA engineers who need strong attention to detail and testing methodology knowledge.",
            "We need to assess candidates for a finance manager role requiring numerical skills and leadership."
        ]
        print(f"Using {len(queries)} sample test queries")
    
    if not queries:
        print("Error: No queries to process")
        sys.exit(1)
    
    # Initialize engine
    print("\nInitializing recommendation engine...")
    engine = RecommendationEngine()
    print(f"Loaded {engine.get_assessment_count()} assessments")
    
    # Generate predictions
    generate_predictions(engine, queries, args.output, args.max_results)
    
    # Show sample of results
    print("\nSample of generated predictions:")
    with open(args.output, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:  # Header
                continue
            if i > 5:  # Show first 5
                print("  ...")
                break
            print(f"  {row[0][:30]}... -> {row[1]}")


if __name__ == '__main__':
    main()
