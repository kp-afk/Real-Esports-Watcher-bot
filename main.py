import discord # pip install -e git+git://github.com/kp-afk/discord.py@master#egg=discord.py 
from discord.ext import commands
import os
from keep_alive import keep_alive
#import discord_buttons_plugin
#from discord_buttons_plugin import  *

client = commands.Bot(command_prefix='>>',
                      case_insensitive=True,
                      intents=discord.Intents.all())
client.remove_command('help')
bot_token = os.getenv('DISCORD_BOT_TOKEN')
#buttons = ButtonsClient(client)

"""
@client.command()
async def op(ctx):
 await buttons.send(content =" **Choose Your Age** \nAdult :man:\nBauwa :baby:", channel = ctx.channel.id,
  components = [
		ActionRow([
			Button(
				label="Adult", 
				style=ButtonType().Primary, 
				custom_id="button_one"       
			),
      Button(
				label="Non-Adult", 
				style=ButtonType().Primary, 
				custom_id="button_on"       
			)
		])
	]
  )
"""


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name="Real Esports Summer League"))
    print('Status set.')
    print(f'bot is now ready. ')

client.load_extension('cmds.tier_2_watch')
client.load_extension('cmds.moderation')
client.load_extension('cmds.tier_3_watch')
client.load_extension('cmds.pmsl')
client.load_extension('cmds.other')
client.load_extension('cmds.antiping')
#client.load_extension('cmds.error_handling')

keep_alive()
client.run(bot_token)
