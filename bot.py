# bot.py
import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

client = discord.Client()

def __init__(self):
    self.bot = discord.Client()

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'HONK\nAwful to meet you {member.name}, I\'m Mr. Goose!\n')

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

@bot.command(name='honk', help='Mr. Goose responds to your honk.')
async def honking(ctx):
    honkquotes = [
        'H Ø Ñ K',
        '........ʰᵒⁿᵏ?',
        'ɥouʞ',
        'ⓗⓞⓝⓚⓗⓞⓝⓚ',
        'h̷̻͉̼̹̬͈̙͎͆̽̈́̈́͠͠o̸̻̞̯͐̈́̉̂͌͠ņ̶̨͓̰̝͈̼͉̲̒̄̌͜͝kh̷̻͉̼̹̬͈̙͎͆̽̈́̈́͠͠o̸̻̞̯͐̈́̉̂͌͠ņ̶̨͓̰̝͈̼͉̲̒̄̌͜͝kh̷̻͉̼̹̬͈̙͎͆̽̈́̈́͠͠o̸̻̞̯͐̈́̉̂͌͠ņ̶̨͓̰̝͈̼͉̲̒̄̌͜͝k̵̡͎̲̫̳͖̩̱̅̔̈́̿̽́̐͝',
        ':woman_fairy::sparkles:  𝒽𝓸𝓃𝓀  :rainbow::revolving_hearts:',
        '(っ◔◡◔)っ ♥ honk ♥',
        'hwonk :3']
    response = random.choice(honkquotes)
    await ctx.send(response)

power=0
@bot.command(name='army', help='Assembles goose army, dont abuse this power.')
async def assemble(ctx):
    global power, ass
    number = int(random.triangular(1,101,10))
    power = number
    answer = "Assembled goose army of size "+str(number)+"!\nCP: "+str(number*12)
    await ctx.send(answer+"\nready to ~~attack~~ say hi")

@bot.command(name='attack', help='Attacks mentioned user with army previously generated.')
async def attack(ctx, member : discord.Member):
    say = "With the power of "+str(power)+" geese, "+str(ctx.message.author.mention)
    if power==0:
        await ctx.send("HONK must assemble army first!")
    else:
        await ctx.send(say+" attacked <@{}>!".format(member.id))

@bot.command(name='create-channel', help='Creates a new channel.')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='channel'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('Honk! You do not have the correct role for this command.')


bot.run(TOKEN)
