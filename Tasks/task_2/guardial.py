from agents import Agent, Runner, RunContextWrapper, input_guardrail, GuardrailFunctionOutput
from model import config, model
import asyncio
from pydantic import BaseModel

class validation_result(BaseModel):
  is_safe: bool
  reason: str

guardial_agent = Agent(
  name = "Guardial Agent",
  instructions = "You are a guardrail agent that blocks dangerous inputs",
  model = model,
  output_type = validation_result
)
@input_guardrail
async def input_guard(ctx:RunContextWrapper , agent:Agent, input:str) -> GuardrailFunctionOutput:
  try:
    res = await Runner.run(guardial_agent, input, run_config = config)
    output = res.final_output
    return GuardrailFunctionOutput(
      output_info= output,
      tripwire_triggered= not output.is_safe
  )
  
  except Exception as e:
        return GuardrailFunctionOutput(
            output_info=validation_result(
                is_safe=True,
                reasoning=f"Error analyzing goal: {str(e)}"
            ),
            tripwire_triggered=False  
        )