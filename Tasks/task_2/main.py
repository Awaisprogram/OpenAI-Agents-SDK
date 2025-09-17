"""
1. Accepts math questions from the user (e.g., 5 + 3 * 2).

2. Uses a tool call to safely evaluate the expression (avoid direct eval, use a safe library like sympy or ast.literal_eval).

3. Implements a guardrail to block dangerous inputs (e.g., import os, __builtins__, system() calls).

4. Adds a RunHook to log every input/output pair."""

from agents import Agent, Runner, RunContextWrapper, function_tool, InputGuardrailTripwireTriggered, AgentHooks
from model import config
import asyncio
from sympy import sympify
from guardial import input_guard

class Hooks(AgentHooks):
    # 4. Adds a RunHook to log every input/output pair
    
    async def on_start(self, ctx:RunContextWrapper, agent:Agent):
        print(f"Agent: {agent.name}")
    
    async def on_end(self, ctx:RunContextWrapper, agent:Agent, output:str):
        print(f"[LOG] Agent: {agent.name}, Output: {output}")




# 2 Uses a tool call to safely evaluate the expression
@function_tool
def math_tool(input: str):
    output = sympify(input)
    return output



async def main():
  def dynamic_instruction(ctx:RunContextWrapper, agent: Agent): #important parameters
    return f"You are {agent.name}, You solve user questions by runnning tool"
  
  agent = Agent(
    name = "Math Agent",
    instructions = dynamic_instruction,
    tools = [math_tool],
    input_guardrails = [input_guard],
    hooks = Hooks()
    
  )
  

  while True:
    # 1. Accepts math questions from the user 
    user_question = input("Enter your question: ")
    
    if user_question.lower() == "exit":
      break
    try:
        result = await Runner.run(
            agent ,
            user_question,
            run_config = config
        )

        print(result.final_output)
    
    except InputGuardrailTripwireTriggered as e:
        print("Alert: Guardrail input tripwire was triggered!")    
    
if __name__ == "__main__":
  asyncio.run(main())    
