import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

import gamerscore

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix=',')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='test')
async def saludo(ctx):
    response = 'No testear'
    await ctx.send(response)

@bot.command(name='gm')
async def saludo(ctx, gamertag):
    response = gamerscore.get_gamerscore(gamertag)
    embed = discord.Embed(title='El gamerscore de ' + gamertag + ' es ' + response,  color = discord.Colour.random())
    await ctx.send(embed=embed)

@bot.command(name="pic")
async def saludo(ctx, gamertag):
    embed = discord.Embed(title = 'Foto de ' + gamertag, color = discord.Colour.green())
    embed.add_field(name='Xbox Live', value = gamerscore.get_pic(gamertag))
    await ctx.send(embed=embed)


bot.run(TOKEN)