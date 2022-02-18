import os
import discord
import random
from discord.ext import commands
from server import keep_alive
from replit import db
import trading as tr
bot = commands.Bot(command_prefix= "$-")

@bot.event
async def on_ready():
  print("We have logged in as {0.user}".format(bot))

@bot.command(name='buy')
async def _buy(ctx, sname):
  value=tr.getinfo(str(sname))
  if value>0:
    await ctx.send('STOCK BROUGHT at '+ str(value))
  else:
    await ctx.send('STOCK NOT AVAILABle')
  


@bot.command(name='check')
async def _check(ctx):
  if ctx.author.name not in db.keys():
    await ctx.send("YOU HAVE NOT REGISTERED. WANT TO REGISTER ? Use register command")
  else:
    await ctx.reply("You are already registered")

@bot.command(name='register')
async def _register(ctx):
  if ctx.author.name not in db.keys():
    db[ctx.author.name]=1
    await ctx.reply("YOU are now REGISTERED.")
  else:
    await ctx.reply("You are already a registered user")
my_secret = os.environ['token']
keep_alive()        
bot.run(my_secret)
