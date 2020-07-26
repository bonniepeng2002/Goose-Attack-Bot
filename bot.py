# bot.py
import os, random, discord, io, aiohttp
from discord.ext import commands
from dotenv import load_dotenv
from discord.utils import find

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')
client = discord.Client()

#---------------------FUNCTIONS----------------------

users=[]
max=300
def assignhealth(member):
    global users, max
    users.append([str(member), max, 0, False, 'Alive']) #[user, health, cp, dead?, status]

def checkifdead(victim):
    global users
    for i in range(len(users)):
        if str(victim)==users[i][0] and users[i][1]<=0:
            users[i][3]=True
            users[i][1]=0
            users[i][4]='Dead'
            return True

#---------------------FILES----------------------

uno = discord.Embed()
uno.set_image(url='https://media.tenor.com/images/ee6e6bb6f35b030eab0dbb7c12040275/tenor.gif')
hap = discord.Embed()
hap.set_image(url='https://m5.paperblog.com/i/68/686386/here-is-theat-happy-goose-again-and-another-o-L-jYMqei.jpeg')
sad = discord.Embed()
sad.set_image(url='https://i1.sndcdn.com/avatars-000178938366-zw94tr-t500x500.jpg')
ang = discord.Embed()
ang.set_image(url='https://i.redd.it/ziyrjzn4fho21.png')
shok = discord.Embed()
shok.set_image(url='https://live.staticflickr.com/5292/5396005497_a4cd1bf1c8_z.jpg')
hung = discord.Embed()
hung.set_image(url='https://marcusmichaels.com/blog/wp-content/uploads/2010/06/goose.jpg')
vio = discord.Embed()
vio.set_image(url='https://1039maxfm.com/wp-content/uploads/sites/8/2019/04/GeeseAttack.png')
horn = discord.Embed()
horn.set_image(url='https://live.staticflickr.com/4055/4415122050_a99d6e1d19_b.jpg')
gang = discord.Embed()
gang.set_image(url='https://a.wattpad.com/cover/84215647-352-k186022.jpg')
lone=discord.Embed()
lone.set_image(url='https://i.redd.it/og8zaq3fib521.jpg')

#---------------------EVENTS----------------------

#send message when joined
@bot.event
async def on_guild_join(guild):
    global users
    users.append(['Mr.Goose#8280', max, 0, False,
                  'Alive'])  # since joining guild, doesn't append itself
    await bot.change_presence(
        activity=discord.Game(name='Untitled Goose Game'))
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('HONK HONK B*TCHES :gun::baby_chick:')
    for guild in bot.guilds:
        for member in guild.members:
            await member.create_dm()
            await member.dm_channel.send(
            f'HONK HONK **{member.name}**!\n'
            f'Always nice to meet another ~~victim~~ friend :heart:\n\n'
            f'Here\'s what you can do:\n'
            f'**!honk** : honk at me and I\'ll respond.\n'
            f'**!mood** : see my current mood.\n'
            f'**!army** : assemble your own goose army, use it to attack others.\n'
            f'**!attack @[user]** : unleash hell on another user.\n'
            f'**!stats** : check your stats.\n'
            f'**!revive @[user]** : revive one of your dead friends... but only if you feel like it...')
            assignhealth(member)
            print(users)

#alert when ready
@bot.event
async def on_ready():
    #await bot.get_channel(735887013215076366).send("HONK activated")
    print('Honk activated')
    #comment the below out when not testing

    for guild in bot.guilds:
        for member in guild.members:
            assignhealth(member)
    await bot.change_presence(activity=discord.Game(name='Untitled Goose Game'))


# we do not want the bot to reply to itself
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
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
    answer = "Assembled goose army of size "+str(number)+"!"
    await ctx.send(answer+"\nready to ~~attack~~ send love")

#!stats
@bot.command(name='stats', help='Check\'s the user\'s stats.')
async def stats(ctx):
    global users
    for i in range(len(users)):
        if str(ctx.message.author.name) in users[i][0]:
            message = '**' + str(
                ctx.message.author.name) + '\'s** stats:\nHealth: ' + str(users[i][1])+"/"+str(max)+"\nStrength: "+str(users[i][2])+"/100\nStatus: "+str(users[i][4])
            await ctx.send(message)

