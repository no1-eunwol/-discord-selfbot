import discord
from discord.ext import commands
import asyncio
import json

with open('setting.json', 'r') as f:
    settings = json.load(f)

prefix = settings['prefix']
token = settings['token']


bot = commands.Bot(command_prefix=prefix, self_bot=True)


spam_task = False
mimic_task = False
mention_spam_task = False

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    
    

@bot.command()
async def 도움말(ctx):
    help_message = f"""

# Meow SelfBot.
-# Developed by @aura.x_

>>> 도움말 >> 도움말을 표시합니다.
핑 >> 응답속도를 테스트합니다.
도배 [메세지] >> 지정된 메세지를 도배합니다.
도배정지 >> 도배를 정지합니다.
따라하기 [유저 ID] >> 지정된 유저의 메세지를 따라합니다.
따라하기정지 >> 따라하는 것을 정지합니다.
"""
    
    await ctx.reply(help_message)

@bot.command()
async def 핑(ctx):
    await ctx.reply(f'퐁! 응답속도 : {round(bot.latency * 1000)}ms')

@bot.command()
async def 도배(ctx, message: str):
    global spam_task
    if spam_task == False:
        spam_task = True
        await ctx.reply(f"도배 시작 중: {message}")
        while spam_task:
            await ctx.send(message)
    else:
        await ctx.reply("이미 도배가 진행중입니다.")
        

@bot.command()
async def 도배정지(ctx):
    global spam_task
    
    if spam_task:
        spam_task = False
        await ctx.reply("도배를 정지합니다.")
    
@bot.command()
async def 따라하기(ctx, user_id: int):
    global follow_id
    follow_id = user_id
    await ctx.reply(f"지금부터 {user_id}님의 메세지를 따라합니다.")
    

@bot.command()
async def 따라하기정지(ctx):
    global follow_id
    follow_id = None
    await ctx.reply("stopped mimicking.")

@bot.command()
@command.has_permissions(kick_member = True)
async def 추방(ctx, member: discord.member, *, reason = None)
	try:
        await member.kick(reason = reason)
    	await ctx.send()
    except:
		pass
    except:
        pass
"""
@bot.command()
async def 멘션도배(ctx, user_id: int):
    global mention_spam_task
    mention = f"<@{user_id}>"
    
    if mention_spam_task == False:
        mention_spam_task = True
        await ctx.reply(f"멘션도배 시작: <@{user_id}>")
        count = 0
        while mention_spam_task:
            await ctx.send(f"<@{user_id}>")
            
@bot.command()
async def 멘션도배정지(ctx):
    global mention_spam_task
    
    if mention_spam_task:
        mention_spam_task = False
        await ctx.reply("멘션도배를 정지합니다.")
"""


bot.run(token)

# Developed by aura.x_
