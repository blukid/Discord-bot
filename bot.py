#!/usr/bin/python3
import os
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

letterkenny_greeting = [
    'how\'re ya now?',
    'how are ya now?',
    'how\'re you now?',
    'how are you now?'
]

letterkenny_random_quotes = [
    'How\'re ya now?',
    'That\'s what I appreciates about yas.',
    'Wish you weren\'t so fuckin awkward, bud.'
]

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.casefold() in letterkenny_greeting:
        response = 'Good, and you?'
        await message.channel.send(response)

    if message.content.casefold() == 'good bot':
        response = 'Good human'
        await message.channel.send(response)

    if message.content.casefold() == 'bad bot':
        response = 'Fuck you Jonesy'
        await message.channel.send(response)

    await bot.process_commands(message)

@bot.command(name='lk')
async def random_lk_quote(ctx, help='Random Letterkenny quote'):
    response = random.choice(letterkenny_random_quotes)
    await ctx.send(response)

@bot.command(name='roll', help='Roll dem dice')
#TODO: allow input of 'xdy' where x = num_dice and y = num_sides
async def roll(ctx, num_dice: int, num_sides: int):
    dice = [
        str(random.choice(range(1, num_sides +1)))
        for _ in range(num_dice)
    ]
    total = 0
    for x in dice:
        total += int(x)
    await ctx.send(', '.join(dice) + ', total: ' + str(total))

bot.run(TOKEN)
