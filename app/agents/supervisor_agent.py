from app.models.llm import llm


def route(question: str):

    prompt = f"""
    You are a supervisor agent.

    Available agents:

    1. definition_agent
       - definitions
       - concepts
       - overview
       - explanations

    2. code_agent
       - endpoints
       - parameters
       - requests
       - responses
       - code examples

    3. troubleshooting_agent
       - errors
       - failures
       - debugging
       - status codes

    Return ONLY one agent name.

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    return response.content.strip()