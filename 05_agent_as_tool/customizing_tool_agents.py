# for testing purpose -> to customize agent.as_tool we use agent and runner inside a function tool decorator and set max_turns in the Runner.


from agents import Agent, Runner, enable_verbose_stdout_logging, function_tool
from model import config
import asyncio


@function_tool
async def run_my_math_agent() -> str:
    """A tool that runs the math agent"""

    agent = Agent(name="MathAgent", instructions="Math Agent")

    result = await Runner.run(
        agent, input="what is 2+2", max_turns=1, run_config=config
    )

    return str(result.final_output)


async def customizing_tool_agents():
    enable_verbose_stdout_logging()
    agent = Agent("testing_agent", instructions="testing agent", tools=[run_my_math_agent])
    result = await Runner.run(agent, input="run math tool", run_config=config)
    print(result.final_output)


asyncio.run(customizing_tool_agents())