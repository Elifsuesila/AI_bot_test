import discord
from discord.ext import commands
from tensorflow.keras.models import load_model



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='*', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} hazır"*" koyarak komut verebilirsin')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'merhaba ben {bot.user} sana sporlar hakkında bilgi verebilen bir botum')

@bot.command()
async def isminniyehavuç(ctx):
    await ctx.send(f'bende bilmiyorum :))')

@bot.command()
async def havuç(ctx, count_havuc = 5):
    await ctx.send("havuç" * count_havuc)
    



async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("You forgot to upload the image :(")

   

    

bot.run("")