import discord
from discord.ext import commands
import os
from keep_alive import keep_alive
import variables

client = commands.Bot(command_prefix='>>',
                      case_insensitive=True,
                      intents=discord.Intents.all())

bot_token = os.getenv('DISCORD_BOT_TOKEN')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                activity=discord.Activity(
                                type=discord.ActivityType.watching,
                                name="Real Esports Summer League"))
    print('Started')
    channel = client.get_channel(827849966000144424)
    guild = client.get_guild(565508242843631616)
    await channel.connect()
    await guild.change_voice_state(channel=channel, self_deaf=True, self_mute=False)

client.load_extension('cmds.tier_2_watch')
client.load_extension('cmds.tier_3_watch')
client.load_extension('cmds.pmsl')
client.load_extension('cmds.other')
client.load_extension('cmds.antiping')
client.load_extension('cmds.admin')

keep_alive()
client.run(bot_token)
