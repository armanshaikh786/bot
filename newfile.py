import discord
from discord.ext import commands

bot =commands.Bot(command_prefix="-")

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Activity(type=1,name="with ARMAN"))
	print("Online with " + bot.user.name)
	
	
@bot.command(name="say")
async def tanmay(ctx,*, content: str):
	author=ctx.message.author
	
	await ctx.send(content)
	
bot.run('NjEzNzM3NzQ0MzA4MzcxNDU2.XV1TWQ.jZkjlDHk7Ihyjy4Q4nF4DSvVtLk')
