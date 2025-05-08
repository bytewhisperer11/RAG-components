from langchain.chat_models import init_chat_model
from langchain.schema import HumanMessage, SystemMessage

llm = init_chat_model(
    "gemini-pro",
    model_provider="google_genai",
    temperature=0.7,
    top_p=1.0,
    top_k=40,
    max_output_tokens=1024,
    stop_sequences=["\nUser:"],
    convert_system_message_to_human=True
)

response = llm.invoke([
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Give an overview of the LangChain v0.3 architecture.")
])
print(response.content)
