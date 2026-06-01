from app.rag.retriever import retriever
from app.models.llm import llm


def run(question: str):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
You are an API Support Engineer.

Rules:
- Use ONLY the provided context.
- Focus on:
  - Error Codes
  - Failure Reasons
  - Authentication Issues
  - Debugging Steps
  - Resolution Guidance
- Explain errors using the documentation.
- Do NOT invent new error codes.
- Do NOT use external knowledge.
- If information is missing, reply:
  "Information not found in the documentation."

Context:
{context}

Question:
{question}
"""

    return llm.invoke(prompt).content