"""
Configuration for SHL Assessment Recommendation System
"""
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    """Application configuration"""
    # Flask
    SECRET_KEY = os.environ.get('SECRET_KEY', 'shl-assessment-secret-key')
    DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    # Data paths
    DATA_DIR = os.path.join(basedir, 'data')
    ASSESSMENTS_FILE = os.path.join(DATA_DIR, 'shl_assessments.json')
    EMBEDDINGS_DIR = os.path.join(DATA_DIR, 'embeddings')
    VECTOR_DB_DIR = os.path.join(DATA_DIR, 'vector_db')
    
    # SHL Catalog URL
    SHL_CATALOG_URL = "https://www.shl.com/solutions/products/product-catalog/"
    SHL_BASE_URL = "https://www.shl.com"
    
    # Embedding model
    EMBEDDING_MODEL = os.environ.get('EMBEDDING_MODEL', 'all-MiniLM-L6-v2')
    
    # LLM Configuration (Gemini)
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')
    
    # OpenAI Configuration (alternative)
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')
    
    # Recommendation settings
    MIN_RECOMMENDATIONS = 1
    MAX_RECOMMENDATIONS = 10
    DEFAULT_RECOMMENDATIONS = 10
    
    # Scraping settings
    SCRAPE_DELAY = 1  # seconds between requests
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    
    # Server
    HOST = os.environ.get('HOST', '0.0.0.0')
    PORT = int(os.environ.get('PORT', 5000))


# Create directories if they don't exist
os.makedirs(Config.DATA_DIR, exist_ok=True)
os.makedirs(Config.EMBEDDINGS_DIR, exist_ok=True)
os.makedirs(Config.VECTOR_DB_DIR, exist_ok=True)
