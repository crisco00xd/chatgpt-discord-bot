import openai
import discord
import os
from discord.ext import commands
import traceback
import asyncio

openai.api_key = os.environ['OPENAI_API_KEY']


# Global Variables
intents = discord.Intents.all()
intents.members = True
COMMAND_PREFIX = '/'
ENGINE = "gpt-3.5-turbo"
DEFAULT_TEMPERATURE = 0.5
temperature = DEFAULT_TEMPERATURE
conversation_histories = {}

bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

async def on_command_error(ctx, error):
    print(f"Error: {error}")
    await ctx.send("An error has occurred while processing your request. Please try again later.")

async def clear_history_after_timeout(user_id, timeout):
    await asyncio.sleep(timeout)
    if user_id in conversation_histories:
        del conversation_histories[user_id]

async def add_message_to_history(user_id, role, content):
    if user_id not in conversation_histories:
        conversation_histories[user_id] = []

    conversation_histories[user_id].append({
        "role": role,
        "content": content
    })

async def get_conversation_history(user_id):
    if user_id in conversation_histories:
        return conversation_histories[user_id]
    return []

@bot.command()
async def smart(ctx, *, prompt):
    user_id = ctx.author.id
    await add_message_to_history(user_id, "user", prompt)

    try:
        history = await get_conversation_history(user_id)
        completions = openai.ChatCompletion.create(
            model=ENGINE,
            messages=history,
            max_tokens=1024,
            n=1,
            temperature=temperature,
        )
        message = completions.choices[0].message['content']
        await add_message_to_history(user_id, "assistant", message)

        # Split the message into chunks of 2000 words -> Discord MAX Char Limit
        chunks = [message[i:i+2000] for i in range(0, len(message), 2000)]

        # Send the chunks as separate messages
        for chunk in chunks:
            await ctx.send(chunk)

        # Clear the user's conversation history after an hour of inactivity
        asyncio.create_task(clear_history_after_timeout(user_id, 3600))

    except Exception as e:
        # Print the traceback here
        print(traceback.format_exc())

        # Send a message to the user to let them know that an error has occurred
        await on_command_error(ctx, e)

@bot.command()
async def temp(ctx, *, value):
    global temperature
    try:
        new_temperature = float(value)
        if new_temperature < 0.1 or new_temperature > 2.0:
            await ctx.send(f"Max Value: 2.0 \n Min Value: 0.1")
        else:
            temperature = new_temperature
            await ctx.send(f"Temperature Changed To {temperature}")
    except ValueError:
        await ctx.send("Please Input A Number (Min = 0.1 : Max = 2.0)")

bot.add_listener(on_ready, 'on_ready')
bot.add_listener(on_command_error, 'on_command_error')
bot.run(os.environ['DISCORD_API_KEY'])