#!attack
lefthealth=0
@bot.command(name='attack', help='Attacks the mentioned user with army previously generated.')
async def attack(ctx, member : discord.Member):
    global lefthealth, users
    say = "With the power of "+str(power)+" geese, \n"+str(ctx.message.author.mention)
    attackquotes=[
        " brutally attacked",
        " knocked out",
        " KO'd",
        " clapped",
        " destroyed",
        " tackled"]
    diequotes=[
        " has been pecked to death by ",
        " has died in the ~~hands~~ *wings* of ",
        " was sent straight to heaven by ",
        " just received the ultimate L by "
    ]
    for h in range(len(users)):
        print(users)

        if str(ctx.message.author)==users[h][0] and users[h][2]==0: #if you dont have army
            await ctx.send("HONK must assemble army first!")
            break

        elif str(member) == users[h][0] and users[h][3] == True:  # if victim is already dead
            await ctx.send(f'**{member.name}** is already dead :dizzy_face:')
            break

        elif str(ctx.message.author) == users[h][0] and users[h][3] == True:  # if you attack when dead
            await ctx.send(
                'You silly goose! You can\'t attack when you\'re dead')
            break

        elif str(ctx.message.author)==users[h][0] and users[h][2]!=0: #if you have army

            if str(member) == str(ctx.message.author): #if you attack yourself
                await ctx.send("Stop it. Get some help.")

            elif str(member) == "Mr.Goose#8280": #if you attack the bot
                await ctx.send(embed=uno)
                await ctx.send(ctx.message.author.mention+" was killed by Mr. Goose.")
                users[h][1]=0
                users[h][3]=True
                users[h][4]='Dead'

            else: #you're allowed to attack
                await ctx.send(say+random.choice(attackquotes)+" <@{}>:bangbang:".format(member.id))

                for j in range(len(users)): #victim
                    for z in range(len(users)): #attacker
                        if str(member)==users[j][0] and str(ctx.message.author)==users[z][0]:
                            lefthealth=users[j][1]-users[z][2] #victims health - attackers cp
                            if lefthealth<=0:
                                lefthealth=0
                            users[j][1]=lefthealth #update victims hp
                await ctx.send("<@{}> has ".format(member.id)+str(lefthealth)+"/"+str(max)+ " HP remaining.")

                if checkifdead(member): #if victim is dead, let em know
                    await ctx.send("<@{}>".format(member.id) + random.choice(diequotes)+ str(
                        ctx.message.author.mention) + "'s army! :coffin:")

@bot.command(name='mood', help='Shows Mr.Goose\'s mood')
async def mood(ctx):
    moods=[['happy',hap, ' :)'],
           ['sad', sad, ' :('],
           ['angry', ang, ' >:('],
           ['shocked', shok, ' :o'],
           ['hungry', hung, ' :9'],
           ['VIOLENT', vio, ' >:0'],
           ['...horny', horn, ' ( ͡° ͜ʖ ͡°)'],
           ['gangsta', gang, ' :triumph::muscle:'],
           ['lonely', lone, ' :\'(']
           ]
    select=random.randint(0,len(moods)-1)
    await ctx.send('Mr. Goose is feeling **'+moods[select][0]+"**"+moods[select][2])
    await ctx.send(embed=moods[select][1])

@bot.command(name='revive', help='revive one of your dead friends... but only if you feel like it...')
async def revive(ctx, member : discord.Member):
    global users
    for i in range(len(users)):
        if str(member)==users[i][0] and users[i][1]==0:
            users[i][1]=300
            users[i][2]=0
            users[i][3]=False
            users[i][4]='Alive'
            await ctx.send('With the power of :dizzy: 𝒻𝓇𝒾𝑒𝓃𝒹𝓈𝒽𝒾𝓅 🎀, <@{}> has been revived!'.format(member.id))
            break
        else:
            await ctx.send(f'**{member.name}** is not dead! ʸᵉᵗ')
            break

@bot.command(name='rps', help='Play rock paper scissors with a goose. Yeah.')
async def rps(ctx, play):
    options=[['rock', 'paper'], ['paper', 'scissors'], ['scissors', 'rock']] #[goose play, what defeats it]
    gplay = str(options[random.randint(0,2)][0])
    print(gplay)
    print(play.lower())
    for i in range(0,len(options)):
        if gplay==options[i][0] and str(play.lower())==options[i][1]:
            await ctx.send(gplay+":bangbang:\nHONK?? :triumph: you win..")
            break
        elif gplay==options[i][1] and str(play.lower())==options[i][0]:
            await ctx.send(gplay+":bangbang:\nHONKK I WIN :crown: you kinda suck.")
            break
        elif gplay==str(play.lower()):
            await ctx.send(gplay+':bangbang:\nHonk... a tie!')
            break

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
