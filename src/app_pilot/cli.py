from app_pilot.services import VectorDBService, StyleService
from app_pilot.core.factory import create_vector_db, get_style_guide
from dotenv import load_dotenv
import os

load_dotenv()

def test_retrieval():
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY is not set. Please check your .env file.")
    
    db = create_vector_db(True)
    style_service = StyleService()
    style_guide = get_style_guide(True)
    # Test 1: Technical Match
    query = "Looking for principal full stack developer for a technical project manager role. You must understand nextjs, React and project management"
    print(f"\n--- Testing Query: '{query}' ---")
    nodes = db.query(query)
    for i, node in enumerate(nodes):
        # Professional check: Look at the 'score' (cosine similarity)
        # 0.8+ is great, < 0.7 usually means "low relevance"
        print(f"Match {i+1} [Score: {node.score:.4f}]:")
        print(f"Content: {node.text[:150]}...")
        print(f"Metadata: {node.metadata}\n")

if __name__ == "__main__":
    test_retrieval()