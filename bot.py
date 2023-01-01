import discord
from discord.ext import commands 

client = commands.Bot(command_prefix="=", intents= discord.Intents.all())

@client.event
async def on_ready():
    print ("Success: Bot is connected to Discord")

@client.commands
async def ping(ctx):
    await ctx.sends("ping")


client.run("#put_the_bot_token_here")    










