import discord
import os
import skills
import skills_combate
import commands

client = discord.Client()

@client.event
async def on_ready():
  print('logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  command = commands.get_command(message)
  skill = ''
  temp = command.split('!')
  skill = temp[1]
  

client.run(os.getenv('BOT_TOKEN'))