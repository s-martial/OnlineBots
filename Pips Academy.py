# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 13:27:26 2019

@author: MARTIAL Stephane
"""


import discord
from discord.ext import commands
import random
import csv
from requests_html import HTMLSession
import datetime
import aiohttp
import json
import asyncio
from quotes import quote
from Admin_token import t

from discord.utils import get
import youtube_dl
import os

TOKEN = t

bot = commands.Bot(command_prefix='.', help_command=None)
client = bot

@bot.event
async def on_ready():
    #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Trader News!'))
    #await bot.change_presence(activity=discord.Game(name="Fortnite"))
    #await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="forex orderflow!"))
    print('Bot is ready.')


bot.remove_command('help')
@bot.command(pass_context=True)
async def hello(ctx):
    await ctx.send(f'Hello! \nTapez .aide si vous avez besoin de moi ! {round(client.latency*1000)}ms')

@bot.command(pass_context=True)
async def Hello(ctx):
    if ctx.author.guild_permissions.administrator == True:
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(description=" ** ` Hello @everyone ` :man_office_worker: \n:wavy_dash: ** ", color=0xF4C434)
        await ctx.send(embed=embed)
    else:
        await ctx.send(":x:  {}, Vous n'avez pas la permission d'utiliser cette commande.".format(ctx.author.mention))

l
@bot.command(pass_context=True, aliases=['quotes'])
async def Quotes(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(description=random.choice(quote), color=0x04dca8)
    await ctx.send(embed=embed)


bot.remove_command('help')

@bot.command(pass_context=True, no_pm=True, aliases=['aide'])
async def help(ctx):
    author = ctx.author
    embed = discord.Embed(description=":robot:   Vous avez demandé de l'aide ? Me voici !", color=0xFFFF)
    embed.add_field(name=" .aide | .help ", value="Menu d'aide", inline=True)
    embed.add_field(name=" .quotes ", value="Phrase de motivation", inline=True)
    embed.add_field(name=" .ping | .dée ", value="commandes Fun !", inline=True)
    embed.add_field(name=" .bitcoin ", value="cours BTC/USD", inline=True)
    embed.add_field(name=" .kick membre raison ", value=" Kick un membre", inline=True)
    embed.add_field(name=" .ban membre raison", value="bannir un membre", inline=True)
    embed.add_field(name=" .unban membre raison", value="unban un membre", inline=True)
    embed.add_field(name=" .mute", value="mute un membre", inline=True)
    embed.add_field(name=" .unmute", value="unlute un membre", inline=True)
    await author.send(embed=embed)
    embed = discord.Embed(description=" ", color=0xFFFF)
    m = await ctx.send(":stopwatch: ")
    await asyncio.sleep(2)
    await m.delete()
    em = discord.Embed()
    em.add_field(name="L'aide est arrivé ... :white_check_mark:  ", value=" . \nPlease check your **Direct Messages**",
                 inline=True)
    await ctx.send(embed=em)
    channel = bot.get_channel(603463285915779075)
    embed = discord.Embed(title=f"User: {ctx.author.name} a utilisé la commande .aide",
                          description=f"User ID: {ctx.author.id}", color=0xff9393)
    await channel.send(embed=embed)

@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')

@bot.command(aliases=['dés', 'dée', 'dées'])
async def _8ball(ctx):
    responses = ['1',
                 '2',
                 '3',
                 '4',
                 '5',
                 '6']
    await ctx.send(f'{random.choice(responses)}')


#----------------------------------------- CLOSE DATA - FOREX -----------------------------------------------

@bot.command()
async def bitcoin(ctx):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await ctx.send("Bitcoin price is :  $" + response['bpi']['USD']['rate'])


@bot.command(pass_context=True)
async def usclose(ctx):
    session = HTMLSession()

    url = 'https://fr.investing.com/indices/us-30-historical-data'
    # web response stored as variable, 'r'
    r = session.get(url).html
    data = r.find('#results_box', first=True).text.split()
    AClose = data[18]
    AVar = data[23]
    url = 'https://fr.investing.com/indices/us-spx-500-historical-data'
    # web response stored as variable, 'r'
    r = session.get(url).html
    data = r.find('#results_box', first=True).text.split()
    BClose = data[18]
    BVar = data[23]
    url = 'https://fr.investing.com/indices/nq-100-historical-data'
    # web response stored as variable, 'r'
    r = session.get(url).html
    data = r.find('#results_box', first=True).text.split()
    CClose = data[18]
    CVar = data[23]
    url = 'https://fr.investing.com/indices/volatility-s-p-500-historical-data'
    # web response stored as variable, 'r'
    r = session.get(url).html
    data = r.find('#results_box', first=True).text.split()
    DClose = data[18]
    DVar = data[23]
    url = 'https://fr.investing.com/rates-bonds/u.s.-3-year-bond-yield-historical-data'
    # web response stored as variable, 'r'
    r = session.get(url).html
    data = r.find('#results_box', first=True).text.split()
    EClose = data[16]
    EVar = data[20]
    url = 'https://fr.investing.com/rates-bonds/u.s.-5-year-bond-yield-historical-data'
    # web response stored as variable, 'r'
    r = session.get(url).html
    data = r.find('#results_box', first=True).text.split()
    FClose = data[16]
    FVar = data[20]
    url = 'https://fr.investing.com/rates-bonds/u.s.-10-year-bond-yield-historical-data'
    # web response stored as variable, 'r'
    r = session.get(url).html
    data = r.find('#results_box', first=True).text.split()
    GClose = data[16]
    GVar = data[20]
    url = 'https://fr.investing.com/rates-bonds/u.s.-30-year-bond-yield-historical-data'
    # web response stored as variable, 'r'
    r = session.get(url).html
    data = r.find('#results_box', first=True).text.split()
    HClose = data[16]
    HVar = data[20]
    url = 'https://fr.investing.com/indices/smallcap-2000-futures-historical-data'
    # web response stored as variable, 'r'
    r = session.get(url).html
    data = r.find('#results_box', first=True).text.split()
    IClose = data[18]
    IVar = data[23]
    Idate = data[17]

    await ctx.channel.purge(limit=1)
    author = ctx.author
    embed = discord.Embed(description=f"U.S. Close au {Idate}", color=0xDF3232)
    embed.add_field(name=" ***DOW 30*** ", value=f"{AClose}  " f"({AVar})", inline=True)
    embed.add_field(name=" ***S&P 500*** ", value=f"{BClose}  " f"({BVar})", inline=True)
    embed.add_field(name=" ***NASDAQ*** ", value=f"{CClose}  " f"({CVar})", inline=True)
    embed.add_field(name=" ***SMALLCAP 2000*** ", value=f"{IClose}  " f"({IVar})", inline=True)
    embed.add_field(name=" ***CBOE VIX*** ", value=f"{DClose}  " f"({DVar})", inline=True)
    embed.add_field(name=" ***3 years notes***", value=f"{EClose}  " f"({EVar})", inline=True)
    embed.add_field(name=" ***5 years notes***", value=f"{FClose}  " f"({FVar})", inline=True)
    embed.add_field(name=" ***10 years notes***", value=f"{GClose}  " f"({GVar})", inline=True)
    embed.add_field(name=" ***30 years notes***", value=f"{HClose}  " f"({HVar})", inline=True)

    await ctx.channel.send(embed=embed)

@bot.command(pass_context=True, aliases=['eurclose'])
async def euclose(ctx):
    session = HTMLSession()

    url = 'https://fr.investing.com/indices/germany-30-historical-data'
    # web response stored as variable, 'r'
    r = session.get(url).html
    data = r.find('#results_box', first=True).text.split()
    IClose = data[18]
    IVar = data[23]
    url = 'https://fr.investing.com/indices/uk-100-historical-data'
    # web response stored as variable, 'r'
    r = session.get(url).html
    data = r.find('#results_box', first=True).text.split()
    JClose = data[18]
    JVar = data[23]
    url = 'https://fr.investing.com/indices/france-40-historical-data'
    # web response stored as variable, 'r'
    r = session.get(url).html
    data = r.find('#results_box', first=True).text.split()
    PClose = data[18]
    PVar = data[23]
    url = 'https://fr.investing.com/indices/eu-stoxx50-historical-data'
    # web response stored as variable, 'r'
    r = session.get(url).html
    data = r.find('#results_box', first=True).text.split()
    LClose = data[18]
    LVar = data[23]
    url = 'https://fr.investing.com/indices/spain-35-historical-data'
    # web response stored as variable, 'r'
    r = session.get(url).html
    data = r.find('#results_box', first=True).text.split()
    MClose = data[18]
    MVar = data[23]
    url = 'https://fr.investing.com/indices/it-mib-40-historical-data'
    # web response stored as variable, 'r'
    r = session.get(url).html
    data = r.find('#results_box', first=True).text.split()
    NClose = data[18]
    NVar = data[23]
    Idate = data[17]

    await ctx.channel.purge(limit=1)
    author = ctx.author
    embed = discord.Embed(description=f"EU Close au {Idate}", color=0x328BDF)
    embed.add_field(name=" ***DAX*** ", value=f"{IClose}  " f"({IVar})", inline=True)
    embed.add_field(name=" ***FTSE 100*** ", value=f"{JClose}  " f"({JVar})", inline=True)
    embed.add_field(name=" ***CAC 40*** ", value=f"{PClose}  " f"({PVar})", inline=True)
    embed.add_field(name=" ***STOXX 50*** ", value=f"{LClose}  " f"({LVar})", inline=True)
    embed.add_field(name=" ***IBEX 35***", value=f"{MClose}  " f"({MVar})", inline=True)
    embed.add_field(name=" ***FTSE MIB***", value=f"{NClose}  " f"({NVar})", inline=True)

    await ctx.channel.send(embed=embed)

@bot.command(pass_context=True, aliases=['apclose'])
async def asianclose(ctx):
        session = HTMLSession()

        url = 'https://fr.investing.com/indices/japan-ni225-historical-data'
        # web response stored as variable, 'r'
        r = session.get(url).html
        data = r.find('#results_box', first=True).text.split()
        AClose = data[18]
        AVar = data[23]
        url = 'https://fr.investing.com/indices/hang-sen-40-historical-data'
        # web response stored as variable, 'r'
        r = session.get(url).html
        data = r.find('#results_box', first=True).text.split()
        BClose = data[18]
        BVar = data[23]
        url = 'https://fr.investing.com/indices/aus-200-historical-data'
        # web response stored as variable, 'r'
        r = session.get(url).html
        data = r.find('#results_box', first=True).text.split()
        CClose = data[18]
        CVar = data[23]
        url = 'https://fr.investing.com/indices/s-p-cnx-nifty-historical-data'
        # web response stored as variable, 'r'
        r = session.get(url).html
        data = r.find('#results_box', first=True).text.split()
        DClose = data[18]
        DVar = data[23]
        Idate = data[17]

        await ctx.channel.purge(limit=1)
        author = ctx.author
        embed = discord.Embed(description=f"ASIAN-PACIFIC Close au {Idate}", color=0xDF7E32)
        embed.add_field(name=" ***NIKKEI 225*** ", value=f"{AClose}  " f"({AVar})", inline=True)
        embed.add_field(name=" ***HANG SENG*** ", value=f"{BClose}  " f"({BVar})", inline=True)
        embed.add_field(name=" ***S&P ASX*** ", value=f"{CClose}  " f"({CVar})", inline=True)
        embed.add_field(name=" ***NIFTY 50*** ", value=f"{DClose}  " f"({DVar})", inline=True)


        await ctx.channel.send(embed=embed)


@bot.command(pass_context=True)
async def fxclose(ctx):
    session = HTMLSession()

    url = 'https://fr.investing.com/currencies/xau-usd-historical-data'
    # web response stored as variable, 'r'
    r = session.get(url).html
    data = r.find('#results_box', first=True).text.split()
    AClose = data[16]
    AVar = data[20]
    url = 'https://fr.investing.com/crypto/bitcoin/btc-usd-historical-data'
    # web response stored as variable, 'r'
    r = session.get(url).html
    data = r.find('#results_box', first=True).text.split()
    BClose = data[18]
    BVar = data[23]
    url = 'https://fr.investing.com/commodities/crude-oil-historical-data'
    # web response stored as variable, 'r'
    r = session.get(url).html
    data = r.find('#results_box', first=True).text.split()
    CClose = data[18]
    CVar = data[23]
    url = 'https://fr.investing.com/indices/usdollar-historical-data'
    # web response stored as variable, 'r'
    r = session.get(url).html
    data = r.find('#results_box', first=True).text.split()
    DClose = data[18]
    DVar = data[23]
    url = 'https://fr.investing.com/commodities/natural-gas-historical-data'
    # web response stored as variable, 'r'
    r = session.get(url).html
    data = r.find('#results_box', first=True).text.split()
    EClose = data[18]
    EVar = data[23]
    Idate = data[17]

    await ctx.channel.purge(limit=1)
    author = ctx.author
    embed = discord.Embed(description=f"FX Close au {Idate}", color=0x33C946)
    embed.add_field(name=" ***GOLD*** ", value=f"{AClose}  " f"({AVar})", inline=True)
    embed.add_field(name=" ***BTC/USD*** ", value=f"{BClose}  " f"({BVar})", inline=True)
    embed.add_field(name=" ***WTI Crude Oil*** ", value=f"{CClose}  " f"({CVar})", inline=True)
    embed.add_field(name=" ***DXY*** ", value=f"{DClose}  " f"({DVar})", inline=True)
    embed.add_field(name=" ***Nat GAZ***", value=f"{EClose}  " f"({EVar})", inline=True)

    await ctx.channel.send(embed=embed)


#----------------------------------------- DELETE MESSAGE -----------------------------------------------

@bot.command(aliases=['clean'])
async def clear(ctx, amount=1):
    if ctx.author.guild_permissions.administrator == True:
        await ctx.channel.purge(limit=amount)
    else:
        await ctx.send(":x:  {}, Vous n'avez pas la permission d'utiliser cette commande.".format(ctx.author.mention))


#----------------------------------------- JOIN CHANNEL -----------------------------------------------

@client.event
async def on_member_join(member):
    mention=member.mention
    guild=member.guild
    await member.create_dm()
    await member.dm_channel.send(str(f"{mention}, Bienvenue chez {guild}").format(mention=mention, guild=guild))

    embed = discord.Embed(title=str(f"***Bienvenue chez {guild}***  :chart_with_upwards_trend:"), colour=0x33C946, description=str(f" Vous êtes le {len(list(member.guild.members))} ème membre ! \nJe vous invite à prendre connaissance du règlement \npour débloquer les channels.").format(mention=mention, guild=guild))
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    embed.timestamp = datetime.datetime.utcnow()
    embed.add_field(name="User ID:", value=member.id)
    embed.add_field(name="User Name:", value=member.display_name)
    embed.add_field(name="Server Name:", value=guild)
    embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    channel = discord.utils.get(member.guild.channels, id=int("603463285915779075"))
    await channel.send(embed=embed)


#----------------------------------------- LEAVE CHANNEL -----------------------------------------------

@client.event
async def on_member_remove(member):
    mention=member.mention
    guild=member.guild

    embed = discord.Embed(title=str(f"***Aurevoir ***"), colour=0x33C946, description=str(f"{mention} a quitté le server ! \n Nous sommes {len(list(member.guild.members))} members.").format(mention=mention, guild=guild))
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    embed.timestamp = datetime.datetime.utcnow()
    embed.add_field(name="User ID:", value=member.id)
    embed.add_field(name="User Name:", value=member.display_name)
    embed.add_field(name="Server Name:", value=guild)
    embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    channel = discord.utils.get(member.guild.channels, id=int("642790992080273408"))
    await channel.send(embed=embed)

#----------------------------------------- Role de base -----------------------------------------------

@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 603483179017568267:
        print(payload.emoji.name)
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == '👍':
            role = discord.utils.get(guild.roles, name='Free Members')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print("done!")
            else:
                print('Membre non trouvé')
        else:
            print('role non trouvé')
    else:
        print('erreur')

    channel = discord.utils.get(member.guild.channels, id=int("603665352139735040"))
    await channel.send(F":robot:   Hello, {member.name} !   \ntapez  *** .aide***  si vous avez besoin de moi.")

@client.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == 603483179017568267:
        print(payload.emoji.name)
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == '👍':
            role = discord.utils.get(guild.roles, name='Free Members')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                print("done!")
            else:
                print('Membre non trouvé')
        else:
            print('role non trouvé')
    else:
        print('erreur')


#----------------------------------------- KICK, BAN, UNBAN, MUTE, UNMUTE -----------------------------------------------

@bot.command(name="kick", pass_context=True)
async def kick(ctx, user: discord.Member = None, *, arg = None):
    if ctx.author.guild_permissions.kick_members == True:
        if user is None:
            await ctx.send(" Qui souhaitez-vous kick.")
            return False
        if arg is None:
            await ctx.send("J'ai besoin d'une raison pour kick: **{}**".format(user.name))
            return False
        reason = arg
        author = ctx.author
        await user.kick()
        embed = discord.Embed(title="Successfully Kicked!", description=" ", color=0x00ff00)
        embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
        embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
        embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
        embed.set_image(url=random.choice(['https://media.giphy.com/media/m9eG1qVjvN56H0MXt8/giphy.gif', 'https://media.giphy.com/media/UrcXN0zTfzTPi/giphy.gif', 'https://media.giphy.com/media/7DzlajZNY5D0I/giphy.gif']))
        await ctx.send(embed=embed)
    else:
        await ctx.send(":x:  {}, Vous n'avez pas la permission d'utiliser cette commande.".format(ctx.author.mention))

@bot.command(name="ban", pass_context=True)
async def ban(ctx, user: discord.Member = None, *, arg = None):
    if ctx.author.guild_permissions.ban_members == True:
        if user is None:
            await ctx.send(" Qui souhaitez-vous bannir ?")
            return False
        if arg is None:
            await ctx.send(" J'ai besoin d'une raison pour bannir : **{}**".format(user.name))
            return False
        reason = arg
        author = ctx.author
        await user.ban()
        embed = discord.Embed(title="Successfully Banned! :white_check_mark:", description=" ", color=0xFF0000)
        embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
        embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
        embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
        embed.set_image(url=random.choice(['https://media.giphy.com/media/fe4dDMD2cAU5RfEaCU/giphy.gif', 'https://media.giphy.com/media/xULW8izI3d8mgPYtA4/giphy.gif', 'https://media.giphy.com/media/n8PUlihJfF5f2/giphy.gif']))
        await ctx.send(embed=embed)
    else:
    	await ctx.send(":x:  {}, Vous n'avez pas la permission d'utiliser cette commande.".format(ctx.author.mention))

@bot.command()
async def unban(ctx,user:int):
    if ctx.message.author.guild_permissions.ban_members == True:
        try:
            who=await bot.get_user_info(user)
            await bot.unban(ctx.guild,who)
            await ctx.send(":white_check_mark: Unbanned!")
        except:
            await ctx.send("Oh No, Something went wrong!!")
    else:
        await ctx.send(":x:  {}, Vous n'avez pas la permission d'utiliser cette commande.".format(ctx.author.mention))

@bot.command(name="mute", pass_context=True)
async def _mute(ctx, user: discord.Member = None, *, arg = None):
    if ctx.author.guild_permissions.manage_messages == True:
        if user is None:
            await ctx.send("Qui voulez-vous mute ?")
            return False
        if arg is None:
            await ctx.send("Pour quelle raison voulez-vous mute **{}** ?".format(user.name))
            return False
        reason = arg
        author = ctx.author
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await user.add_roles(role)
        embed = discord.Embed(title="Successfully Muted!   :white_check_mark:", description=" ", color=0xFFA500)
        embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
        embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
        embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
        embed.set_image(url=random.choice(['https://media.giphy.com/media/Lpo6QNQc4ivdaVm3RG/giphy.gif', 'https://media.giphy.com/media/A7XLVY8QoE3n8KzpjP/giphy.gif', 'https://media.giphy.com/media/NdKVEei95yvIY/giphy.gif', 'http://giphygifs.s3.amazonaws.com/media/B46OnS3oGxk5y/giphy.gif']))# https://cdn.discordapp.com/attachments/524655977832775710/541446963887996939/Fade_image.png
        await ctx.send(embed=embed)
    else:
    	await ctx.send(":x:  {}, Vous n'avez pas la permission d'utiliser cette commande.".format(ctx.author.mention))

@bot.command(name="unmute", pass_context=True)
async def _unmute(ctx, user: discord.Member = None, *, arg = None):
    if ctx.author.guild_permissions.manage_messages == True:
        if user is None:
            await ctx.send("Qui voulez-vous unmute ?")
            return False
        if arg is None:
            await ctx.send("Pour quelle raison voulez-vous unmute {}".format(user.name))
            return False
        reason = arg
        author = ctx.author
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await user.remove_roles(role)
        embed = discord.Embed(title="Unmuted   :white_check_mark:", description=" ", color=0x00ff00)
        embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
        embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
        embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
        embed.set_image(url="https://media.giphy.com/media/8Iv5lqKwKsZ2g/giphy.gif")
        await ctx.send(embed=embed)
    else:
    	await ctx.send(":x:  {}, Vous n'avez pas la permission d'utiliser cette commande.".format(ctx.author.mention))





bot.run(TOKEN)
