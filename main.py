import discord
import os
import utils
from keep_alive import keep_alive
import random

client = discord.Client()

@client.event
async def on_ready():
  print('\n\nlogged in as {0.user}'.format(client))

@client.event
async def on_message(message):

  msg = message.content

  if msg.startswith('!o'):
    fields = msg.split(' ')
    try:      
      dice_pool = fields[1]
      modifier = fields[2]
      dt = fields[3]
    except Exception as e:
      reply = f'Exception {e}'
    else:
      reply = f'Seguindo para validate fields'

    dice_rolled = random.randint(1,20)
    
    await message.channel.send(reply)

  # if msg.startswith('rs!skill'):
  #   skill = msg.split('rs!skill ', 1)[1]
  #   command = skills.get_command_skill(skill)
  #   temp = command.split('!')
  #   function = temp[1]
  #   reply = eval(function + "()")

  #   await message.channel.send(reply)

  # elif msg.startswith('rs!boss'):
  #   boss = msg.split('rs!boss ', 1)[1]
  #   try:
  #     reply = eval(boss + "()")
  #   except:
  #     reply = 'Chefe não encontrado, utitlize **!help** para mais informações'

  #   await message.channel.send(reply)
  
  # elif msg.startswith('rs!ping'):
  #   reply = f'Pong! {round(client.latency * 1000)}ms'
  #   await message.channel.send(reply)

  #elif msg.startswith('rs!help'):
  #  helpcmd = msg.split('rs!help ',1)[1]
    
  #  reply = ''
  #  await message.channel.send(reply)

keep_alive()
client.run(os.getenv('BOT_TOKEN'))