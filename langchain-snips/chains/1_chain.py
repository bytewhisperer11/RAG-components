from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# Initialize the chat model
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

# Define a chat prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "Tell me a joke about {topic}."),
    ]
)

# Compose the chain by piping the prompt into the model
chain = prompt | llm

# Invoke the chain with input
result = chain.invoke({"topic": "bears"})

print(result.content)  # Outputs a joke about bears
