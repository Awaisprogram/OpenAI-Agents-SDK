import chainlit as cl
from agents import Runner
from my_agent import story_outline_agent, outline_checker_agent, story_agent, OutlineCheckerOutput
from model import config

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="👋 Hi! What kind of story would you like to create today?").send()

@cl.on_message
async def on_message(message: cl.Message):
    user_input = message.content

    await cl.Message(content="✍️ Generating an outline...").send()
    outline_result = await Runner.run(
        story_outline_agent,
        user_input,
        run_config=config
    )
    await cl.Message(content=f"[OUTLINE_GENERATED]\n\n{outline_result.final_output}").send()

    await cl.Message(content="🔍 Checking the outline...").send()
    outline_checker_result = await Runner.run(
        outline_checker_agent,
        outline_result.final_output,
        run_config=config
    )

    assert isinstance(outline_checker_result.final_output, OutlineCheckerOutput)

    if not outline_checker_result.final_output.good_quality:
        await cl.Message(content="❌ Outline is not of good quality. Stopping here.").send()
        return

    # Optionally, check for genre
    # if not outline_checker_result.final_output.is_scifi:
    #     await cl.Message(content="❌ Not a sci-fi story. Stopping here.").send()
    #     return

    await cl.Message(content="✅ Outline is good quality and genre is acceptable. Proceeding to write the story...").send()

    await cl.Message(content="📖 Writing the story...").send()
    story_result = await Runner.run(
        story_agent,
        outline_result.final_output,
        run_config=config
    )

    await cl.Message(content=f"✨ Here is your story:\n\n{story_result.final_output}").send()
