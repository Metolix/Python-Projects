import nextcord as discord
from nextcord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("Ready")

@client.command()
async def ping(ctx):
    latency = round(client.latency * 1000)
    await ctx.reply(f"The latency is `{latency}ms`")


client.run("your discord bot token here")