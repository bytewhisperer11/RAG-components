from langchain_together import ChatTogether
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatTogether(
    model="mistralai/Mistral-7B-Instruct-v0.1",
    temperature=0.7,
    top_p=0.9,
    top_k=50,
    max_tokens=1024,
    repetition_penalty=1.1,
    stop=["<|endoftext|>"],
    streaming=False,
    timeout=60
)

response = llm.invoke([
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Compare PostgreSQL with MongoDB.")
])
print(response.content)
