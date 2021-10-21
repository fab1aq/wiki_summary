import os
import discord

exec(open("env.py").read())
WIKI_SUMMARY_TOKEN = os.environ["WIKI_SUMMARY_TOKEN"]

client = discord.Client()
# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('bot が起動しました')

# Botの起動とDiscordサーバーへの接続
client.run(WIKI_SUMMARY_TOKEN)