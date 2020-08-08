import discord
import random
import datetime
import openpyxl
import os
from captcha.image import ImageCaptcha
from discord.ext import commands, tasks
from itertools import cycle
from discord import DMChannel

player_dict = dict()
client = discord.Client()
status = cycle (['24시간 구매문의', '카운터 서버봇 구동중'])

@client.event
async def on_ready():
    change_message.start()
    print(client.user.id)
    print("How to Code a Python?")

def is_not_pinned(mess):
    return not mess.pinned
@client.event
async def on_member_join(member):
    if not member.bot:
        embed = discord.Embed(title='Welcome'.format(member.name),
                              description='구매문의는 오직 COUNTER 님에게만 해주세요 \n 관리자가 답변이 늦을수있으니 양해바랍니다.',
                              color=0xff8080)
        try:
            if not member.dm_channel:
                await member.create_dm()
            await member.dm_channel.send(embed=embed);
        except discord.errors.Forbidden:
            print(''.format(member.name))

@client.event
async def on_message(message):

    if message.content.startswith("!인증"):
        Image_captcha = ImageCaptcha()
        verity = ""
        msg = ""
        for i in range(6):
            verity += str(random.randint(0, 9))

        name = str(message.author.id) + ".png"
        Image_captcha.write(verity, name)

        await message.channel.send(file=discord.File(name))
        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg = await client.wait_for("message", timeout=10, check=check)
        except:
            await message.channel.send("Time out")
            return

        if msg.content == verity:
            await message.channel.send("인증이완료되었습니다.")
            role = discord.utils.get(message.guild.roles, name="인증됨")
            await message.author.add_roles(role)

        else:

            await message.channel.send("인증이거부되었습니다.")


    if "discord.gg" in message.content.lower():
         await message.delete()
         embed = discord.Embed(colour=0xff8080)
         embed.set_author(name="Detected")
         embed.add_field(name='Anti advertisement Detected', value='앞메금지', inline=False)
         await message.channel.send(embed=embed)
    if "https://discord.com" in message.content.lower():
         await message.delete()
         embed = discord.Embed(colour=0xff8080)
         embed.set_author(name="Detected")
         embed.add_field(name='Anti advertisement Detected', value='앞메금지', inline=False)
         await message.channel.send(embed=embed)

    if message.content.startswith('!청소'):
        if message.author.id == (692613343219023922):
            args = message.content.split(' ')
            if len(args) == 2:
                if args[1].isdigit():
                    count = int(args[1]) + 1
                    deleted = await message.channel.purge(limit=count, check=is_not_pinned)
                    await message.channel.send('{}개의 메세지가 삭제되었습니다.'.format(len(deleted) - 1))

    if message.content.startswith("!이번생여친여부"):
        await message.channel.send("얼굴을보아하니 없습니다.")

    if message.content.startswith("!개인디엠"):
        author = message.guild.get_member(int(message.mentions[0].id))
        msg = message.content[23:]
        await author.send(msg)

    if message.content.startswith('!뮤트'):
         author = message.guild.get_member(int(message.mentions[0].id))
         role = discord.utils.get(message.guild.roles, name="뮤트됨")
         await author.add_roles(role)

    if message.content.startswith('!뮤트해제'):
         author = message.guild.get_member(int(message.mentions[0].id))
         role = discord.utils.get(message.guild.roles, name="뮤트됨")
         await author.remove_roles(role)

    if message.content.startswith("!채널공지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await client.get_channel(int(channel)).send(msg)

    if message.content.startswith(""):
        file = openpyxl.load_workbook("레벨.xlsx")
        sheet = file.active
        exp = [10, 20, 40, 80, 160]
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(message.author.id):
                sheet["B" + str(i)].value = sheet["B" + str(i)].value + 5
                if sheet["B" + str(i)].value >= exp[sheet["C" + str(i)].value - 1]:
                    sheet["C" + str(i)].value = sheet["C" + str(i)].value + 1
                    await message.channel.send("당신의 레벨이 올랐습니다.\n현재 레벨 : " + str(sheet["C" + str(i)].value) + "\n경험치 : " + str("B" + str(i).value))
                file.save("레벨.xlsx")
                break

            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(message.author.id)
                sheet["B" + str(i)].value = 0
                sheet["C" + str(i)].value = 1
                file.save("레벨.xlsx")
                break

    if message.content.startswith('!전체디엠'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id == (692613343219023922):
                        embed = discord.Embed(colour=0xff8080, timestamp=message.created_at, title="Notice")
                        embed.add_field(name="`Counter님에 의해 전송되었습니다`", value=msg, inline=True)
                        await i.send(embed=embed)
                except:
                    pass
                
@client.event
async def on_member_join(member):
        embed = discord.Embed(color=0xff00ae)
        embed.add_field(name='Counter Cheat Shop', value=str(member.mention)+'**님 안녕하세요 !**', inline=True)
        embed.set_image(url="https://cdn.discordapp.com/avatars/692613343219023922/a_d3bb9e7b9b62087d120b4e14d20fed61.png")
        embed.set_footer(text=f"https://discord.gg/5Xg4X32", icon_url="https://cdn.discordapp.com/avatars/692613343219023922/a_d3bb9e7b9b62087d120b4e14d20fed61.png?size=128")
        hello = client.get_channel(741507799237918792)
        await hello.send(embed=embed)

@client.event
async def on_member_remove(member):
        embed = discord.Embed(color=0xffa00ae)
        embed.add_field(name='Counter Cheat Shop', value=str(member.mention)+'**님 안녕히가세요....**', inline=True)
        embed.set_image(url="https://cdn.discordapp.com/avatars/692613343219023922/a_d3bb9e7b9b62087d120b4e14d20fed61.png")
        embed.set_footer(text=f"https://discord.gg/5Xg4X32", icon_url="https://cdn.discordapp.com/avatars/692613343219023922/a_d3bb9e7b9b62087d120b4e14d20fed61.png?size=128")
        bye = client.get_channel(741507823585722368)
        await bye.send(embed=embed)

@tasks.loop(seconds=5)
async def change_message():
    await client.change_presence(activity=discord.Game(next(status)))

acsess_token = os.environ["BOT_TOKEN"]
client.run("access_token")
