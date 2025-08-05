from agents import AsyncOpenAI , OpenAIChatCompletionsModel ,RunConfig
import os
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
  api_key = gemini_api_key,
  base_url= "https://generativelanguage.googleapis.com/v1beta/openai/",
) 

model = OpenAIChatCompletionsModel(
  model = "gemini-2.0-flash",
  openai_client = provider
)

config = RunConfig(
  model = model,
  tracing_disabled= True,
  model_provider= provider
)