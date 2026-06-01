from app.rag.retriever import retriever
from app.models.llm import llm


def run(question: str):

    docs = retriever.invoke(question)

    context = "\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
    You are an API troubleshooting expert.

    Focus on:
    - Errors
    - Failure Causes
    - Debugging Steps
    - Fixes

    Context:
    {context}

    Question:
    {question}
    """

    return llm.invoke(prompt).content