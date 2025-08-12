import asyncio
from pydantic import BaseModel
from model import config
from agents import Agent,  Runner,  handoff, enable_verbose_stdout_logging , SQLiteSession


class UserContext(BaseModel):
    user_id: str
    subscription_tier: str = "free"  # free, premium, enterprise
    has_permission: bool = False


# This agent will use the custom LLM provider
agent = Agent(
    name="Assistant",
    instructions="You only respond for the user's request and delegate to the expert agent if needed.",
   
)

expert_agent = Agent(
    name="Expert",
    instructions="You are an expert in the field of recursion in programming.",
)


agent.handoffs = [handoff(expert_agent, is_enabled=lambda ctx, agent: ctx.context.has_permission)]



async def main():
    
    session = SQLiteSession("conversation123")
    
    # enable_verbose_stdout_logging()
    context = UserContext(user_id="123", subscription_tier="premium", has_permission=True)
    
    if context.has_permission == True:
      print("You have permission to use the agent.")
    else:
      print("\nYou do not have permission to use the agent.\n")  
      
      
    while True: 
      user_input = input("User: ")
      if user_input.lower() == "exit":
        break
      result = await Runner.run(
          agent,
          user_input,
          run_config=config,
          context=context,
          session = session
      )
      print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
    