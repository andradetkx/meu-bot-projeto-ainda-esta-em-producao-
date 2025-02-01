import discord
from discord.ext import commands
import random

# Configurando as permissões do bot
permissoes = discord.Intents.default()
permissoes.members = True
permissoes.message_content = True

# Criando o bot com prefixo "/"
bot = commands.Bot(command_prefix="!", intents=permissoes)

# Comando para deletar mensagens
@bot.command()
@commands.has_permissions(manage_messages=True)
async def deltexto(ctx, quantidade: int):
    if quantidade < 1:
        await ctx.send("Digite um número válido (1 ou mais).")
        return
    await ctx.channel.purge(limit=quantidade)
    await ctx.send(f"{quantidade} mensagens foram apagadas.", delete_after=5)

#um simples embed
@bot.command()
async def enviar_embed(ctx:commands.context):
    meu_embed = discord.Embed(title='ola, mundo', description='o mundo e lindo')
    await ctx.send(embed=meu_embed)
    meu_embed.set_image(url='https://pbs.twimg.com/profile_images/1694401953432788993/qTwInwmh_400x400.jpg')
# quando criar um canal ele vai dizer
@bot.event
async def on_guild_channel_create(canal: discord.abc.GuildChannel):
    await canal.send(f"Novo canal criado: {canal.name}")
    
# bot vai dar boa vindas
@bot.event
async def on_member_join(self, member:discord.Member):
    canal = bot.get_channel(1334954067512004661)
    await canal.send(f"bem vindo {member.display_name} ao servidor!!!")

# bot vai dar um tchau para a pessoa
@bot.event
async def on_member_remove(member:discord.member):
    canal = bot.get_channel(1334954067512004661)
    await canal.send(f"{member.display_name} saiu do servidor")

# Comando de barra para mostrar o ping do bot
@bot.tree.command(name="ping", description="Mostra o ping do bot")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong! {round(bot.latency * 1000)}ms")



# Sincronizar os comandos de barra
@bot.event
async def on_ready():
    await bot.tree.sync()  # Sincroniza os comandos de barra
    print(f"Bot {bot.user} está online!")



#token do bot fica aqui
bot.run("")