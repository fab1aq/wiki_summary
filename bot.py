import os
import wikipedia
import discord

wikipedia.set_lang('ja')

def get_wiki_summary(search_word):
    try:
        result = wikipedia.page(search_word)
        return result.summary
    except wikipedia.exceptions.DisambiguationError  as e:
        return 'wikiの結果が上手く返ってきませんでした。より具体的なワードで検索してみてください。'

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
        print(search_word)
        wiki_summary = get_wiki_summary(search_word)
        await message.channel.send(wiki_summary)

# Botの起動とDiscordサーバーへの接続
client.run(WIKI_SUMMARY_TOKEN)