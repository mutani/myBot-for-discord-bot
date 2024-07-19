import discord
import config
from discord.ext import commands
from discord import app_commands
from geminiApi import gemini_onetimetext_api, get_gemini_models, translate_to_english, translate_to_japanese
from sdxl import sdxl_turbo

#config
DISCORD_TOKEN = config.DISCORD_TOKEN
SDXL_TURBO_STATE = config.SDXL_TURBO_STATE
SDXL_TURBO_TEMPORALY_STORAGE = config.SDXL_TURBO_TEMPORALY_STORAGE
SDXL_ANIME_STATE = config.SDXL_ANIME_STATE
SDXL_ANIME_TEMPORALY_STORAGE = config.SDXL_ANIME_TEMPORALY_STORAGE


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

# geminiChatBot
@tree.command(name="chatbot", description="geminiChatBot")
@app_commands.describe(mode="Select mode")
@app_commands.choices(mode=[
    app_commands.Choice(name="ChatBot", value="gemini-1.5-flash"),
    app_commands.Choice(name="ChatBotPro", value="gemini-pro")
])
async def chatbot(interaction: discord.Interaction, mode: str, message: str):
    await interaction.response.defer()
    response_message = gemini_onetimetext_api(message, mode)
    await interaction.followup.send(f"{response_message.data}") 

# geminiTranslate
@tree.command(name="translate", description="geminiを使用した翻訳機能")
@app_commands.describe(mode="select")
@app_commands.choices(mode=[
    app_commands.Choice(name="to English", value="english"),
    app_commands.Choice(name="to Japanese", value="japanese")
])
async def translate(interaction: discord.Interaction, mode: str, message: str):
    await interaction.response.defer()
    response_message = "Error"
    if mode == "english":
        response_message = translate_to_english(message)
    elif mode == "japanese":
        response_message = translate_to_japanese(message)

    await interaction.followup.send(f"{response_message.data}") 

@tree.command(name="draw_sdxl", description="stabilityai/sdxl-turboを使用して画像を生成します(promptは英文を推奨します)")
async def draw_sdxl(interaction: discord.Interaction, message: str):
    await interaction.response.defer()
    state = SDXL_TURBO_STATE
    if state == "on":
        image = sdxl_turbo(message)
        image_path = SDXL_TURBO_TEMPORALY_STORAGE
        if image is not None:
            image.save(image_path)
            with open(image_path, "rb") as file:
                await interaction.followup.send(file=discord.File(file, image_path))
        else:
            await interaction.followup.send(f"エラーが発生しました")
    else:
        await interaction.followup.send(f"draw機能は利用できません")

@tree.command(name="draw_sdxl_anime", description="ntc-ai/SDXL-LoRA-slider.animeを使用して画像を生成")
async def draw_sdxl_anime(interaction: discord.Interaction, message: str):
    await interaction.response.defer()
    state = SDXL_ANIME_STATE
    if state == "on":
        image = sdxl_turbo(message)
        image_path = SDXL_ANIME_TEMPORALY_STORAGE
        if image is not None:
            image.save(image_path)
            with open(image_path, "rb") as file:
                await interaction.followup.send(file=discord.File(file, image_path))
        else:
            await interaction.followup.send(f"エラーが発生しました")
    else:
        await interaction.followup.send(f"draw機能は利用できません")

bot.run(DISCORD_TOKEN)