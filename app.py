"""
SHL Assessment Recommendation API

Flask application providing REST API endpoints for assessment recommendations.
"""
import os
import re
import logging
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create Flask app
app = Flask(__name__,
            static_folder='static',
            template_folder='templates')

# Enable CORS for API access
CORS(app)

# Initialize recommendation engine (lazy loading)
_engine = None


def get_engine():
    """Lazy load the recommendation engine."""
    global _engine
    if _engine is None:
        from recommendation_engine import RecommendationEngine
        _engine = RecommendationEngine()
    return _engine


def extract_text_from_url(url: str) -> str:
    """Extract job description text from a URL."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'lxml')
        
        # Remove script and style elements
        for script in soup(['script', 'style', 'nav', 'footer', 'header']):
            script.decompose()
        
        # Try to find job description content
        # Look for common job posting containers
        selectors = [
            '.job-description',
            '.description',
            '#job-description',
            '.job-details',
            '[data-testid="jobDescriptionText"]',
            '.jobsearch-jobDescriptionText',
            'article',
            'main',
            '.content'
        ]
        
        text = ''
        for selector in selectors:
            element = soup.select_one(selector)
            if element:
                text = element.get_text(separator=' ', strip=True)
                if len(text) > 100:  # Reasonable content length
                    break
        
        # Fallback to body text
        if len(text) < 100:
            text = soup.body.get_text(separator=' ', strip=True) if soup.body else ''
        
        # Clean up text
        text = re.sub(r'\s+', ' ', text)
        text = text[:5000]  # Limit length
        
        return text
        
    except Exception as e:
        logger.error(f"Failed to extract text from URL {url}: {e}")
        return ''


def is_url(text: str) -> bool:
    """Check if the text is a URL."""
    url_pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain
        r'localhost|'  # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return bool(url_pattern.match(text.strip()))


# ====================
# API ENDPOINTS
# ====================

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint.
    
    Returns:
        JSON with status "healthy" and 200 OK if the API is running.
    """
    return jsonify({"status": "healthy"}), 200


@app.route('/recommend', methods=['POST'])
def recommend():
    """
    Assessment recommendation endpoint.
    
    Accepts a job description or natural language query and returns
    recommended assessments.
    
    Request Body:
        {
            "query": "Job description text or URL or natural language query"
        }
    
    Returns:
        {
            "recommended_assessments": [
                {
                    "url": "Valid URL to the assessment resource",
                    "name": "Name of the assessment",
                    "adaptive_support": "Yes/No",
                    "description": "Detailed description of the assessment",
                    "duration": 60,
                    "remote_support": "Yes/No",
                    "test_type": ["Knowledge & Skills", "Personality & Behaviour"]
                },
                ...
            ]
        }
    """
    try:
        # Get request data
        data = request.get_json()
        
        if not data:
            return jsonify({
                "error": "Invalid request. Please provide JSON body with 'query' field."
            }), 400
        
        query = data.get('query', '')
        
        if not query or not query.strip():
            return jsonify({
                "error": "Missing or empty 'query' field."
            }), 400
        
        query = query.strip()
        
        # Check if query is a URL and extract text
        if is_url(query):
            logger.info(f"Extracting job description from URL: {query}")
            extracted_text = extract_text_from_url(query)
            
            if not extracted_text:
                return jsonify({
                    "error": "Could not extract job description from the provided URL."
                }), 400
            
            query = extracted_text
        
        # Get recommendations
        engine = get_engine()
        recommendations = engine.recommend_balanced(query, max_results=10)
        
        # Format response (remove internal score field)
        formatted_recommendations = []
        for rec in recommendations:
            formatted_rec = {
                "url": rec.get('url', ''),
                "name": rec.get('name', ''),
                "adaptive_support": rec.get('adaptive_support', 'No'),
                "description": rec.get('description', ''),
                "duration": rec.get('duration', 0),
                "remote_support": rec.get('remote_support', 'No'),
                "test_type": rec.get('test_type', [])
            }
            formatted_recommendations.append(formatted_rec)
        
        return jsonify({
            "recommended_assessments": formatted_recommendations
        }), 200
        
    except Exception as e:
        logger.exception(f"Error processing recommendation request: {e}")
        return jsonify({
            "error": f"Internal server error: {str(e)}"
        }), 500


@app.route('/api/assessments', methods=['GET'])
def get_assessments():
    """Get all available assessments."""
    try:
        engine = get_engine()
        return jsonify({
            "total": engine.get_assessment_count(),
            "test_types": engine.get_test_types(),
            "assessments": engine.assessments[:50]  # Return first 50 for preview
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get system statistics."""
    try:
        engine = get_engine()
        
        # Count by test type
        type_counts = {}
        for assessment in engine.assessments:
            for t in assessment.get('test_type', []):
                type_counts[t] = type_counts.get(t, 0) + 1
        
        return jsonify({
            "total_assessments": engine.get_assessment_count(),
            "test_types": engine.get_test_types(),
            "type_counts": type_counts
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ====================
# WEB INTERFACE
# ====================

@app.route('/')
def index():
    """Render the main web interface."""
    return render_template('index.html')


@app.route('/static/<path:path>')
def serve_static(path):
    """Serve static files."""
    return send_from_directory('static', path)


# ====================
# ERROR HANDLERS
# ====================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({"error": "Internal server error"}), 500


@app.errorhandler(405)
def method_not_allowed(error):
    """Handle 405 errors."""
    return jsonify({"error": "Method not allowed"}), 405


# ====================
# MAIN
# ====================

if __name__ == '__main__':
    # Get configuration from environment
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'True').lower() == 'true'
    
    logger.info(f"Starting SHL Assessment Recommendation API on {host}:{port}")
    logger.info(f"Debug mode: {debug}")
    
    # Pre-load the recommendation engine
    logger.info("Pre-loading recommendation engine...")
    engine = get_engine()
    logger.info(f"Loaded {engine.get_assessment_count()} assessments")
    
    # Run the app
    app.run(host=host, port=port, debug=debug)
