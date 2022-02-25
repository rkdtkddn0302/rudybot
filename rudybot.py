import discord
from discord.ext import commands
import os
import random
from discord.activity import game
from random import *
client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():

  print(client.user.name)
  game = discord.game('루디는 열심히 일')
  await client.change_presence(stauts=discord.Status.online, activity=game)
  print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)

@client.event
async def on_message(message):
  if message.content == "안녕":
    await message.channel.send("하이")

client.run(os.environ['token'])