
import os
from dotenv import load_dotenv
import discord
from discord import app_commands 
from discord.ext import commands
import google.generativeai as genai

#configuration
load_dotenv()
discord_api_key = os.getenv("DISCORD_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)
model=genai.GenerativeModel("gemini-pro")


chat = model.start_chat(history=[])

intents = discord.Intents.default()
intents.messages = True
intents.message_content  = True

bot = commands.Bot(command_prefix="!" , intents=intents)

#BOT EVENT
@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Bot is ready")



@bot.tree.command(name="yaki", description="Talk to Sakura")
async def yaki(interaction:discord.Interaction, message:str):
    await interaction.response.defer()
    response = chat.send_message(message)
    await interaction.followup.send(response.text)



bot.run(discord_api_key)