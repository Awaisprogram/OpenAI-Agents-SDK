from agents import Agent, Runner, RunContextWrapper
from model import config

print("\n🎭 Example 1: Basic Dynamic Instructions")
print("-" * 40)
    
def basic_instructions(ctx:RunContextWrapper, agent: Agent) -> str:
        """Basic dynamic instructions."""
        return f"You are {agent.name}. Be helpful and informative!"
    
agent = Agent(
        name = "Basic agent",
        instructions = basic_instructions
)
    
result = Runner.run_sync(agent, "Whats agent name!", run_config=config)
print("Basic Agent:")
print(result.final_output)