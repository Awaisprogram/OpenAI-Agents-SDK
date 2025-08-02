import asyncio
from pydantic import BaseModel
from agents import Agent, Runner

story_outline_agent = Agent(
    name="story_outline_agent",
    instructions="Generate a very 50 words story outline based on the user's input.",
)

class OutlineCheckerOutput(BaseModel):
    good_quality: bool

outline_checker_agent = Agent(
    name="outline_checker_agent",
    instructions="Read the given story outline shortly, and judge the quality",
    output_type=OutlineCheckerOutput,
)

story_agent = Agent(
    name="story_agent",
    instructions="Write a long story based on the given outline.",
    output_type=str,
)
