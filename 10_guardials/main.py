from agents import Agent, Runner, GuardrailFunctionOutput, input_guardrail, InputGuardrailTripwireTriggered, RunContextWrapper, output_guardrail, OutputGuardrailTripwireTriggered, function_tool
from typing import Any
from pydantic import BaseModel
from model import config


@function_tool
def get_weather():
    return "Rainy"



class WeatherSanitizer(BaseModel):
   is_weather: bool
   reasoning: str 


weather_sanitizer = Agent(
    name="WeatherSanitizer",
    instructions="Check if this is a weather related query",
    output_type=WeatherSanitizer,
)


@input_guardrail
async def weather_input_checker(
    ctx: RunContextWrapper, agent: Agent, input
) -> GuardrailFunctionOutput:
    result = await Runner.run(weather_sanitizer, input,  run_config = config)
    print("output: ", result.final_output)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        # tripwire_triggered=False #result.final_output.is_math_homework,
        tripwire_triggered=result.final_output.is_weather is False,
    )
     
@output_guardrail
def weather_response_checker(ctx: RunContextWrapper, agent: Agent, output: Any):    
    # CODE REGREX PATTERN......
    # AGENT Call -> Special guardrail agent
    return GuardrailFunctionOutput(
        output_info="passed",
        tripwire_triggered=False
        )

base_agent: Agent = Agent(
    name="WeatherAgent",
    instructions="You are a helpful assistant.",
    input_guardrails=[weather_input_checker],
    output_guardrails=[weather_response_checker],
    tools=[get_weather]
)


try:
    res = Runner.run_sync(base_agent, "What is the weather today" , run_config=config)
    print("[OUTPUT]: " , res.final_output)
except InputGuardrailTripwireTriggered as e:
    print("Alert: Guardrail input tripwire was triggered!")
except OutputGuardrailTripwireTriggered as e:
    print("Alert: Guardrail output tripwire was triggered!")