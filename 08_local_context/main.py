import asyncio
from dataclasses import dataclass
from agents import Agent, Runner, function_tool, RunContextWrapper
from model import config


@dataclass
class UserContext:
    username: str
    email: str | None = None
    location : str | None = None

@function_tool()
async def search() -> str:
    return [{"name": "Ali" , "profession" : "Math Tutor", "location" : "Karachi"},
            {"name": "Zaid" , "profession" : "Math Tutor", "location" : "Islamabad"}]



async def special_prompt(Wrapper: RunContextWrapper[UserContext], agent: Agent[UserContext]) -> str:
    # who is user?
    # which agent
    print(f"\nUser: {Wrapper.context},\n Agent: {agent.name}\n")
    return f"You are a math expert. User: {Wrapper.context.username}, Agent: {agent.name}. Please assist with math-related queries.User location is {Wrapper.context.location}"

math_agent = Agent(
    name="Genius", 
    instructions=special_prompt,  
    tools=[search]
)

async def call_agent():
    # Call the agent with a specific input
    user_context = UserContext(username="abdullah", location="Islamabad")

    output = await Runner.run(
        starting_agent=math_agent, 
        input="search for the best math tutor ",
        run_config= config,
        context=user_context
        )
    print(f"\n\nOutput: {output.final_output}\n\n")
    
asyncio.run(call_agent())