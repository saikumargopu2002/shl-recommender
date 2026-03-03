"""Initialize the assessment data for the SHL Recommendation System."""
import json
import os
from scraper import create_sample_assessments

def main():
    # Create data directory
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    # Create embeddings directory
    embeddings_dir = os.path.join(data_dir, 'embeddings')
    os.makedirs(embeddings_dir, exist_ok=True)
    
    # Generate sample assessments
    print("Generating assessment data...")
    data = create_sample_assessments()
    print(f"Created {len(data)} assessments")
    
    # Save to JSON
    output_path = os.path.join(data_dir, 'shl_assessments.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Saved to: {output_path}")
    
    # Print summary by test type
    print("\nAssessments by test type:")
    type_counts = {}
    for assessment in data:
        for t in assessment.get('test_type', []):
            type_counts[t] = type_counts.get(t, 0) + 1
    
    for t, count in sorted(type_counts.items()):
        print(f"  {t}: {count}")

if __name__ == '__main__':
    main()
