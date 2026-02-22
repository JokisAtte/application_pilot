import os
import json
from llama_index.core import StorageContext, load_index_from_storage, VectorStoreIndex, Document
from app_pilot.services import VectorDBService

def create_vector_db() -> VectorDBService:
    storage_path = "./storage"
    data_folder = "../../data"
    
    if os.path.exists(storage_path) and os.listdir(storage_path):
        # Production: Load from disk
        sc = StorageContext.from_defaults(persist_dir=storage_path)
        index = load_index_from_storage(sc)
    else:
        # Initial Setup: Create empty index from JSON files in the data folder
        documents = []
        for filename in os.listdir(data_folder):
            if filename.endswith(".json"): 
                file_path = os.path.join(data_folder, filename)
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    # Convert the dictionary into a Document object
                    document = Document(text=json.dumps(data), metadata={"filename": filename})
                    documents.append(document)

        # Create the index from the loaded documents
        index = VectorStoreIndex.from_documents(documents)
        
    return VectorDBService(index=index)