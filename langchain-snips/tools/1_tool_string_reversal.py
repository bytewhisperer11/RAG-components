from langchain.tools import Tool

def reverse_string(text: str) -> str:
    """
    Reverses the given string.
    
    :param text: The string to reverse.
    :return: The reversed string.
    """
    return text[::-1]

# Define the String Reversal tool
string_reversal_tool = Tool(
    name="String Reversal",
    func=reverse_string,
    description="Reverses the given string. Input should be a string of text."
)

# Test run (optional)
if __name__ == "__main__":
    print(string_reversal_tool.run("LangChain"))  # Expected output: "niahCgnaL"