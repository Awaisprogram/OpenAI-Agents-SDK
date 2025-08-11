from agents import Agent , Runner, SQLiteSession, enable_verbose_stdout_logging
from model import config, model



enable_verbose_stdout_logging()
    # session = SQLiteSession("conversation124")

english_agent = Agent(
        name="english_agent",
        instructions="You are a helpful assistant who always responds in English, no matter the input.",
        model = model
)

 

spanish_agent = Agent(
        name="spanish_agent",
        instructions="You are a helpful assistant who always responds in spanish, no matter the input.",
        model = model
)

urdu_agent = Agent(
        name="urdu_agent",
        instructions="You are a helpful assistant who always responds in urdu, no matter the input.",
        model = model
)

    
agent = Agent(
         name="Main Agent",
        instructions="You are a language router. Decide which language agent should respond.",
        handoffs=[english_agent, spanish_agent,urdu_agent]
    )

while True:
        user_input = input("Enter your message: ")
        if user_input == "exit":
            break
        
        response = Runner.run_sync(
            agent,
            user_input,
            run_config= config,
            # session = session
        )
        
        result = response.final_output
        
        print("=" * 50)
        print("\n", result)
        print("=" * 50)