from pydantic import BaseModel , Field
from agents import function_tool
from datetime import datetime


class GreetingsTool(BaseModel):
    name: str = Field(description="The name of the person to greet")


@function_tool
async def Greetings(name: str ) -> GreetingsTool:
    print("Tool is running")

    current_hour = datetime.now().hour

    if 5 <= current_hour < 12:
        greeting = "Good morning"
    elif 12 <= current_hour < 17:
        greeting = "Good afternoon"
    elif 17 <= current_hour < 21:
        greeting = "Good evening"
    else:
        greeting = "Good night"

    
    return f"{greeting}, {name}!"
