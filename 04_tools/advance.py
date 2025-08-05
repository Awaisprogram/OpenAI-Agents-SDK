from agents import Agent , SQLiteSession , ModelSettings, enable_verbose_stdout_logging
from model import config
from streaming import stream_response
import asyncio
from tools.greeting import Greetings


async def advance():
    enable_verbose_stdout_logging()
    session = SQLiteSession("conversation123")
    
    agent = Agent(
        name = "Agent with tool",
        instructions = "You are a Greeting agent, When user greet you must greet them by taking name",
        tools = [
            Greetings
        ],
        model_settings= ModelSettings(
            max_tokens = 100,
            temperature = 0.9
        )
    )
    while True:
        user_input = input("Enter your question: ")
        

        await stream_response(
            agent ,
            user_input = user_input, 
            run_config= config,
            session = session
        )
        
        if user_input == "exit":
            break

if __name__ == "__main__":
    asyncio.run(advance())    

