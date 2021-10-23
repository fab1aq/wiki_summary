import os
import wikipedia
import discord

wikipedia.set_lang('ja')

exec(open('env.py').read())
WIKI_SUMMARY_TOKEN = os.environ['WIKI_SUMMARY_TOKEN']

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
    # 「/wiki」と発言したら wiki の要約を返す
    if message.content.startswith('/wiki'):
        search_word = message.content.strip('/wiki ')
        try:
            result = wikipedia.summary(search_word)
        except wikipedia.exceptions.DisambiguationError  as e:
            result = '[error] 曖昧な単語です。より具体的な単語で検索してみてください。'
        except wikipedia.exceptions.PageError  as e:
            result = '[error] ページが存在しない単語です。別の単語で検索してみてください。'
        await message.channel.send(result)

# Botの起動とDiscordサーバーへの接続
client.run(WIKI_SUMMARY_TOKEN)