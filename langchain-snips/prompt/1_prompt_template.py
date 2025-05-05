from langchain.prompts import PromptTemplate


def get_project_spec_prompt() -> PromptTemplate:
    """
    Create and return a PromptTemplate for generating a complete project specification.
    """
    return PromptTemplate(
        input_variables=[
            "project_title",
            "goal",
            "tech_stack",
            "features",
            "constraints",
        ],
        template=(
            "You are a senior software architect.\n\n"
            "Design a complete project plan with the following parameters:\n\n"
            "Title: {project_title}\n"
            "Goal: {goal}\n"
            "Tech Stack: {tech_stack}\n"
            "Core Features: {features}\n"
            "Constraints: {constraints}\n\n"
            "Respond with:\n"
            "- Folder/file structure\n"
            "- Key components and responsibilities\n"
            "- Recommended libraries or frameworks\n"
            "- Optional enhancements\n"
            "- Technical risks or trade-offs"
        ),
    )


def generate_project_spec(**kwargs) -> str:
    """
    Format the project specification prompt using provided parameters.

    Expected keyword arguments:
        project_title (str)
        goal (str)
        tech_stack (str)
        features (str)
        constraints (str)

    Returns:
        str: Formatted project specification prompt.
    """
    prompt = get_project_spec_prompt()
    return prompt.format(**kwargs)


if __name__ == "__main__":
    prompt_output = generate_project_spec(
        project_title="AI Legal Clause Extractor",
        goal="Extract metadata from legal contracts using LLMs.",
        tech_stack="Python, LangChain, Streamlit, OpenAI, SQLite",
        features="PDF upload, clause segmentation, clause classification, export JSON",
        constraints="Client-only UI, no cloud storage, OpenAI only",
    )
    print(prompt_output)
