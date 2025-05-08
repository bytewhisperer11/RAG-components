from langchain.callbacks import AsyncIteratorCallbackHandler
from langchain_google_genai import ChatGoogleGenerativeAI
import asyncio

# Custom Callback Handler to implement the required method
class CustomAsyncIteratorCallbackHandler(AsyncIteratorCallbackHandler):
    async def on_chat_model_start(self, model: str, messages: list):
        # You can add your custom logic here when the model starts
        print(f"Chat model {model} has started with messages: {messages}")

# Main function
async def main():
    handler = CustomAsyncIteratorCallbackHandler()  # Use the custom handler

    # Initialize the LLM with the model and the custom callback handler
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",  # Change the model version if needed
        temperature=0,
        callbacks=[handler]
    )

    # Create and run the task
    task = asyncio.create_task(llm.invoke("India"))

    # Asynchronously print the generated tokens
    async for token in handler.aiter():
        print(token, end="", flush=True)

    await task

# Entry point
if __name__ == "__main__":
    asyncio.run(main())
