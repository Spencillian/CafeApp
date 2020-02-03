import os, sys
import json
import discord
import random
import urllib.parse
from itertools import cycle
from discord.ext import commands, tasks
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from CafeBackend import Crawler

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
    print('-' * 30)
    print('[Login info]')
    print(f'Bot Name: {client.user.name}')
    print(f'Bot ID: {client.user.id}')
    print(f'Bot Verson: {Bot_Version}')
    print('-' * 30)
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
                description = 'wHaT cAn I hElP yOu? (☞ﾟヮﾟ)☞',
                colour = discord.Colour.from_rgb(126, 214, 223)
    )
    embed.add_field(name = '**!help**', value = 'Information about this bot.', inline = False)
    embed.add_field(name = '**!meal**', value = 'Provide information about meal plan at Avon Old Farms School.', inline = False)
    embed.add_field(name = '**!weather**', value = 'Weather info at Avon.', inline = False)
    embed.add_field(name = '**!dice <Start> <End>**', value = "Let's Roll the Dice!\n Default value: Start = 1, End = 6", inline = False)
    embed.add_field(name = '**!rdbox <Item 1> <Item 2> ... <Item N>**', value = 'Random Box!', inline = False)
    embed.add_field(name = '**!rdimg <Topic>**', value = 'Random image', inline = False)
    embed.add_field(name = '**!ping**', value = 'pong!', inline = False)
    embed.add_field(name = '**!about**', value = 'Information about Developers', inline = False)
    embed.set_footer(text = f'Avo by Spencer & HyunJun', icon_url = 'https://github.com/MovoLovo/CafeApp/blob/master/Discord-Bot-AOF/LOGO/Avo%20LOGO.png?raw=true')
    await ctx.send(embed = embed)

@client.command()
async def meal(ctx):
    c = Crawler.Crawler()
    c.nav('food')
    await ctx.send(c.get_elements())

@client.command()
async def dice(ctx, start = 1, end = 6):
    rd = random.randrange(start, end)
    if start == 1 and end == 6:
        embed = discord.Embed(
            title = 'Dice',
            description = "Let's Roll the Dice!",
            colour = discord.Colour.from_rgb(126, 214, 223)
        )
        if rd == 1:
            embed.set_image(url = 'https://raw.githubusercontent.com/MovoLovo/CafeApp/master/Discord-Bot-AOF/Image/icons8-dice-one-100.png')
        elif rd == 2:
            embed.set_image(url = 'https://raw.githubusercontent.com/MovoLovo/CafeApp/master/Discord-Bot-AOF/Image/icons8-dice-two-100.png')
        elif rd == 3:
            embed.set_image(url = 'https://raw.githubusercontent.com/MovoLovo/CafeApp/master/Discord-Bot-AOF/Image/icons8-dice-three-100.png')
        elif rd == 4:
            embed.set_image(url = 'https://raw.githubusercontent.com/MovoLovo/CafeApp/master/Discord-Bot-AOF/Image/icons8-dice-four-100.png')
        elif rd == 5:
            embed.set_image(url = 'https://raw.githubusercontent.com/MovoLovo/CafeApp/master/Discord-Bot-AOF/Image/icons8-dice-five-100.png')
        elif rd == 6:
            embed.set_image(url = 'https://raw.githubusercontent.com/MovoLovo/CafeApp/master/Discord-Bot-AOF/Image/icons8-dice-six-100.png')
        embed.set_footer(text = f'Avo by Spencer & HyunJun / Icon by Icons8', icon_url = 'https://github.com/MovoLovo/CafeApp/blob/master/Discord-Bot-AOF/LOGO/Avo%20LOGO.png?raw=true')
        await ctx.send(embed = embed)
    else:
        return await ctx.send(f'||{rd}||')

@client.command()
async def rdbox(ctx, *rdtext):
    if len(rdtext) == 0:
        return await ctx.send('Please enter items.')
    return await ctx.send(f'||{rdtext[random.randrange(0, len(rdtext))]}||')

@client.command()
async def rdimg(ctx, *, topic):
    if topic == "":
        return await ctx.send('Please enter the topic.')
    embed = discord.Embed(
                title = 'Topic',
                description = topic,
                colour = discord.Colour.from_rgb(255, 195, 18)
    )
    embed.set_image(url = f'https://source.unsplash.com/1600x900/?{topic}'.replace(" ", "%20"))
    embed.set_footer(text = f'Avo by Spencer & HyunJun', icon_url = 'https://github.com/MovoLovo/CafeApp/blob/master/Discord-Bot-AOF/LOGO/Avo%20LOGO.png?raw=true')
    await ctx.send(embed = embed)

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

@client.command()
async def about(ctx):
    embed = discord.Embed(
                title = 'About',
                description = 'About Us',
                colour = discord.Colour.from_rgb(186, 220, 88)
    )
    embed.set_thumbnail(url = 'https://github.com/MovoLovo/CafeApp/blob/master/Discord-Bot-AOF/LOGO/Avo%20LOGO.png?raw=true')
    embed.add_field(name = '**API Developer**', value = 'Spencer', inline = False)
    embed.add_field(name = '**Discord Bot Developer**', value = 'HyunJun Park', inline = False)
    embed.add_field(name = '**GitHub**', value = 'https://github.com/MovoLovo/CafeApp', inline = False)
    embed.set_footer(text = f'Avo by Spencer & HyunJun', icon_url = 'https://github.com/MovoLovo/CafeApp/blob/master/Discord-Bot-AOF/LOGO/Avo%20LOGO.png?raw=true')
    await ctx.send(embed = embed)

client.run(BotToken)