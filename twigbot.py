import discord
from discord.ext import commands
import os 
import requests

intents = discord.Intents.all()
intents.members = True

client = discord.Bot(command_prefix="/", intents=intents)

@client.event
async def on_ready():
    print('Meow?')
    activity = discord.Activity(type=discord.ActivityType.watching, name="the starlings as autumn draws in")
    await client.change_presence(activity=activity)

# create Slash command group with bot.create_group
greetings = client.create_group("greetings")

@greetings.command()
async def hi(ctx):
    await ctx.respond(f"Hello, {ctx.author} Mreowwwwwww!")

@client.slash_command()
async def help(ctx):
    await ctx.respond(f"Here's a provided list of my commands!") # i'm too lazy to add the commands stuff, maybe later

@client.slash_command()
async def sexytime (ctx):
    await ctx.respond(f"https://cdn.discordapp.com/attachments/977409205126447124/1079781794754338926/v09044g40000cfg1vh3c77u2ftqve8d0.mov")

@client.slash_command()
async def help (ctx):
    await ctx.respond(f"Hi there! Here's a list of my commands 


client.run("token")
