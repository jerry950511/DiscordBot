#設定非必要不要動
from platform import java_ver
import discord
from discord.ext import commands
import json
import random,asyncio
import time




with open("settings.json","r",encoding="utf8") as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix="!",intents = intents)



#terminal顯示上線
@bot.event
async def on_ready():
    print(">>This bot is online<<")

#加入訊息
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(jdata["channelID"])
    await channel.send(f"歡迎{member}進來到資工臭甲的大家庭")

#離開訊息
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(jdata["channelID"])
    await channel.send(f"{member}離開了資工臭甲的大家庭 以後有緣再見")

#找人打瓦
@bot.event
async def on_message(message):
    if message.content in jdata["瓦羅蘭"]:
       if message.author != bot.user:
        await message.channel.send(f"上線啊你各位<@&913401379865899018>")
    await bot.process_commands(message)
    if message.content.startswith('更改狀態'):
        #切兩刀訊息
        tmp = message.content.split(" ",2)
        #如果分割後串列長度只有1
        if len(tmp) == 1:
            await message.channel.send("你要改成什麼啦？")
        else:
            game = discord.Game(tmp[1])
            #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
            await bot.change_presence(status=discord.Status.idle, activity=game)
    if message.content in jdata["R6"]:
        if message.author != bot.user:
            await message.channel.send(f"欸打R6<@&911531657771773982>")



#指令區

#ping
@bot.command()
async def ping(ctx):
    await ctx.send(f"現在機器人的延遲為{round(bot.latency*1000)}ms")

#logo
@bot.command()
async def logo(ctx):
    await ctx.send(jdata["logo"])

#rex
@bot.command()
async def rex(ctx):
    await ctx.send(jdata["rex"])

#課表
@bot.command()
async def 課表(ctx):
    await ctx.send(jdata["課表"])

#傑哥
@bot.command()
async def 傑哥(ctx):
    await ctx.send(jdata["傑哥"])
  
#dice
@bot.command()
async def dice(ctx):
    await ctx.send(f"1-6選出來的隨機數字為"+random.choice(jdata["dice"]))

#delete msg
@bot.command()
async def clean(ctx,num:int):
    await ctx.channel.purge(limit=num+1)
    await ctx.send("清理完成")
    time.sleep(5)
    await ctx.channel.purge(limit=1)

bot.run(jdata["TOKEN"])