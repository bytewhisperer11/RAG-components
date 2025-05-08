from langchain_anthropic import ChatAnthropic
from langchain.schema import HumanMessage, SystemMessage  # updated import

llm = ChatAnthropic(
    model="claude-3-opus-20240229",
    temperature=0.7,
    top_k=250,
    top_p=1.0,
    max_tokens=1024,
    stop_sequences=["\n\nHuman:"],
    streaming=False,
    metadata={"user_id": "dev-avatar"},
    timeout=60
)

response = llm.invoke([
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="How do you implement semantic search?")
])
print(response.content)
