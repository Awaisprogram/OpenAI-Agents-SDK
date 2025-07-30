from agents import Runner
from openai.types.responses import ResponseTextDeltaEvent

async def streamed_response(agent , user_input, run_config ,sessions): 
  
  result = Runner.run_streamed(
    agent,
    user_input,
    run_config = run_config,
    session = sessions
  )
  
  async for event in result.stream_events():
    if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
      print(event.data.delta, end="", flush=True)