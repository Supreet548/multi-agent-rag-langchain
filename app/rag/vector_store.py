from langchain_chroma import Chroma
from app.models.embedding import embeddings

VECTOR_DB_PATH = "chroma_db"
COLLECTION_NAME = "api_docs"

vector_store = Chroma(
    persist_directory=VECTOR_DB_PATH,
    embedding_function=embeddings,
    collection_name=COLLECTION_NAME
)