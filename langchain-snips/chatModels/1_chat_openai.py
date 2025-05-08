import getpass
import os

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain.chat_models import init_chat_model
from langchain.schema import HumanMessage, SystemMessage

llm = init_chat_model(
    "gpt-4",
    model_provider="openai",
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
