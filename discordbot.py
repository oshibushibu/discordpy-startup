import discord
from datetime import datetime
from discord.ext import tasks

TOKEN = "NzAyODMyNTQ1OTcyMjI0MDQw.XtcV_g.YCmaTEH4xVjKHhjI5PBiPmnX9sw" #トークン


CHANNEL_ID = 697732323659218966 #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()


#投稿する日時
dateTimeList = [
'2020/06/03 14:03',
'2019/05/20 18:30',
'2019/05/21 18:30',
'2019/05/22 07:00',
'2019/05/23 07:00',
'2019/05/24 07:00',
'2019/05/25 07:00'
]

# 起動時に動作する処理
@client.event
async def on_ready():
    print('ready')

# 指定時間に走る処理
async def SendMessage():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('時間だよ')

# 30秒に一回ループ
@tasks.loop(seconds=30)
async def time_check():
    sleepTime = 0
    # 現在の時刻
    now = datetime.now().strftime('%Y/%m/%d %H:%M')
    if now in dateTimeList :
        print(now)
        await SendMessage()
        #該当時間だった場合は２重に投稿しないよう３０秒余計に待機
        await asyncio.sleep(30)

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 使用できるコマンド一覧
    if message.content == '!help':
        await message.channel.send('現在使用できるコマンドはありません')

#ループ処理
time_check.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
