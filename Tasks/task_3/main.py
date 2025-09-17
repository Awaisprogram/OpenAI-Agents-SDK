"""
1. Accepts a city name from the user.

2. Uses a tool function to fetch mock weather data (no real API calls needed).

3. Responds in a friendly message showing:

- City name

- Current temperature

- Weather condition (e.g., Sunny, Rainy, Cloudy)

4. Includes a guardrail to reject suspicious input (e.g., "import os", "delete system32").

5. Uses RunHooks to log both input and output."""




from agents import Agent, Runner, RunContextWrapper, function_tool, InputGuardrailTripwireTriggered, AgentHooks
from model import config
import asyncio
from guardial import input_guard

class Hooks(AgentHooks):
    # 4. Adds a RunHook to log every input/output pair
    
    async def on_start(self, ctx:RunContextWrapper, agent:Agent):
        print(f"Agent: {agent.name}")
    
    async def on_end(self, ctx:RunContextWrapper, agent:Agent, output:str):
        print(f"[LOG] Agent: {agent.name}, Output: {output}")




# 2 Uses a tool call to safely evaluate the expression
@function_tool
def Weather_tool(city:str):
    """ """
    
    weather_data = {
    "karachi": {"temp": 32, "condition": "Sunny"},
    "lahore": {"temp": 29, "condition": "Cloudy"},
    "islamabad": {"temp": 26, "condition": "Rainy"},
}

    city_lower = city.strip().lower()
    if city_lower in weather_data:
        data = weather_data[city_lower]
        return f"Weather in {city.capitalize()}: {data['temp']}°C, {data['condition']}"
    else:
        return f"Sorry, I don’t have data for {city.capitalize()}."



async def main():
  def dynamic_instruction(ctx:RunContextWrapper, agent: Agent): #important parameters
    return f"You are {agent.name}, You tell the weather, by asking ther user's city by runnning tool"
  
  agent = Agent(
    name = "Weather Agent",
    instructions = dynamic_instruction,
    tools = [Weather_tool],
    input_guardrails = [input_guard],
    hooks = Hooks()
    
  )
  

  while True:
    # 1. Accepts math questions from the user 
    user_question = input("Enter city name: ")
    
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