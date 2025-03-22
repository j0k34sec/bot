from discord.ext import commands
import discord
import json
import os

intents = discord.Intents.default()
intents.voice_states = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def create_vc(ctx, name: str):
    guild = ctx.guild
    channel = await guild.create_voice_channel(name)
    await ctx.send(f'Temporary voice channel {channel.mention} created!')

@bot.command()
async def claim(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
        await ctx.send(f'You have claimed the voice channel {channel.mention}!')
    else:
        await ctx.send('You need to be in a voice channel to claim it.')

@bot.command()
async def delete_vc(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
        await channel.delete()
        await ctx.send(f'Temporary voice channel {channel.name} deleted!')
    else:
        await ctx.send('You need to be in a voice channel to delete it.')

# Load command modules
async def load_extensions():
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            await bot.load_extension(f'commands.{filename[:-3]}')

# Load token from config.json
with open('config.json') as config_file:
    config = json.load(config_file)

# Run the bot
bot.loop.run_until_complete(load_extensions())
bot.run(config['token'])