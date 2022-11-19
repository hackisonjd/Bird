import os
from dotenv import load_dotenv

# Import the Discord library

import discord

# Loads environment variables from .env file. DO NOT CHANGE THIS LINE AND DO NOT COMMIT .env FILE.

dotenv_path = '.env'
load_dotenv(dotenv_path)

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

# Create an instance of a client, which acts as a connection to Discord. Turning intents on is required for the bot to work.

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# NOTE: In order to add any future commands, you must precede them with a @client.event and an async def. More information can be found here: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

@client.event
# Simple async, which prints to the console when the bot is ready.
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
# Prints to the console whenever a message is sent.
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# TODO: ADD A DICE ROLLING FUNCTIONALITY HERE

# Run the client. DO NOT CHANGE THIS LINE.

client.run(DISCORD_TOKEN)
