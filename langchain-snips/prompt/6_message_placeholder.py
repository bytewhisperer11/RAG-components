from langchain.prompts import MessagesPlaceholder

# Used in chat prompts to insert prior message history
placeholder = MessagesPlaceholder(variable_name="chat_history")

print(placeholder.variable_name)  # Outputs: chat_history
