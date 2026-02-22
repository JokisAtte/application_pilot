class VectorDBService:
    def __init__(self, index):
        self.index = index

    def query(self, query_text):
        # Example method to query the vector database
        return self.index.query(query_text)