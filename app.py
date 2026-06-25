from langgraph.graph import StateGraph
from typing import TypedDict

from agents.account_assistant import account_agent
from agents.compliance_checker import compliance_agent
from agents.customer_support import customer_support_agent


class AgentState(TypedDict):
    query: str
    response: str


def router(state):
    query = state["query"].lower()

    if "balance" in query:
        return {"response": account_agent("123456")}

    elif "kyc" in query:
        return {"response": compliance_agent("CUST001")}

    else:
        return {"response": customer_support_agent(query)}


graph = StateGraph(AgentState)

graph.add_node("router", router)

graph.set_entry_point("router")
graph.set_finish_point("router")

app = graph.compile()


if __name__ == "__main__":
    result = app.invoke(
        {
            "query": "Check balance"
        }
    )

    print(result["response"])
