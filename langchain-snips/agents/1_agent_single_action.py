from langchain.agents import LLMSingleActionAgent, AgentExecutor, Tool
from langchain.prompts import PromptTemplate
from langchain.schema import AgentAction, AgentFinish
from langchain.agents.agent import AgentOutputParser
from langchain.llms import OpenAI
from typing import Union
import re

# Tool implementation
def search_tool(input_text: str) -> str:
    return f"[SearchTool] Simulated search result for: {input_text}"

tools = [
    Tool(
        name="Search",
        func=search_tool,
        description="Useful for answering general knowledge queries."
    )
]

# Prompt template for the agent
prompt = PromptTemplate(
    input_variables=["input", "agent_scratchpad"],
    template="""You are a helpful agent that uses tools to solve problems.
Question: {input}
{agent_scratchpad}"""
)

# Output parser to handle LLM responses
class ReActOutputParser(AgentOutputParser):
    def parse(self, llm_output: str) -> Union[AgentAction, AgentFinish]:
        if "Final Answer:" in llm_output:
            return AgentFinish(
                return_values={"output": llm_output.split("Final Answer:")[-1].strip()},
                log=llm_output
            )
        match = re.search(r"Action: (.*)\nAction Input: (.*)", llm_output)
        if not match:
            raise ValueError(f"Could not parse LLM output: {llm_output}")
        return AgentAction(
            tool=match.group(1).strip(),
            tool_input=match.group(2).strip(),
            log=llm_output
        )

# LLM and Agent setup
llm = OpenAI(temperature=0)
agent = LLMSingleActionAgent(
    llm_chain=prompt | llm,
    output_parser=ReActOutputParser(),
    stop=["\nObservation:"],
    allowed_tools=["Search"]
)

# Agent executor for running the loop
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Run example
if __name__ == "__main__":
    question = "What is the capital of Germany?"
    result = agent_executor.run(question)
    print("Agent Response:", result)
