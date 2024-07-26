import discord
from discord.ext import commands
from bot_class import MyView,read_config,read_color

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def button(ctx):
    user_mention = ctx.author.mention #ดึงข้อมูลของคนกด
    view = MyView()
    embed = discord.Embed(title = "Verification", 
                        description = "Click below to verify.",
                        colour=discord.colour.parse_hex_number(read_color())
                        )
    await ctx.send(embed = embed,view=view)
    # await ctx.send("Here is a button:", view=view)

bot.run(read_config())
