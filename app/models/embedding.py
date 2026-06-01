import os

from langchain_google_genai import GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv
load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model=os.getenv("MODEL_EMBED"),
    google_api_key=os.getenv("GOOGLE_API_KEY")
)