from agents import Agent , SQLiteSession
from model import config
from streaming import stream_response
import asyncio
from tools.greeting import Greetings


async def main():
    
    session = SQLiteSession("conversation123")
    
    agent = Agent(
        name = "Agent with tool",
        instructions = "You are a Greeting agent.",
        tools = [
            Greetings
        ]
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
    asyncio.run(main())    

