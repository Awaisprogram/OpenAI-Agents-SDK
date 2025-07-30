from model import config
from agents import Agent , SQLiteSession, Runner

sessions = SQLiteSession("conversation-123")

agent = Agent(
  name = "Multi-turn Agent",
  instructions = "You are a helpful assistant",
)

while True:
  user_input = input("User: ")

  response = Runner.run_sync(
    agent,
    user_input,
    run_config = config,
    session = sessions
  )

  result = response.final_output

  print("=" * 50)
  print("\n", result)
  print("=" * 50)
  
  if user_input == "exit":
    break
