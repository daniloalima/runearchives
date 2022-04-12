import discord
import os
from static_commands import *
from static_boss import *
import skills
import boss
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('\n\nlogged in as {0.user}'.format(client))

@client.event
async def on_message(message):

  msg = message.content

  if msg.startswith('rs!skill'):
    skill = msg.split('rs!skill ', 1)[1]
    command = skills.get_command_skill(skill)
    temp = command.split('!')
    function = temp[1]
    reply = eval(function + "()")

    await message.channel.send(reply)

  elif msg.startswith('rs!boss'):
    boss = msg.split('rs!boss ', 1)[1]
    try:
      reply = eval(boss + "()")
    except:
      reply = 'Chefe não encontrado, utitlize **!help** para mais informações'

    await message.channel.send(reply)
  
  elif msg.startswith('rs!ping'):
    reply = f'Pong! {round(client.latency * 1000)}ms'
    await message.channel.send(reply)

  #elif msg.startswith('rs!help'):
  #  helpcmd = msg.split('rs!help ',1)[1]
    
  #  reply = ''
  #  await message.channel.send(reply)

keep_alive()
client.run(os.getenv('BOT_TOKEN'))