from app.rag.retriever import retriever
from app.models.llm import llm


def run(question: str):

    docs = retriever.invoke(question)

    context = "\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
    You are a senior API developer.

    Focus on:
    - Endpoints
    - Parameters
    - Request Examples
    - Response Examples

    Context:
    {context}

    Question:
    {question}
    """

    return llm.invoke(prompt).content