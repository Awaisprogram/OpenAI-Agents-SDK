from openai.types.responses import ResponseTextDeltaEvent
from agents import Runner

async def stream_response(agent, user_input , run_config, session):
  response = Runner.run_streamed(
    agent,
    user_input,
    run_config= run_config,
    session = session
)

  async for event in response.stream_events():
    if event.type == "raw_response_event" and isinstance(event.data , ResponseTextDeltaEvent):
      print(event.data.delta , end = "" , flush = True)  