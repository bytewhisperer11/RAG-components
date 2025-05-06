import requests
from langchain.tools import Tool

def get_weather(city: str) -> str:
    # Placeholder logic - Weather API call would go here.
    return f"The current weather in {city} is 41°C and sunny."

weather_tool = Tool(
    name="Weather API",
    func=get_weather,
    description="Gets the current weather for a given city. Input should be a city name like 'Berlin'."
)

# Test run (optional)
if __name__ == "__main__":
    print(weather_tool.run("Jhansi"))