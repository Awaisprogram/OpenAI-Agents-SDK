from agents import Agent ,Runner , input_guardrail , output_guardrail , GuardrailFunctionOutput , RunContextWrapper , InputGuardrailTripwireTriggered , OutputGuardrailTripwireTriggered
from pydantic import BaseModel
from model import config

class MathRelated(BaseModel):
  is_math_homework: bool
  reasoning: str


checker_maths = Agent(
  name = "Math agent",
  instructions= "Check weather the query is math related",
  output_type= MathRelated
)

@input_guardrail
async def math_input_checker(ctx:RunContextWrapper, agent: Agent, input)-> GuardrailFunctionOutput:
  response = await Runner.run(checker_maths, input , run_config=config)
  return GuardrailFunctionOutput(
    output_info = response.final_output,
    tripwire_triggered = response.final_output.is_math_homework is False
  )
# @input_guardrail
# async def weather_input_checker(
#     ctx: RunContextWrapper, agent: Agent, input
# ) -> GuardrailFunctionOutput:
#     result = await Runner.run(weather_sanitizer, input,  run_config = config)
#     print("output: ", result.final_output)
#     return GuardrailFunctionOutput(
#         output_info=result.final_output,
#         # tripwire_triggered=False #result.final_output.is_math_homework,
#         tripwire_triggered=result.final_output.is_weather is False,
#     )  
  
  
 
@output_guardrail
def math_output_checker(ctx:RunContextWrapper, agent: Agent, output)-> GuardrailFunctionOutput:
  return GuardrailFunctionOutput(
    output_info = "passed",
    tripwire_triggered = False
  )

base_agent: Agent = Agent(
  name="MathAgent",
  instructions="",
  input_guardrails=[math_input_checker],
  output_guardrails=[math_output_checker]
)

try:
    res = Runner.run_sync(base_agent, "what is a union, answer in one line" , run_config=config)
    print("[OUTPUT]: " , res.final_output)
except InputGuardrailTripwireTriggered as e:
    print("Alert: Guardrail input tripwire was triggered!")
except OutputGuardrailTripwireTriggered as e:
    print("Alert: Guardrail output tripwire was triggered!")
