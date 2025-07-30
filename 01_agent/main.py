from agents import Agent , OpenAIChatCompletionsModel , AsyncOpenAI , Runner, RunConfig
from dotenv import load_dotenv
import os



def main():
  load_dotenv()
  
  gemini_api_key = os.getenv("GEMINI_API_KEY")
  
  
  provider = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
  )
  
  model = OpenAIChatCompletionsModel(
    openai_client= provider,
    model = "gemini-2.0-flash",
  )
  
  config = RunConfig(
    model = model,
    tracing_disabled= True,
    model_provider= provider
 )
  
  agent = Agent(
    name = "Agent",
    instructions="You are a helpful assistant.",
  )  
  
  user_input = input("User: ")
  
  response = Runner.run_sync(
    agent,
    user_input,
    run_config = config,
    
  )
  result = response.final_output
  
  
  print("result: " , result)
  
  
if __name__ == "__main__":
  main()