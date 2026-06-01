from app.agents.definition_agent import run as definition_agent
from app.agents.code_agent import run as code_agent
from app.agents.troubleshooting_agent import run as troubleshooting_agent

from app.agents.supervisor_agent import route


while True:

    question = input("\nAsk Question: ")

    if question.lower() == "exit":
        break

    selected_agent = route(question)

    print(f"\nSelected Agent: {selected_agent}")

    if selected_agent == "definition_agent":

        answer = definition_agent(question)

    elif selected_agent == "code_agent":

        answer = code_agent(question)

    elif selected_agent == "troubleshooting_agent":

        answer = troubleshooting_agent(question)

    else:

        answer = "Unable to determine appropriate agent."

    print("\nAnswer:\n")
    print(answer)