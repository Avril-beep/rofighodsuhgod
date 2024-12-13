import discord
from discord.ext import commands
import os
import random

def reci():
    recis = [
    '''Macetas de botellas plásticas
Materiales: Botellas de plástico, tijeras, pinturas acrílicas, pinceles.
Instrucciones:
1. Corta la botella por la mitad o en la forma que prefieras.
2. Decora el exterior con pintura acrílica o marcadores permanentes.
3. Llena con tierra y planta hierbas, flores o suculentas.''',

    '''Pulseras o collares con plástico derretido
Materiales: Plástico transparente (como de envases de yogur), tijeras, pintura, horno.
Instrucciones:
1. Corta el plástico en formas pequeñas (círculos, corazones, etc.).
2. Pinta las piezas o déjalas transparentes.
3. Hornéalas a baja temperatura para moldearlas.
4. Ensarta en hilos o cadenas para crear accesorios.''',

    '''Portalápices decorativo
Materiales: Botellas plásticas, tela o papel decorativo, pegamento.
Instrucciones:
1. Corta una botella de plástico a la altura deseada.
2. Forra con tela o papel decorativo.
3. Usa como portalápices o para guardar pinceles.''',

    '''Mosaicos de plástico reciclado
Materiales: Tapas de plástico, base de cartón o madera.
Instrucciones:
1. Junta tapas de distintos colores.
2. Pégalas en una base para formar figuras, letras o patrones.
3. Crea cuadros o decoraciones para colgar.''',

    '''Flores decorativas
Materiales: Botellas de plástico, tijeras, pintura, alambres.
Instrucciones:
1. Corta el fondo o la parte superior de la botella en forma de pétalos.
2. Pinta y ensambla con alambres para hacer ramos decorativos.''',

    '''Estuches con cierre
Materiales: Botellas plásticas, tijeras, cierre (cremallera), pegamento.
Instrucciones:
1. Corta dos bases de botellas de plástico.
2. Une las dos partes con un cierre utilizando pegamento resistente.
3. Usa como estuche para lápices o pequeños objetos.''',

    '''Juguetes o figuras decorativas
Materiales: Botellas, tapas, tijeras, pegamento, ojos móviles.
Instrucciones:
1. Usa las botellas y tapas para crear figuras como animales o robots.
2. Decora con pintura y accesorios pequeños.'''
]
    return random.choice(recis)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Comando no encontrado. Revisa el prefijo y el nombre del comando.")
    else:
        raise error
    
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def reciclar(ctx):
    await ctx.send(f'claro, aquí hay un ejemplo: ' + reci())
bot.run(token)
