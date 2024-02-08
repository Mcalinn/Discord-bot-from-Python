import discord
from discord.ext import commands
import youtube_dl

# Создаем экземпляр бота
intents = discord.Intents.default()
intents.voice_states = True
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)

# Функция для загрузки и воспроизведения музыки
@bot.command()
async def play(ctx, url):
# Подключаемся к голосовому каналу пользователя
    channel = ctx.message.author.voice.channel
    voice_client = await channel.connect()

# Загружаем музыку из YouTube по указанному URL
    ydl_opts = {'format': 'bestaudio'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    url2 = info['formats'][0]['url']
    voice_client.play(discord.FFmpegPCMAudio(url2))

# Функция для отключения бота от голосового канала
@bot.command()
async def leave(ctx):
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client.is_connected():
      await voice_client.disconnect()

# Запускаем бота
bot.run('tokens')
