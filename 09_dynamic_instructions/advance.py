from agents import Agent, Runner, RunContextWrapper
from model import config
 
 # 🎯 Example 2: Context-Aware Instructions
print("\n🎭 Example 2: Context-Aware Instructions")
print("-" * 40)

def context_aware(ctx:RunContextWrapper, agent:Agent) :
    """Context-aware instructions based on message count."""
    message_count = len(getattr(ctx, 'message', []))
    if message_count == 0:
        return "You are a welcoming assistant. Introduce yourself!"
    elif message_count < 3:
        return "You are a helpful assistant. Be concise."
    else:
        return "You are an experienced assistant. Be detailed." 
      
agent = Agent(
  name = "Context Aware Agent",
  instructions = context_aware
)          

result1 = Runner.run_sync(agent, "Hello!",run_config=config)
print("First message:")
print(result1.final_output)
    
result2 = Runner.run_sync(agent, "Tell me about Python", run_config=config)
print("\nSecond message:")
print(result2.final_output)