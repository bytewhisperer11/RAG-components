from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate, MessagesPlaceholder
from langchain.schema import HumanMessage, AIMessage

# Chat-based prompt for dynamic project creation via conversation
chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("You are an AI software architect that creates custom project designs."),
    HumanMessagePromptTemplate.from_template("Build a project with:\nTitle: {project_title}\nGoal: {goal}"),
    AIMessagePromptTemplate.from_template("Please provide tech stack and required features."),
    MessagesPlaceholder(variable_name="chat_history"),
    HumanMessagePromptTemplate.from_template("Tech: {tech_stack}\nFeatures: {features}\nConstraints: {constraints}")
])

# Simulated conversation
chat_history = [
    HumanMessage(content="Build a project with: AI Legal Clause Extractor"),
    AIMessage(content="Please provide tech stack and required features.")
]

if __name__ == "__main__":
    messages = chat_prompt.format_prompt(
        project_title="AI Legal Clause Extractor",
        goal="Extract legal clause metadata from uploaded contracts.",
        tech_stack="Python, LangChain, Streamlit, SQLite",
        features="PDF upload, clause extraction, classification, export",
        constraints="Run locally, use OpenAI only",
        chat_history=chat_history
    ).to_messages()

    for msg in messages:
        print(f"{msg.type.upper()}: {msg.content}")
