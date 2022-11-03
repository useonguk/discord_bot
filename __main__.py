# discord 라이브러리 사용 선언
from discord.ext import commands
import discord
import requests
from bs4 import BeautifulSoup
import datetime
import re

bot = commands.Bot(command_prefix='!!',intents=discord.Intents.all())
now = str(datetime.datetime.now())
day = now[:4] + now[5:7] + now[8:10]

print(day)

req = requests.get("http://stu.sen.go.kr/sts_sci_md01_001.do?schulCode=B100000579&schulCrseScCode=4&schulKndScCode=04&schMmealScCode=2&schYmd=2022.11.03")
#print(req.text)
soup = BeautifulSoup(req.text, "html.parser")
#print(soup)
element = soup.find_all("tr")
#print(element[2])
element = element[2].find_all('td')

element = element[5]  # num
element = str(element)
element = element.replace('[', '')
element = element.replace(']', '')
element = element.replace('<br/>', '\n')
element = element.replace('<td class="textC last">', '')
element = element.replace('<td class="textC">', '')
element = element.replace('</td>', '')
element = element.replace('(h)', '')
element = element.replace('.', '')
element = re.sub(r"\d", "", element)

print(element)

class chatbot(discord.Client):
    # 프로그램이 처음 실행되었을 때 초기 구성
    async def on_ready(self):
        # 상태 메시지 설정
        # 종류는 3가지: Game, Streaming, CustomActivity
        game = discord.Game("내용")

        # 계정 상태를 변경한다.
        # 온라인 상태, game 중으로 설정
        await client.change_presence(status=discord.Status.online, activity=game)

        # 준비가 완료되면 콘솔 창에 "READY!"라고 표시
        print("READY")

    # 봇에 메시지가 오면 수행 될 액션
    @bot.event
    async def on_message(self, message):
        # SENDER가 BOT일 경우 반응을 하지 않도록 한다.
        if message.author.bot:
            return None

        if message.content.startswith('!!hellow'):
            await message.channel.send('Hellow')

        elif message.content.startswith('!!급식'):
             # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg =  element
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        


# 프로그램이 실행되면 제일 처음으로 실행되는 함수
if __name__ == "__main__":
    # 객체를 생성
    client = chatbot(intents=discord.Intents.all())
    # TOKEN 값을 통해 로그인하고 봇을 실행
    client.run("MTAzNjg0MjM5NzU2MjMyNzEwMw.GqXcNS.FGNnr5oEIhyv0nM5dvqJlFzFVIBGK7dWKdgFqE")