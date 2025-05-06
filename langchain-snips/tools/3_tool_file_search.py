import os
from langchain.tools import Tool

def search_files(keyword: str, search_dir="docs/") -> str:
    matches = []
    for root, _, files in os.walk(search_dir):
        for file in files:
            if file.endswith(".txt"):
                with open(os.path.join(root, file), "r") as f:
                    contents = f.read()
                    if keyword in contents:
                        matches.append(os.path.join(root, file))
    return "\n".join(matches) if matches else "No matches found."

file_search_tool = Tool(
    name="File Search Tool",
    func=search_files,
    description="Searches for a keyword inside .txt files within the /docs directory."
)

# Test run (optional)
if __name__ == "__main__":
    print(file_search_tool.run("LangChain"))
