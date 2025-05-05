from langchain.prompts import AIMessagePromptTemplate

# Simulate LLM structured response template
ai_prompt = AIMessagePromptTemplate.from_template(
    "Understood. Please share your preferred tech stack and constraints."
)

msg = ai_prompt.format()

print(f"{msg.type.upper()}: {msg.content}")
