from agents import Agent, Runner,function_tool, AgentHooks, RunContextWrapper
from model import config


# Agent Lifecycle Callbacks/Hooks
# class HelloAgentHooks(AgentHooks):
#     def __init__(self, lifecycle_name: str):
#         self.lifecycle_name = lifecycle_name
        
#     async def on_start(self, context, agent):
#         context.context
#         print(f"\n\n[{self.lifecycle_name}] Agent {agent.name} starting with context: {context}\n\n")
        
#     async def on_llm_start(self, context: RunContextWrapper, agent, system_prompt, input_items):
#         print(f"\n\n[{self.lifecycle_name}] LLM call starting with system prompt: {system_prompt} and input items: {input_items}\n\n")
        
#     async def on_llm_end(self, context, agent, response):
#         print(f"\n\n[{self.lifecycle_name}] LLM call ended with response: {response}\n\n")
        
#     async def on_end(self, context, agent, output):
#         print(f"\n\n[{self.lifecycle_name}] Agent {agent.name} ended with output: {output}\n\n")

class HelloAgentHooks(AgentHooks):
  def __init__(self,  lifecycle_name: str):
    self.lifecycle_name = lifecycle_name
    
  async def on_start(self,context:RunContextWrapper,agent):
    context.context = context
    print(f"\n\n[{self.lifecycle_name}] Agent {agent.name} starting with context: {context}\n\n")
  
  async def on_llm_start(self, context, agent, system_prompt, input_items):
    print(f"\n\n[{self.lifecycle_name}] Agent {agent.name} starting with system prompt: {system_prompt} and input items: {input_items}\n\n")
  
  
  async def on_llm_end(self, context, agent, response):
    print(f"\n\n[{self.lifecycle_name}] Agent {agent.name} give reponse: {response}\n\n")
    
  async def on_end(self, context, agent, output):
    print(f"\n\n[{self.lifecycle_name}] Agent {agent.name} ended with output: {output}\n\n")
    
@function_tool
def get_weather(city: str) -> str:
    """A simple function to get the weather for a user."""
    return f"The weather for {city} is sunny."



news_agent: Agent = Agent(
    name="NewsAgent",
    instructions="You are a helpful news assistant.",
    hooks=HelloAgentHooks("NewsAgentLifecycle")
)


base_agent: Agent = Agent(
    name="WeatherAgent",
    instructions="You are a helpful assistant. Talk about weather and let news_agent handle the news things",
    tools=[get_weather],
    hooks=HelloAgentHooks("WeatherAgentLifecycle"),
    handoffs=[news_agent]
)

res = Runner.run_sync(base_agent, "PM of Pakistan", run_config=config)
print(res.last_agent.name)
print(res.final_output)

# Now check the trace in 