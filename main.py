import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv
import datetime

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=nextcord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Game("Title Fight"), status=nextcord.Status.dnd)
    print(f"Logged in as {bot.user}\nPing on startup: {round(bot.latency*1000)}ms")

@bot.slash_command(name='embedtest', description='Embed test', force_global=True)
async def embedtest(interaction: nextcord.Interaction):
    embed = nextcord.Embed(
        title="Man Paper Scissors",
        description=f"It's currently {interaction.user.mention}'s turn.", # type: ignore
        timestamp=datetime.datetime.now()
    )

    await interaction.send(embed=embed)

@bot.slash_command(name='echo', description='Echoes your message!', force_global=True)
async def echo(interaction: nextcord.Interaction, args):
    await interaction.response.send_message(f"{interaction.user.mention} {args}") # type: ignore
    print(f"{bot.user}: {args}")

@bot.slash_command(name="ping", description='Shows the bot latency', force_global=True)
async def ping(interaction: nextcord.Interaction):
    await interaction.send(f"Pong! **{round(bot.latency*1000)}ms**", ephemeral=True)

@bot.slash_command(name='rps', description="Challenge someone to a game of Rock Paper Scissors", force_global=True)
async def rps(interaction: nextcord.Interaction, recipient: nextcord.User):
    await interaction.send(f"{recipient.mention}, you have been challenged to a manly game of Rock Paper Scissors by {interaction.user.mention}! To start playing, click one of the (3) buttons below.") # type: ignore

bot.run(str(TOKEN))