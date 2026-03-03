# SHL Assessment Recommendation System

An intelligent recommendation system that suggests relevant SHL assessments based on job descriptions or natural language queries.

## Features

- **Natural Language Query Support**: Enter job descriptions or queries in plain English
- **URL Support**: Paste a job posting URL and the system extracts the description
- **Semantic Search**: Uses sentence embeddings for accurate semantic matching
- **Balanced Recommendations**: Intelligently balances technical vs. behavioral assessments
- **REST API**: Easy-to-use API endpoints for integration
- **Web Interface**: User-friendly web interface for testing

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd shl_assessment_system
```

2. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. (Optional) Set up environment variables:
```bash
# Create .env file
GEMINI_API_KEY=your-gemini-api-key  # Optional, for enhanced query understanding
EMBEDDING_MODEL=all-MiniLM-L6-v2    # Default embedding model
```

## Running the Application

### Start the Server

```bash
python app.py
```

The server will start on `http://localhost:5000`

### API Endpoints

#### Health Check
```
GET /health

Response:
{
    "status": "healthy"
}
```

#### Get Recommendations
```
POST /recommend
Content-Type: application/json

Request:
{
    "query": "I am hiring for Java developers who can also collaborate effectively with my business teams."
}

Response:
{
    "recommended_assessments": [
        {
            "url": "https://www.shl.com/...",
            "name": "Java 8",
            "adaptive_support": "No",
            "description": "...",
            "duration": 20,
            "remote_support": "Yes",
            "test_type": ["Knowledge & Skills"]
        },
        ...
    ]
}
```

### Web Interface

Open `http://localhost:5000` in your browser for the interactive web interface.

## Project Structure

```
shl_assessment_system/
├── app.py                    # Flask API application
├── config.py                 # Configuration settings
├── recommendation_engine.py  # Core recommendation logic
├── scraper.py               # SHL catalog web scraper
├── evaluation.py            # Evaluation metrics and tools
├── requirements.txt         # Python dependencies
├── data/
│   ├── shl_assessments.json # Assessment catalog data
│   └── embeddings/          # Cached embeddings
├── templates/
│   └── index.html           # Web interface
└── README.md
```

## How It Works

1. **Data Collection**: The scraper collects assessment data from SHL's product catalog, including names, descriptions, test types, duration, and other metadata.

2. **Embedding Creation**: Each assessment is converted to a vector embedding using sentence transformers for semantic similarity matching.

3. **Query Processing**: When a user submits a query:
   - If it's a URL, the system extracts the job description
   - The query is enhanced with extracted requirements (using LLM if available)
   - Query embedding is computed

4. **Similarity Search**: Cosine similarity is computed between the query and all assessments.

5. **Result Ranking**: Results are boosted based on category matching and balanced for multi-domain queries.

## Test Types

The system supports all SHL test types:
- **A** - Ability & Aptitude
- **B** - Biodata & Situational Judgement
- **C** - Competencies
- **D** - Development & 360
- **E** - Assessment Exercises
- **K** - Knowledge & Skills
- **P** - Personality & Behaviour
- **S** - Simulations

## Evaluation

Run evaluation on labeled data:

```bash
python evaluation.py
```

This computes Mean Recall@K and other metrics.

## Sample Queries

- "I am hiring for Java developers who can also collaborate effectively with my business teams."
- "Looking to hire mid-level professionals who are proficient in Python, SQL and JavaScript."
- "Need a customer service representative who is empathetic and good at problem solving"

## Deployment

For production deployment:

```bash
# Using gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# With environment variables
export DEBUG=False
export PORT=5000
python app.py
```

## License

MIT License
