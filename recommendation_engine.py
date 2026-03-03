"""
SHL Assessment Recommendation Engine

Uses embeddings and semantic search to recommend relevant assessments
based on job descriptions or natural language queries.
"""
import os
import json
import pickle
import re
import logging
from typing import List, Dict, Optional, Tuple
import numpy as np

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Attempt to import optional dependencies
try:
    from sentence_transformers import SentenceTransformer  # type: ignore
    SENTENCE_TRANSFORMERS_AVAILABLE = True
except ImportError:
    SENTENCE_TRANSFORMERS_AVAILABLE = False
    logger.warning("sentence-transformers not installed. Using TF-IDF fallback.")

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False
    logger.warning("sklearn not installed.")

try:
    import google.generativeai as genai  # type: ignore
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    logger.warning("google-generativeai not installed.")
    genai = None  # type: ignore


class RecommendationEngine:
    """
    Recommendation engine for SHL assessments using semantic search.
    
    Uses sentence embeddings for semantic similarity matching between
    job descriptions/queries and assessment descriptions.
    """
    
    def __init__(self, data_dir: str = None):
        """Initialize the recommendation engine."""
        self.data_dir = data_dir or os.path.join(os.path.dirname(__file__), 'data')
        self.assessments: List[Dict] = []
        self.embeddings: Optional[np.ndarray] = None
        self.model = None
        self.tfidf_vectorizer = None
        self.tfidf_matrix = None
        
        # Paths
        self.assessments_file = os.path.join(self.data_dir, 'shl_assessments.json')
        self.embeddings_file = os.path.join(self.data_dir, 'embeddings', 'assessment_embeddings.pkl')
        
        # Initialize model
        self._init_model()
        
        # Load data
        self._load_assessments()
        self._load_or_create_embeddings()
    
    def _init_model(self):
        """Initialize the embedding model."""
        if SENTENCE_TRANSFORMERS_AVAILABLE:
            try:
                model_name = os.environ.get('EMBEDDING_MODEL', 'all-MiniLM-L6-v2')
                logger.info(f"Loading sentence transformer model: {model_name}")
                self.model = SentenceTransformer(model_name)
                logger.info("Model loaded successfully")
            except Exception as e:
                logger.warning(f"Failed to load sentence transformer: {e}")
                self.model = None
        
        # Fallback to TF-IDF if sentence transformers not available
        if self.model is None and SKLEARN_AVAILABLE:
            logger.info("Using TF-IDF vectorizer as fallback")
            self.tfidf_vectorizer = TfidfVectorizer(
                ngram_range=(1, 2),
                max_features=5000,
                stop_words='english'
            )
    
    def _load_assessments(self):
        """Load assessments from JSON file or create sample data."""
        if os.path.exists(self.assessments_file):
            with open(self.assessments_file, 'r', encoding='utf-8') as f:
                self.assessments = json.load(f)
            logger.info(f"Loaded {len(self.assessments)} assessments from file")
        else:
            # Create sample data
            from scraper import create_sample_assessments
            self.assessments = create_sample_assessments()
            
            # Save for future use
            os.makedirs(os.path.dirname(self.assessments_file), exist_ok=True)
            with open(self.assessments_file, 'w', encoding='utf-8') as f:
                json.dump(self.assessments, f, indent=2)
            logger.info(f"Created and saved {len(self.assessments)} sample assessments")
    
    def _create_assessment_text(self, assessment: Dict) -> str:
        """Create searchable text representation of an assessment."""
        parts = [
            assessment.get('name', ''),
            assessment.get('description', ''),
        ]
        
        # Add test types
        test_types = assessment.get('test_type', [])
        if test_types:
            parts.append(' '.join(test_types))
        
        return ' '.join(parts)
    
    def _load_or_create_embeddings(self):
        """Load existing embeddings or create new ones."""
        os.makedirs(os.path.dirname(self.embeddings_file), exist_ok=True)
        
        # Check if embeddings exist and are compatible
        if os.path.exists(self.embeddings_file):
            try:
                with open(self.embeddings_file, 'rb') as f:
                    data = pickle.load(f)
                
                # Check if embeddings match current assessments
                if data.get('count') == len(self.assessments):
                    if self.model is not None:
                        self.embeddings = data.get('embeddings')
                        logger.info(f"Loaded {len(self.embeddings)} embeddings from cache")
                        return
                    elif self.tfidf_vectorizer is not None:
                        self.tfidf_matrix = data.get('tfidf_matrix')
                        self.tfidf_vectorizer = data.get('tfidf_vectorizer')
                        if self.tfidf_matrix is not None:
                            logger.info("Loaded TF-IDF matrix from cache")
                            return
            except Exception as e:
                logger.warning(f"Failed to load embeddings: {e}")
        
        # Create new embeddings
        self._create_embeddings()
    
    def _create_embeddings(self):
        """Create embeddings for all assessments."""
        logger.info("Creating embeddings for assessments...")
        
        # Get texts for all assessments
        texts = [self._create_assessment_text(a) for a in self.assessments]
        
        if self.model is not None:
            # Use sentence transformers
            self.embeddings = self.model.encode(texts, show_progress_bar=True)
            
            # Save embeddings
            with open(self.embeddings_file, 'wb') as f:
                pickle.dump({
                    'embeddings': self.embeddings,
                    'count': len(self.assessments)
                }, f)
        
        elif self.tfidf_vectorizer is not None:
            # Use TF-IDF
            self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(texts)
            
            # Save TF-IDF data
            with open(self.embeddings_file, 'wb') as f:
                pickle.dump({
                    'tfidf_matrix': self.tfidf_matrix,
                    'tfidf_vectorizer': self.tfidf_vectorizer,
                    'count': len(self.assessments)
                }, f)
        
        logger.info("Embeddings created and saved")
    
    def _extract_requirements_with_llm(self, query: str) -> Dict:
        """Use LLM to extract structured requirements from query."""
        if not GEMINI_AVAILABLE:
            return {}
        
        api_key = os.environ.get('GEMINI_API_KEY', '')
        if not api_key:
            return {}
        
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')
            
            prompt = f"""Analyze this job description or query and extract the key requirements:

Query: {query}

Extract and return a JSON object with:
1. "technical_skills": list of technical skills required (programming languages, tools, technologies)
2. "soft_skills": list of soft skills or behavioral competencies required
3. "domain": the industry or domain (e.g., IT, Finance, Sales, Healthcare)
4. "role_level": experience level (Entry, Mid, Senior, Manager, Executive)
5. "key_responsibilities": main job responsibilities

Return only valid JSON, no explanation."""

            response = model.generate_content(prompt)
            
            # Parse JSON response
            text = response.text.strip()
            # Clean up markdown code blocks if present
            if text.startswith('```'):
                text = text.split('```')[1]
                if text.startswith('json'):
                    text = text[4:]
            
            return json.loads(text)
        
        except Exception as e:
            logger.warning(f"LLM extraction failed: {e}")
            return {}
    
    def _compute_similarity(self, query: str) -> np.ndarray:
        """Compute similarity scores between query and all assessments."""
        if self.model is not None and self.embeddings is not None:
            # Use sentence embeddings
            query_embedding = self.model.encode([query])
            
            # Compute cosine similarity
            similarities = cosine_similarity(query_embedding, self.embeddings)[0]
            
        elif self.tfidf_vectorizer is not None and self.tfidf_matrix is not None:
            # Use TF-IDF
            query_vector = self.tfidf_vectorizer.transform([query])
            similarities = cosine_similarity(query_vector, self.tfidf_matrix)[0]
        
        else:
            # Simple keyword matching fallback
            query_lower = query.lower()
            query_words = set(query_lower.split())
            
            similarities = []
            for assessment in self.assessments:
                text = self._create_assessment_text(assessment).lower()
                text_words = set(text.split())
                
                # Jaccard similarity
                intersection = len(query_words & text_words)
                union = len(query_words | text_words)
                score = intersection / max(union, 1)
                similarities.append(score)
            
            similarities = np.array(similarities)
        
        return similarities
    
    def _boost_scores_by_category(self, scores: np.ndarray, query: str) -> np.ndarray:
        """Boost scores based on query requirements matching test types."""
        query_lower = query.lower()
        
        # Define category boosting keywords
        category_keywords = {
            'Knowledge & Skills': [
                'programming', 'coding', 'technical', 'python', 'java', 'javascript',
                'sql', 'database', 'developer', 'software', 'engineer', 'technology',
                'technical skills', 'hard skills', 'proficient', 'expertise', 'knowledge'
            ],
            'Personality & Behaviour': [
                'personality', 'behavioral', 'behaviour', 'soft skills', 'interpersonal',
                'collaborate', 'collaboration', 'teamwork', 'communication', 'leadership',
                'culture fit', 'attitude', 'work style', 'motivation'
            ],
            'Ability & Aptitude': [
                'cognitive', 'aptitude', 'reasoning', 'analytical', 'problem solving',
                'logical', 'numerical', 'verbal', 'aptitude test', 'intelligence',
                'mental ability', 'critical thinking'
            ],
            'Competencies': [
                'competency', 'competencies', 'professional', 'job performance',
                'skills assessment', 'capability', 'management', 'leadership skills'
            ],
            'Biodata & Situational Judgement': [
                'situational', 'judgment', 'situational judgment', 'sjt', 'scenarios',
                'decision making', 'work situations', 'biodata'
            ],
            'Simulations': [
                'simulation', 'hands-on', 'practical', 'exercise', 'role play',
                'inbox', 'case study', 'realistic'
            ]
        }
        
        # Detect required categories
        required_categories = []
        for category, keywords in category_keywords.items():
            for keyword in keywords:
                if keyword in query_lower:
                    required_categories.append(category)
                    break
        
        # Apply boosts
        boosted_scores = scores.copy()
        
        for i, assessment in enumerate(self.assessments):
            test_types = assessment.get('test_type', [])
            
            for category in required_categories:
                if category in test_types:
                    boosted_scores[i] *= 1.3  # 30% boost
        
        # Balance technical and behavioral if both are mentioned
        has_technical = any(kw in query_lower for kw in ['technical', 'programming', 'coding', 'developer'])
        has_behavioral = any(kw in query_lower for kw in ['collaborate', 'team', 'communication', 'personality', 'behavioral'])
        
        if has_technical and has_behavioral:
            # Boost assessments that cover both
            for i, assessment in enumerate(self.assessments):
                test_types = assessment.get('test_type', [])
                
                is_technical = 'Knowledge & Skills' in test_types
                is_behavioral = 'Personality & Behaviour' in test_types or 'Competencies' in test_types
                
                if len(test_types) > 1 or (is_technical and is_behavioral):
                    boosted_scores[i] *= 1.2  # Additional 20% boost for multi-category
        
        return boosted_scores
    
    def recommend(
        self,
        query: str,
        max_results: int = 10,
        min_results: int = 1
    ) -> List[Dict]:
        """
        Get assessment recommendations for a query or job description.
        
        Args:
            query: Natural language query or job description text
            max_results: Maximum number of recommendations (1-10)
            min_results: Minimum number of recommendations
            
        Returns:
            List of recommended assessments with metadata
        """
        # Validate inputs
        max_results = min(max(max_results, min_results), 10)
        
        if not query or not query.strip():
            return []
        
        # Clean query
        query = query.strip()
        
        # Try to extract structured requirements using LLM
        requirements = self._extract_requirements_with_llm(query)
        
        # Enhance query with extracted requirements
        enhanced_query = query
        if requirements:
            if requirements.get('technical_skills'):
                enhanced_query += ' ' + ' '.join(requirements['technical_skills'])
            if requirements.get('soft_skills'):
                enhanced_query += ' ' + ' '.join(requirements['soft_skills'])
        
        # Compute similarities
        scores = self._compute_similarity(enhanced_query)
        
        # Boost by category matching
        scores = self._boost_scores_by_category(scores, query)
        
        # Get top indices
        top_indices = np.argsort(scores)[::-1][:max_results]
        
        # Build results
        results = []
        for idx in top_indices:
            assessment = self.assessments[idx]
            score = scores[idx]
            
            # Skip very low scores
            if score < 0.01 and len(results) >= min_results:
                continue
            
            result = {
                'url': assessment.get('url', ''),
                'name': assessment.get('name', ''),
                'adaptive_support': assessment.get('adaptive_support', 'No'),
                'description': assessment.get('description', ''),
                'duration': assessment.get('duration', 0),
                'remote_support': assessment.get('remote_support', 'No'),
                'test_type': assessment.get('test_type', []),
                'score': float(score)  # Include score for debugging
            }
            results.append(result)
        
        return results
    
    def recommend_balanced(
        self,
        query: str,
        max_results: int = 10
    ) -> List[Dict]:
        """
        Get balanced recommendations ensuring coverage of different test types.
        
        For queries spanning multiple domains, this ensures a balanced mix
        of assessments from different categories.
        """
        # Get initial recommendations
        all_recommendations = self.recommend(query, max_results=max_results * 2)
        
        if not all_recommendations:
            return []
        
        query_lower = query.lower()
        
        # Check if query spans multiple domains
        has_technical = any(kw in query_lower for kw in [
            'java', 'python', 'javascript', 'sql', 'programming', 'coding',
            'developer', 'software', 'technical', 'technology', 'engineer'
        ])
        has_behavioral = any(kw in query_lower for kw in [
            'collaborate', 'team', 'stakeholder', 'communication', 'leadership',
            'behavioral', 'personality', 'soft skills', 'interpersonal'
        ])
        has_cognitive = any(kw in query_lower for kw in [
            'cognitive', 'aptitude', 'reasoning', 'analytical', 'problem solving'
        ])
        
        domains_count = sum([has_technical, has_behavioral, has_cognitive])
        
        if domains_count <= 1:
            # Single domain - return top results
            return all_recommendations[:max_results]
        
        # Multiple domains - balance results
        balanced_results = []
        category_counts = {}
        
        # First pass: add top result from each required category
        for rec in all_recommendations:
            test_types = rec.get('test_type', [])
            
            for test_type in test_types:
                if test_type not in category_counts:
                    category_counts[test_type] = 0
                
                # Check if this category is relevant
                is_relevant = False
                if has_technical and test_type == 'Knowledge & Skills':
                    is_relevant = True
                if has_behavioral and test_type in ['Personality & Behaviour', 'Competencies']:
                    is_relevant = True
                if has_cognitive and test_type == 'Ability & Aptitude':
                    is_relevant = True
                
                if is_relevant and category_counts[test_type] < 3:
                    if rec not in balanced_results:
                        balanced_results.append(rec)
                        category_counts[test_type] += 1
                        break
            
            if len(balanced_results) >= max_results:
                break
        
        # Fill remaining slots with top scoring results
        for rec in all_recommendations:
            if rec not in balanced_results:
                balanced_results.append(rec)
            if len(balanced_results) >= max_results:
                break
        
        return balanced_results[:max_results]
    
    def get_assessment_count(self) -> int:
        """Get total number of assessments in the database."""
        return len(self.assessments)
    
    def get_test_types(self) -> List[str]:
        """Get all unique test types."""
        types = set()
        for assessment in self.assessments:
            for t in assessment.get('test_type', []):
                types.add(t)
        return sorted(list(types))


# Singleton instance for API usage
_engine_instance: Optional[RecommendationEngine] = None


def get_engine() -> RecommendationEngine:
    """Get or create the recommendation engine singleton."""
    global _engine_instance
    if _engine_instance is None:
        _engine_instance = RecommendationEngine()
    return _engine_instance


if __name__ == "__main__":
    # Test the recommendation engine
    engine = RecommendationEngine()
    
    print(f"Total assessments: {engine.get_assessment_count()}")
    print(f"Test types: {engine.get_test_types()}")
    
    # Test queries
    test_queries = [
        "I am hiring for Java developers who can also collaborate effectively with my business teams.",
        "Looking to hire mid-level professionals who are proficient in Python, SQL and JavaScript.",
        "I am hiring for an analyst and want applications to screen using Cognitive and personality tests"
    ]
    
    for query in test_queries:
        print(f"\n{'='*80}")
        print(f"Query: {query}")
        print('='*80)
        
        recommendations = engine.recommend_balanced(query, max_results=5)
        
        for i, rec in enumerate(recommendations, 1):
            print(f"\n{i}. {rec['name']}")
            print(f"   URL: {rec['url']}")
            print(f"   Types: {', '.join(rec['test_type'])}")
            print(f"   Duration: {rec['duration']} min")
