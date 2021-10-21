import os
import re
import discord

exec(open("env.py").read())
WIKI_SUMMARY_TOKEN = os.environ["WIKI_SUMMARY_TOKEN"]

client = discord.Client()
# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('bot が起動しました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/wiki」と発言したら wiki と返す処理
    if re.search('/wiki', message.content):
        word = message.content.strip('/wiki ')
        await message.channel.send(word)


# Botの起動とDiscordサーバーへの接続
client.run(WIKI_SUMMARY_TOKEN)