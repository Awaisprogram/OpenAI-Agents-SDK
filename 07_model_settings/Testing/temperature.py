from agents import Agent, Runner, function_tool, ModelSettings
from model import config


def temperature_testing():
    cold_agent = Agent(
        name= "Cold Agent",
        instructions= "You are a helpful assistant",
        model_settings= ModelSettings(
            temperature= 0.5
        )
    )
    hot_agent = Agent(
        name= "Cold Agent",
        instructions= "You are a helpful assistant",
        model_settings= ModelSettings(
            temperature= 1.5
        )
    )
    question = "Tell me about AI in 2 sentences"
    print("-"*50)
    print("\nTemperature Testing\n")
    print("-"*50)
    
    # Cold Agent Response
    
    response = Runner.run_sync(
        cold_agent,
        question,
        run_config= config
    )
    print("Cold Agent response: ")
    print("-"*50)
    
    print(response.final_output)
    
    # Hot Agent Response
    
    response = Runner.run_sync(
        hot_agent,
        question,
        run_config= config
    )
    print("Hot Agent response: ")
    print("-"*50)
    
    print(response.final_output)
if __name__ == "__main__":
    temperature_testing()
