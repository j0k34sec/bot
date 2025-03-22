from discord.ext import commands
import discord

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
    # Logic for claiming the VC goes here
    pass

@bot.command()
async def delete_vc(ctx):
    # Logic for deleting the VC goes here
    pass

# Load command modules
for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')

bot.run('YOUR_BOT_TOKEN')