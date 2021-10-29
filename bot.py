import os
import wikipedia
from discord.ext import commands

wikipedia.set_lang('ja')

exec(open('env.py').read())
WIKI_SUMMARY_TOKEN = os.environ['WIKI_SUMMARY_TOKEN']

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

@bot.command()
async def wiki(context, search_word):
    try:
        result = wikipedia.summary(search_word)
    except wikipedia.exceptions.DisambiguationError  as e:
        result = '[error] 曖昧な単語です。より具体的な単語で検索してみてください。'
    except wikipedia.exceptions.PageError  as e:
        result = '[error] ページが存在しない単語です。別の単語で検索してみてください。'
    await context.send(result)

@wiki.error
async def wiki_error(context, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await context.send('[error] 検索単語がありません。\"/wiki 検索単語\" で検索してみてください。')

# Botの起動とDiscordサーバーへの接続
bot.run(WIKI_SUMMARY_TOKEN)