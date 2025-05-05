from langchain.prompts import MessagesPlaceholder
from langchain.schema import HumanMessage, AIMessage

chat_history = str([
    HumanMessage(content="Build a project with: AI Legal Clause Extractor"),
    AIMessage(content="Please provide tech stack and required features.")])

# Used in chat prompts to insert prior message history
placeholder = MessagesPlaceholder(variable_name=chat_history)

print(placeholder.variable_name)  # Outputs: chat_history
