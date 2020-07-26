# bot.py
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord.utils import find

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')
client = discord.Client()


#---------------------FUNCTIONS----------------------

users=[]
def assignhealth(member):
    global users
    users.append([str(member), 300, 0, False]) #[user, health, cp, dead?]

def checkifdead(victim):
    global users
    for i in range(len(users)):
        if str(victim)==users[i][0] and users[i][1]<=0:
            users[i][3]=True
            return True

#---------------------EVENTS----------------------

#send message when joined
@bot.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('HONK HONK B*TCHES\nI have arrived :gun::baby_chick:')
    for guild in bot.guilds:
        for member in guild.members:
            #await member.create_dm()
            #await member.dm_channel.send(
            #f'HONK HONK **{member.name}**!\n'
            #f'Always nice to meet another ~~victim~~ friend :heart:')
            assignhealth(member.id)

#alert when ready
@bot.event
async def on_ready():
    #await bot.get_channel(735887013215076366).send("HONK activated")
    print('Honk activated')
    for guild in bot.guilds:
        for member in guild.members:
            print(member)
            assignhealth(member)

# we do not want the bot to reply to itself
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == client.user:
        return

#---------------------COMMANDS----------------------

#!honk
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
        'hwoonnk :3',
        'HONK (╯ ͠° ͟ʖ ͡°)╯┻━┻ HONK'
    ]
    response = random.choice(honkquotes)
    await ctx.send(response)

#!army
power=0
@bot.command(name='army', help='Assembles powerful goose army')
async def assemble(ctx):
    global power, users
    number = int(random.triangular(1,101,10))
    power = number
    person= str(ctx.message.author)
    for i in range(len(users)):
        if users[i][0]==person:
            users[i][2]=power
    answer = "Assembled goose army of size "+str(number)+"!\nCP: "+str(number*12)
    await ctx.send(answer+"\nready to ~~attack~~ send love")

#!attack
lefthealth=0
@bot.command(name='attack', help='Attacks the mentioned user with army previously generated.')
async def attack(ctx, member : discord.Member):
    global lefthealth
    say = "With the power of "+str(power)+" geese, "+'\n'+str(ctx.message.author.mention)
    attackquotes=[
        " brutally attacked",
        " knocked out",
        " KO'd",
        " clapped",
        " assaulted",]
    diequotes=[
        " has been pecked to death by ",
        " has died in the ~~hands~~ *wings* of ",
        " was sent straight to heaven by ",
        " IS BLASTING OFF AGAINNN :skull: Thanks a lot, ",
        " just received the ultimate L by "
    ]
    for h in range(len(users)):
        if str(ctx.message.author)==users[h][0] and users[h][2]==0:
            await ctx.send("HONK must assemble army first!")
            break
        elif str(ctx.message.author)==users[h][0] and users[h][2]!=0:
            await ctx.send(say+random.choice(attackquotes)+" <@{}>:bangbang:".format(member.id))

            for j in range(len(users)): #victim
                for z in range(len(users)): #attacker
                    if str(member)==users[j][0] and str(ctx.message.author)==users[z][0]:
                        lefthealth=users[j][1]-users[z][2] #victims health - attackers cp
                        users[j][1]=lefthealth #update victims hp
            await ctx.send("<@{}> has ".format(member.id)+str(lefthealth)+"/300 HP remaining.")

            if checkifdead(member): #if victim is dead, let em know
                await ctx.send("<@{}>".format(member.id) + random.choice(diequotes)+ str(
                    ctx.message.author.mention) + "'s army! :coffin:")

'''
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
'''

bot.run(TOKEN)
