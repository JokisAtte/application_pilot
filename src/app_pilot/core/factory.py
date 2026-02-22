import os
import json
from llama_index.core import StorageContext, load_index_from_storage, VectorStoreIndex, Document
from app_pilot.services import VectorDBService
from app_pilot.services import StyleService
# In the testing and validation PoC phase we can manually pass true to manualReload to always recalculate the index after changing the data
# Leter this needs to be done dynamically, when data has changed
def create_vector_db(manualReload: False) -> VectorDBService:
    storage_path = "./storage"
    data_folder = "../../data"
    
    if (os.path.exists(storage_path) and os.listdir(storage_path)) or manualReload == False:
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

def get_style_guide(style_service: StyleService, manualReload: False) -> str:
    data_folder = "../../data"
    style_guide_path = os.path.join(data_folder, "style_guide.json")

    # Check if the style guide file exists
    if not os.path.exists(style_guide_path):
        # If the file does not exist, generate it using the StyleService
        print(f"Style guide file not found. Generating a new one at {style_guide_path}...")
        os.makedirs(data_folder, exist_ok=True)  # Ensure the data folder exists

        # Generate the style guide using the StyleService
        style_guide_data = style_service.generate_style_guide()  # Assuming this method generates the guide

        # Save the generated style guide to the file
        with open(style_guide_path, "w", encoding="utf-8") as f:
            json.dump(style_guide_data, f, indent=4)

    # Load the style guide from the file
    with open(style_guide_path, "r", encoding="utf-8") as f:
        style_guide_contents = f.read()

    return style_guide_contents
    
