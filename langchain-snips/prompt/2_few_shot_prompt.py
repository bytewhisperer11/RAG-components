from langchain.prompts import PromptTemplate, FewShotPromptTemplate

# Template to format each few-shot example
example_prompt = PromptTemplate(
    input_variables=["project_title", "output"],
    template="PROJECT: {project_title}\nSOLUTION:\n{output}"
)

# Few-shot template for generating similar new project plans
few_shot = FewShotPromptTemplate(
    examples=[
        {
            "project_title": "Real-time Crypto Tracker",
            "output": "Stack: Python, FastAPI, WebSockets\nFeatures: live feed, alert rules..."
        },
        {
            "project_title": "Fitness App with AI Coach",
            "output": "Stack: React Native, TensorFlow Lite\nFeatures: posture detection..."
        }
    ],
    example_prompt=example_prompt,
    suffix="PROJECT: {project_title}",
    input_variables=["project_title"]
)

if __name__ == "__main__":
    print(few_shot.format(project_title="AI Legal Clause Extractor"))
