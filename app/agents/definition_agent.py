from app.rag.retriever import retriever
from app.models.llm import llm


def run(question: str):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
You are an API Documentation Expert.

Rules:
- Use ONLY the provided context.
- Explain concepts, overview, purpose, and use cases.
- Do NOT generate code examples.
- Do NOT invent information.
- If information is missing, reply:
  "Information not found in the documentation."

Context:
{context}

Question:
{question}
"""

    return llm.invoke(prompt).content