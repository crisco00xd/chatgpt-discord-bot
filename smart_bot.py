import openai
import discord
import re
import os
from discord.ext import commands

openai.api_key = os.getenv('OPENAI_API_KEY')

# Add intents parameter to the commands.Bot constructor
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

temperature = 0.5 #Default Value
tempo = 0.0

@bot.command()
async def smart(ctx, *, prompt):
    try:
        completions = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            temperature=temperature,
        )
        message = completions.choices[0].text
        if "code" in prompt.lower():
            message = '`' + message.lstrip() + '`'
        
        # split the message into chunks of 2000 words -> Discord MAX Char Limit
        chunks = [message[i:i+2000] for i in range(0, len(message), 2000)]
        
        # send the chunks as separate messages
        for chunk in chunks:
            await ctx.send(chunk)
        
    except Exception as e:
        # You can print the traceback here using the traceback module
        import traceback
        print(traceback.format_exc())

        # You can also send a message to the user to let them know that an error has occurred
        await ctx.send("An error has occurred while processing your request. Please try again later.")


@bot.command()
async def temp(ctx, *, value):
    global tempo
    global temperature
    tempo = temperature
    try:
        temperature = float(value)
        await ctx.send(f"Temperature Changed To {temperature}")
    except ValueError:
        temperature = tempo #Safety Switch
        await ctx.send("Don't be a bitch and input a number you dumb shit...")

bot.run(os.getenv('DISCORD_API_KEY'))
