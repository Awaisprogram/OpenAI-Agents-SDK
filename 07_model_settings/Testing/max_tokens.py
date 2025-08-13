from agents import Agent, Runner, function_tool, ModelSettings
from model import config


def max_token_testing():
    low_agent = Agent(
        name= "Cold Agent",
        instructions= "You are a helpful assistant",
        model_settings= ModelSettings(
            max_tokens= 10
        )
    )
    high_agent = Agent(
        name= "Cold Agent",
        instructions= "You are a helpful assistant",
        model_settings= ModelSettings(
            max_tokens= 90
        )
    )
    question = "Tell me about AI in 2 sentences"
    print("-"*50)
    print("\nMax Token Testing\n")
    print("-"*50)
    
    # low Agent Response
    
    response = Runner.run_sync(
        low_agent,
        question,
        run_config= config
    )
    print("Low Agent response: ")
    print("-"*50)
    
    print(response.final_output)
    
    # High Agent Response
    
    response = Runner.run_sync(
        high_agent,
        question,
        run_config= config
    )
    print("High Agent response: ")
    print("-"*50)
    
    print(response.final_output)
if __name__ == "__main__":
    max_token_testing()
