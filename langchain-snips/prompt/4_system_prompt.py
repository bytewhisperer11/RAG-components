from langchain.prompts import SystemMessagePromptTemplate

# Set LLM role and instruction
system_prompt = SystemMessagePromptTemplate.from_template(
    "You are an expert software architect creating full-stack project designs."
)

msg = system_prompt.format()

print(f"{msg.type.upper()}: {msg.content}")
