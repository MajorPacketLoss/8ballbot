import discord
from discord import app_commands
import os
import random

TOKEN = os.environ.get('DISCORD_TOKEN')
if not TOKEN:
    raise ValueError('DISCORD_TOKEN environment variable not set')

RESPONSES = [
    # Positive
    'It is certain.',
    'It is decidedly so.',
    'Without a doubt.',
    'Yes, definitely.',
    'You may rely on it.',
    'As I see it, yes.',
    'Most likely.',
    'Outlook good.',
    'Yes.',
    'Signs point to yes.',
    # Neutral
    'Reply hazy, try again.',
    'Ask again later.',
    'Better not tell you now.',
    'Cannot predict now.',
    'Concentrate and ask again.',
    # Negative
    "Don't count on it.",
    'My reply is no.',
    'My sources say no.',
    'Outlook not so good.',
    'Very doubtful.',
]

class EightBallBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        @self.tree.command(name='8ball', description='Ask the Magic 8-Ball a question')
        @app_commands.describe(question='The question you want to ask')
        async def eightball(interaction: discord.Interaction, question: str):
            answer = random.choice(RESPONSES)
            embed = discord.Embed(
                title='\U0001f3b1 Magic 8-Ball',
                color=0x1a0080
            )
            embed.add_field(name='Question', value=question, inline=False)
            embed.add_field(name='Answer', value=f'**{answer}**', inline=False)
            await interaction.response.send_message(embed=embed)

        await self.tree.sync()
        print('Slash commands synced globally.')

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')

client = EightBallBot()
client.run(TOKEN)
