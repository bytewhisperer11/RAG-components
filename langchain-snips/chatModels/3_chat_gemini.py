from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
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
