import discord
from discord.ext import commands
import os
import random
from random import *
client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online)
  print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)

@client.event
async def on_message(message):
  if message.content == "안녕":
    await message.channel.send("하이")

client.run(os.environ['token'])