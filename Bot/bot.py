import discord
from discord.ext import commands

import json
import os

# CONSTANTS
CONFIG_FILE = open("./config.json")
CONFIG_FILE = json.load(CONFIG_FILE)
TOKEN = CONFIG_FILE["TOKEN"]
INTENTS = discord.Intents.all()

bot = commands.Bot(

    command_prefix = ">",
    help_command = None,
    case_insensitive = True,
    activity = discord.Activity(name="the Food Chain", type=discord.ActivityType.competing),
    intents=INTENTS

)

@bot.event
async def on_ready():

    # Import ApplicationCommands
    for file in os.listdir("./Bot/ApplicationCommands"):

        if file.endswith(".py"):

            bot.load_extension(f"ApplicationCommands.{file[:-3]}")
            print("Loaded {}".format(file))

    # Import ChatCommands
    for file in os.listdir("./Bot/ChatCommands"):

        if file.endswith(".py"):

            bot.load_extension(f"ChatCommands.{file[:-3]}")
            print("Loaded {}".format(file))
    

bot.run(TOKEN)