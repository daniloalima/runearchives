import discord
import os
from skills import herblore

client = discord.Client()

@client.event
async def on_ready():
  print('logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  reply = ''

  if message.author == client.user:
    return

  if message.content.startswith('rs!herb') or message.content.startswith('rs!herblore'):
    reply = herblore()
    await message.channel.send(reply)


client.run(os.getenv('BOT_TOKEN'))