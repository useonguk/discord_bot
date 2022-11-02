import discord
from discord.ext import commands

bot = commands.Bot( command_prefix='!!',intents=discord.Intents.all()) # #을 앞에 넣어서 명령어 실행

@bot.event
async def on_ready():#봇이 시작될 떄 실행되는 이벤트 함수
    print(f"Login bot: {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('!!hello'):
        await message.channel.send('Hellow!!')

bot.run('MTAzNjg0MjM5NzU2MjMyNzEwMw.G71jqx._Zkbp1m9o8kO3t2KPaQMO7wuQreThODgcQ6IMk')