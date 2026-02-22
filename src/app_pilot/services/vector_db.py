from typing import List, Optional
from llama_index.core.base.base_retriever import BaseRetriever
from app_pilot.models import WorkExperience, PreviousApplicationStyleSample
import os
from llama_index.core import (
    VectorStoreIndex, 
    SimpleDirectoryReader, 
    StorageContext, 
    load_index_from_storage,
    Document
)

class VectorDBService:
    def __init__(self, index: VectorStoreIndex):
        """
        Allows us to use an in-memory index for tests and a persistent one for production.
        """
        self.index = index
        self._retriever: Optional[BaseRetriever] = None

    def _initialize_index(self):
        if not os.path.exists(self.persist_dir):
            print(f"DEBUG: No index found at {self.persist_dir}. Creating...")
            # Ensure the data directory actually exists before reading
            if not os.path.exists(self.data_dir):
                os.makedirs(self.data_dir)
                
            documents = SimpleDirectoryReader(self.data_dir).load_data()
            index = VectorStoreIndex.from_documents(documents)
            index.storage_context.persist(persist_dir=self.persist_dir)
            return index
        else:
            print(f"DEBUG: Loading existing index from {self.persist_dir}")
            storage_context = StorageContext.from_defaults(persist_dir=self.persist_dir)
            return load_index_from_storage(storage_context)
    
    @property
    def retriever(self) -> BaseRetriever:
        if self._retriever is None:
            # We configure the search behavior here (Top-K)
            self._retriever = self.index.as_retriever(similarity_top_k=3)
        return self._retriever

    def query(self, text: str):
        """Standard query method for validation."""
        return self.retriever.retrieve(text)

    def add_documents(self, documents: List[Document]):
        """Allows adding new data dynamically."""
        for doc in documents:
            self.index.insert(doc)
    
    