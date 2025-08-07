# custom_output_extraction.py

from agents import Agent, Runner, enable_verbose_stdout_logging, ToolCallOutputItem
from model import config, model
import re  


rupees_agent = Agent(
    name="rupees_agent",
    instructions="You are an agent that gives rupee-based financial info or values.",
    model=model,
)


async def check_output(output) -> ToolCallOutputItem:
    text = output.final_output
    print("raw agent output:", text)

    # Try to extract a number from the agent's response
    match = re.search(r"(\d+(?:,\d+)?(?:\.\d+)?)", text)
    print("match:", match)

    if match:
        amount = float(match.group(1).replace(",", ""))
        print("Amount extracted:", amount)

        if amount >= 100000:
            return f"{amount} PKR is a large amount. You should consider investing or saving."
        elif amount >= 10000:
            return f"{amount} PKR is a decent amount. Use it wisely!"
        else:
            return f"{amount} PKR is a small amount. Consider budgeting carefully."

    else:
        return "Could not extract any numeric value from the agent's output."


rupees_tool = rupees_agent.as_tool(
    tool_name="rupees_tool",
    tool_description="Provides financial guidance based on the amount in PKR.",
    custom_output_extractor=check_output,
)

agent = Agent(
    name="Main Agent",
    instructions="You are a helpful agent that uses rupee-based tools to provide advice.",
    tools=[rupees_tool],
)


def agent_as_tool(input):
    # enable_verbose_stdout_logging()
    result = Runner.run_sync(
        agent,
        input=input,
        run_config=config,
    )
    print("Final Output:", result.final_output)


def run_interactive():
    """Run the interactive loop within a single event loop"""
    while True:
        user_input = input("Ask anything about money: ")
        if user_input.lower() == "exit":
            break
        agent_as_tool(user_input)


run_interactive()
