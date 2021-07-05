import discord
from discord.ext import commands
import variables
import asyncio
import re


class other(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
      try:
        await ctx.message.delete()
      except:
        pass
      await ctx.send(f'pong! {round(self.client.latency * 1000)}ms')
        
        
    @commands.command()
    @commands.has_guild_permissions(view_audit_log=True)
    async def embed(self, ctx, title, fieldname, *, content):
      try:
        await ctx.message.delete()
      except:
        pass
      embed=discord.Embed(title=f"**{title}**", color=0x28f0e3)
      embed.add_field(name=f"{fieldname}",value=f"```{content}```", inline=False)
      embed.set_footer(text="▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
      await ctx.send(embed=embed)

    @commands.command(hidden=True)
    @commands.has_guild_permissions(view_audit_log=True)
    async def edit(self, ctx, arg1, *, arg2):
      try:
        await ctx.message.delete()
      except:
        pass
      channel = self.client.get_channel(854740291584393236)
      x = await channel.fetch_message(arg1)
      embed=discord.Embed(title=f"**Group B Weekly War **", color=0x28f0e3)
      embed.add_field(name=f"Slot List", value=f"```{arg2}```", inline=False)
      await x.edit(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
      if "t2wait" in message.content:
        embedVar = discord.Embed(title="Tier 2 Normal Waiting time", description="**Real Esports** always welcome you in Tier 2 Normally waiting time is   **1 week** but at present time **100 of teams are in Queue** so it may take at least **3 or 4 weeks.** When we reach to Your team we will contact you ourselves. You will get a **DM** on behalf of tier 2 the bot of Real Esports will be alert you in your dm \nOtherwise you can contact to [Admin](https://discord.com/channels/565508242843631616/842458727416332308/848775392331956244)", color=0x00ff00)
        await message.channel.send(embed=embedVar)

  
    


    """
    @commands.Cog.listener()
    async def on_message(self, message):
      if "https://tenor.com/view" in message.content:
        return
        
      urls = re.findall('(((((http|ftp|https|gopher|telnet|file|localhost):\\/\\/)|(www\\.)|(xn--)){1}([\\w_-]+(?:(?:\\.[\\w_-]+)+))([\\w.,@?^=%&:\\/~+#-]*[\\w@?^=%&\\/~+#-])?)|(([\\w_-]{2,200}(?:(?:\\.[\\w_-]+)*))((\\.[\\w_-]+\\/([\\w.,@?^=%&:\\/~+#-]*[\\w@?^=%&\\/~+#-])?)|(\\.((in|gg|org|com|net|edu|gov|mil|int|arpa|biz|info|unknown|one|ninja|network|host|coop|tech)|(jp|br|it|cn|mx|ar|nl|pl|ru|tr|tw|za|be|uk|eg|es|fi|pt|th|nz|cz|hu|gr|dk|il|sg|uy|lt|ua|ie|ir|ve|kz|ec|rs|sk|py|bg|hk|eu|ee|md|is|my|lv|gt|pk|ni|by|ae|kr|su|vn|cy|am|ke))))))(?!(((ttp|tp|ttps):\\/\\/)|(ww\\.)|(n--)))', message.content)
      
      
      if urls != []:
        await message.delete()
    """
      
      

      


def setup(client):
    client.add_cog(other(client))
