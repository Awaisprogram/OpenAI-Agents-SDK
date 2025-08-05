from agents import Agent , Runner , enable_verbose_stdout_logging
from model import config, provider, model
import asyncio

async def agent_as_tool():
    enable_verbose_stdout_logging()

    rupees_agent = Agent(
        name = "Rupees Convertor",
        instructions= "You are a agent that convert currency to pakistani rupees",
        model=model
    )

    usd_agent = Agent(
        name = "USD Convertor",
        instructions= "You are a agent that convert currency to USD",
        model=model
    )

    agent = Agent(
        name = "Main Agent",
        instructions="You are a helpful currency assistant. If the user asks to convert something to rupees, use the Rupees Convertor tool. If they ask for USD, use the USD Convertor tool."
,
   tools=[
        rupees_agent.as_tool(
                tool_name= "rupees_convertor",
                tool_description= "You are a agent that convert currency to pakistani rupees"
        ),
            usd_agent.as_tool(
                tool_name= "usd_convertor",
                tool_description= "You are a agent that convert currency to USD"
            )
    ],
        
    )


    while True:
        user_input = input("User: ")
        if user_input == "exit":
            break
        response = await Runner.run(
            agent,
            user_input,
            run_config= config
        )
        print(response.final_output)
    
if __name__ == "__main__":
    asyncio.run(agent_as_tool())