import discord
from discord.ext import commands
import asyncio

bot =commands.Bot(command_prefix="-")

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Activity(type=1,name="with DEEPAK"))
	print("Online with " + bot.user.name)
	
	
@bot.command(name="say")
async def tanmay(ctx,*, content: str):
	author=ctx.message.author
	
	await ctx.send(content)
	
bot.run('NjExNDY1ODI5ODQ1OTU4NjY3.XV1BnA.JeW-MtbRBs7_QVR0U6lhnSiA9Ro')
