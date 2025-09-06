from agents import Agent, Runner,function_tool, RunHooks, RunContextWrapper,trace
from model import config


# Agent Lifecycle Callbacks/Hooks
class HelloRunHooks(RunHooks):
        
    async def on_agent_start(self, context: RunContextWrapper, agent: Agent):
        print(f"\n\n[RunLifecycle] Agent {agent.name} start with context: {context}\n\n")
        
    async def on_llm_start(self, context: RunContextWrapper, agent: Agent, system_prompt, input_items):
        print(f"\n\n[RunLifecycle] LLM call for agent {agent.name} starting with system prompt: {system_prompt} and input items: {input_items}\n\n")
    
    async def on_llm_end(self, context, agent, response):
      print(f"\n\n[RunLifecycle] LLM call for agent {agent.name} gave response: {response}\n\n")
        
    
@function_tool
def get_weather(city: str) -> str:
    """A simple function to get the weather for a user."""
    return f"The weather for {city} is sunny."

news_agent: Agent = Agent(
    name="NewsAgent",
    instructions="You are a helpful news assistant.",
)


base_agent: Agent = Agent(
    name="WeatherAgent",
    instructions="You are a helpful assistant. Talk about weather and let news_agent handle the news things",
    tools=[get_weather],
    handoffs=[news_agent]
)
with trace("run_lifecycle"):
  res = Runner.run_sync(
      starting_agent=base_agent, 
      input="What's the latest news about Qwen Code - seems like it can give though time to claude code.",
      run_config=config,
      hooks=HelloRunHooks()
      )

  print(res.last_agent.name)
  print(res.final_output)
