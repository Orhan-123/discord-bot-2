import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

client.run('MTEzNjYwMDk3NTEwOTUyOTY0MQ.Gspglr.PIocRoR9Z0YjLZfwFOECV9F0PU_kOBofMj5tp4')