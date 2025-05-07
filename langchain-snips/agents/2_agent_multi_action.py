from langchain.agents import AgentExecutor, Tool
from langchain.agents.agent import BaseMultiActionAgent
from langchain.schema import AgentAction, AgentFinish
from typing import List, Union


# Define multiple tools
def math_tool(input_text: str) -> str:
    return f"[MathTool] Computed result for: {input_text}"

def translate_tool(input_text: str) -> str:
    return f"[TranslateTool] Translated to French: {input_text}"

tools = [
    Tool(name="Math", func=math_tool, description="Performs basic math operations."),
    Tool(name="Translate", func=translate_tool, description="Translates text into French."),
]

# Custom multi-action agent implementation
class CustomMultiActionAgent(BaseMultiActionAgent):
    def plan(self, intermediate_steps: List, **kwargs) -> Union[List[AgentAction], AgentFinish]:
        user_input = kwargs["input"]

        # Decide to invoke both tools simultaneously
        actions = [
            AgentAction(tool="Math", tool_input=user_input, log=""),
            AgentAction(tool="Translate", tool_input=user_input, log="")
        ]
        return actions

    async def aplan(self, intermediate_steps: List, **kwargs) -> Union[List[AgentAction], AgentFinish]:
        return self.plan(intermediate_steps, **kwargs)

    def return_stopped_response(self, intermediate_steps: List, **kwargs) -> AgentFinish:
        return AgentFinish(return_values={"output": "Stopped execution."}, log="Stopped.")

# Instantiate executor
agent = CustomMultiActionAgent()
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Example usage
if __name__ == "__main__":
    question = "Translate 'hello' and calculate 3 * 4"
    result = agent_executor.run(question)
    print("Agent Response:", result)
