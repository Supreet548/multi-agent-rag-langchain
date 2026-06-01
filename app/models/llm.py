import os

from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model=os.getenv("MODEL_CHAT"),
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0
)