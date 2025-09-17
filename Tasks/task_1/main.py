"""
1. Accept a user question about programming (e.g., "Explain Python decorators in simple terms").

2.Use dynamic instructions to tell the model to:

-Respond in Markdown format with a level 2 heading for the title.

-Include a numbered list if steps are provided.

3.Validate the response using Pydantic’s BaseModel with two fields:

-title (string)

-content (string)

4.Implement error handling so that if the model’s output does not match the schema, you raise a ModelBehaviorError and retry once with a system message:

"Ensure the output matches the schema strictly."

"""

from agents import Agent, Runner, RunContextWrapper, ModelBehaviorError
from model import config
import asyncio
from pydantic import BaseModel

class validate_response(BaseModel):
  title: str
  content: str




async def main():
  
  def dynamic_instruction(ctx:RunContextWrapper, agent: Agent): #important parameters
    return f"Respond in Markdown format with a level 2 heading for the title. Include a numbered list if steps are provided. "
  
  agent = Agent(
    name = "Agent",
    instructions = dynamic_instruction, #2. dynamic_instruction
    output_type = validate_response #3 pydantic
    
  )
  

  while True:
    # 1. Asking the user their question
    user_question = input("Enter your question: ")
    
    if user_question.lower() == "exit":
      break
    # 4. Error handling
    try:
      result = await Runner.run(
        agent ,
        user_question,
        run_config = config
      )

      print(result.final_output)
    except ModelBehaviorError as e:
      print(e.message)
    
if __name__ == "__main__":
  asyncio.run(main())    