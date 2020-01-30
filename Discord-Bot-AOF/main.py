import os, sys
import json
import discord
from itertools import cycle
from discord.ext import commands, tasks

Bot_Version = 'Beta 0.0.1'
print("Starting up...")

with open('key.k', 'r') as f:
    TokenData = json.load(f)
BotToken = TokenData['bot']

client = commands.Bot(command_prefix = '!', case_insensitive = True) # Ignore the upper/lower case
client.remove_command('help')

status = cycle(['Say !help', 'AOF Discord Bot', 'AVO'])

@client.event
async def on_ready():
    print('-' * 20)
    print('[Login info]')
    print(f'Bot Name: {client.user.name}')
    print(f'Bot ID: {client.user.id}')
    print(f'Bot Verson: {Bot_Version}')
    print('-' * 20)
    change_status.start()

@tasks.loop(seconds = 15)
async def change_status(): # Change the Bot's status message for every 15 seconds.
    activity = discord.Activity(name = next(status), type = discord.ActivityType.listening)
    await client.change_presence(activity = activity)

@client.event
async def on_message(message): # On Message Event: this will be executed every single time when someone sends the message.
    if message.author.bot: # Ignore the self's message.
        return None
    elif message.content.startswith('!'):
        log(message)
    await client.process_commands(message)

def log(message):
    print(f'[{message.author.name}:{message.author.id}] {message.content}')

@client.command()
async def help(ctx):
    embed = discord.Embed(
                title = 'Help',
                description = 'wHaY cAn I hElP yOu? (☞ﾟヮﾟ)☞',
                colour = discord.Colour.purple()
    )
    embed.add_field(name = '!help', value = 'help', inline = True)
    embed.add_field(name = '!meal', value = 'meal plan', inline = True)
    embed.add_field(name = '!weather', value = 'weather', inline = True)
    await ctx.send(embed = embed)

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

client.run(BotToken)