from agents import Agent, Runner, function_tool, ModelSettings
from model import config


@function_tool

def calculate_area(length, width):
   """Calculate the area of a rectangle."""
   area = length * width
   return f"Area = {length} × {width} = {area} square units"

def tool_choice_testing():
    auto_agent = Agent(
        name= "Auto Agent",
        instructions= "You are a helpful assistant",
        tools=[calculate_area],
        model_settings= ModelSettings(
            tool_choice= "auto"
        )
    )
    required_agent = Agent(
        name= "Required Agent",
        instructions= "You are a helpful assistant",
        tools=[calculate_area],
        model_settings= ModelSettings(
            tool_choice= "required"
        )
    )
    none_agent = Agent(
        name= "Required Agent",
        instructions= "You are a helpful assistant",
        tools=[calculate_area],
        model_settings= ModelSettings(
            tool_choice= "none"
        )
    )
    question = "What's the area of a 5x3 rectangle?"
    print("-"*50)
    print("\nTool Choice Testing\n")
    print("-"*50)
    
    # Auto Agent Response
    
    response = Runner.run_sync(
        auto_agent,
        question,
        run_config= config
    )
    print("Auto Agent response: ")
    print("-"*50)
    
    print(response.final_output)
    
    # Required Agent Response
    
    response = Runner.run_sync(
        required_agent,
        question,
        run_config= config
    )
    print("Required Agent response: ")
    print("-"*50)
    
    print(response.final_output)
    
    # None Agent Response
    
    response = Runner.run_sync(
        none_agent,
        question,
        run_config= config
    )
    print("None Agent response: ")
    print("-"*50)
    
    print(response.final_output)
if __name__ == "__main__":
    tool_choice_testing()
