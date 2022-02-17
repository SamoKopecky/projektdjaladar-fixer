#!/usr/bin/env python3

import discord
import os
from discord.ext import commands
import subprocess

DISCORD_TOKEN = os.getenv("ALADAR_FIXER_BOT")

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("ready!")
    await bot.change_presence(activity=discord.Game(name="!fix"))

@bot.command()
async def fix(ctx):
    await ctx.channel.send(r"Anyways, um... I bought a whole bunch of shungite rocks, do you know what shungite is? Anybody know what shungite is? No, not Suge Knight, I think he's" 
    + " locked up in prison. I'm talkin' shungite. Anyways, it's a two billion year-old like, rock stone that protects against frequencies and unwanted frequencies that may be traveling in " 
    + "the air. That's my story, I bought a whole bunch of stuff. "
    + " Put 'em around the la casa. Little pyramids, stuff like that.")
    subprocess.run(["./restart.sh"])


bot.run(DISCORD_TOKEN)
