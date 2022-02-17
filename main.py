#!/usr/bin/env python3

import discord
import os
from discord.ext import commands
import subprocess

DISCORD_TOKEN = os.environ['ALADAR_BOT']


bot = commands.Bot(command_prefix="!")

@bot.command()
async def ping(ctx):
    await ctx.channel.send("Fixing !")
    subprocess.run(["./restart.sh"])


bot.run(DISCORD_TOKEN)
