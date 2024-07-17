import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
from geminiApi import gemini_onetimetext_api, get_gemini_models

# .envファイルを読み込む
load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)
tree = bot.tree

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await tree.sync()

@bot.command()
async def chat(ctx, *, message: str):
    response_message = gemini_onetimetext_api(message)
    await ctx.send(response_message.data)

@bot.command()
async def getGeminiModel(ctx):
    response_message = get_gemini_models()
    response_text = "\n".join(response_message)
    await ctx.send(response_text)
    
# geminiChatBotTree
@tree.command(name="chatbot", description="geminiChatBot")
@app_commands.describe(mode="Select mode")
@app_commands.choices(mode=[
    app_commands.Choice(name="ChatBot", value="gemini-1.5-flash"),
    app_commands.Choice(name="ChatBotPro", value="gemini-1.5-pro")
])
async def chatbot(interaction: discord.Interaction, mode: str, message: str):
    await interaction.response.defer()
    response_message = gemini_onetimetext_api(message, mode)
    await interaction.followup.send(f"{response_message.data}") 

bot.run(os.getenv('DISCORD_TOKEN'))