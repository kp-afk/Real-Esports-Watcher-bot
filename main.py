import discord 
from discord.ext import commands
import os
from keep_alive import keep_alive
import variables

client = commands.Bot(command_prefix='>>',
                      case_insensitive=True,
                      intents=discord.Intents.all())
client.remove_command('help')
bot_token = os.getenv('DISCORD_BOT_TOKEN')

owner = 550948377148522498

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(
                                type=discord.ActivityType.watching,
                                name="Real Esports Summer League"
                                ))
    print('Started')

"""
@client.command()
@commands.has_any_role(variables.botaccess1, 
                      variables.botaccess2,
                      variables.botaccess3, 
                      variables.botaccess4)
async def rajo(ctx, server_id : int):
  server = client.get_guild(server_id)
  for channel in server.channels:
    try:
      invite = await channel.create_invite(unique=True)
      await ctx.send(f"Invite Created For channel `{channel.name}` in server `{server.name}` \n `{invite}`")
      break
    except:
      print(f"Invite creation failed for channel {channel.name}")
"""

client.load_extension('cmds.tier_2_watch')
client.load_extension('cmds.tier_3_watch')
client.load_extension('cmds.pmsl')
client.load_extension('cmds.other')
client.load_extension('cmds.antiping')
#client.load_extension('cmds.error_handling')

keep_alive()
client.run(bot_token)
