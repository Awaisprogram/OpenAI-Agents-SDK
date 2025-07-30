from agents import Agent,Runner,SQLiteSession 
from model import config
import asyncio
from openai.types.responses import ResponseTextDeltaEvent
from streaming import streamed_response

async def main():
    
   sessions = SQLiteSession("conversation123") 
   agent = Agent(
       name = "Streaming agent",
       instructions= "You are a helpful agent"
   )
   while True:
       user_input = input("User: ")
       
       if user_input == "exit":
           print("Goodbye")
           break
       
       await streamed_response(
           agent,
           user_input = user_input,
           run_config = config,
           sessions = sessions
        )
       
       
       
       

if __name__ == "__main__":
   asyncio.run(main())
