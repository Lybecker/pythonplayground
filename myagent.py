import asyncio
from random import randint
from typing import Annotated
from pydantic import Field
from agent_framework.azure import AzureAIAgentClient
from azure.identity.aio import AzureCliCredential
from dotenv import load_dotenv

load_dotenv()

async def main():
    async with AzureAIAgentClient(credential=AzureCliCredential()).create_agent(
        instructions="You are good at telling jokes.",
        name="Joker",
        tools=get_weather) as agent:
            result = await agent.run("Tell me a joke about about the current weather in New York City include the current temperature.")
            print(result.text)


def get_weather(
    location: Annotated[str, Field(description="The location to get the weather for.")],
) -> str:
    """Get the weather for a given location."""
    conditions = ["sunny", "cloudy", "rainy", "stormy"]
    return f"The weather in {location} is {conditions[randint(0, 3)]} with a high of {randint(10, 30)}°C."

asyncio.run(main())