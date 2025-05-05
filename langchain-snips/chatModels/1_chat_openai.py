from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.7,
    top_p=1.0,
    max_tokens=1024,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    n=1,
    stop=None,
    streaming=False,
    timeout=60,
    model_kwargs={"logit_bias": {}, "user": "dev-avatar"}
)

response = llm.invoke([
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Explain RAG in AI.")
])
print(response.content)
