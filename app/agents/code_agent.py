from app.rag.retriever import retriever
from app.models.llm import llm


def run(question: str):

    docs = retriever.invoke(question)

    print("\nRetrieved Chunks:\n")

    

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
    You are an API Documentation Assistant.

    Use ONLY the information provided in the context.

    For API-related questions:
    - Extract endpoints
    - Extract parameters
    - Extract request examples
    - Extract response examples
    - Extract authentication details

    Do not say information is missing if the answer exists in the context.

    Context:
    {context}

    Question:
    {question}
"""

    return llm.invoke(prompt).content