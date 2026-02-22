from app_pilot.core.factory import create_vector_db

def main():
    # Create the vector database service
    vector_db_service = create_vector_db()

    # Example usage of the vector database service
    print("VectorDBService created successfully!")
    # You can add more functionality here, like querying the database.

if __name__ == "__main__":
    main()