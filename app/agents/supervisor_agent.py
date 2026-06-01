from app.models.llm import llm


def route(question: str):

    prompt = f"""
You are a supervisor agent.

Available Agents:

1. definition_agent
   - concepts
   - overview
   - definitions
   - use cases

2. code_agent
   - endpoints
   - request examples
   - response examples
   - authentication
   - parameters

3. troubleshooting_agent
   - errors
   - status codes
   - debugging
   - failures
   - unauthorized issues

Return ONLY one of:

definition_agent
code_agent
troubleshooting_agent

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content.strip().lower()