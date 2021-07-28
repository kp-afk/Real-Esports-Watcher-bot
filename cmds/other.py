import discord
from discord.ext import commands, tasks
import variables
import asyncio
import re
from cmds import utils

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
      embed.set_footer(text="▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
      await ctx.send(embed=embed)

  
    @commands.Cog.listener()
    async def on_message(self, message):
      y = message.content.replace(" ", "")
      x = y.casefold() 
      channelids = [827290385037524992, 857501729213120531, 829663937179418624]
      if not message.channel.id in channelids:
        return
      if "t2wait" in x:
        embedVar = discord.Embed(title="Tier 2 Normal Waiting time", description="**Real Esports** always welcome you in Tier 2 Normally waiting time is   **2 Day** but at present time **20 of teams are in Queue** so it may take at least **1 or 2 weeks.** When we reach to Your team we will contact you ourselves. You will get a **DM** on behalf of tier 2 the bot of Real Esports will be alert you in your dm \nOtherwise you can contact to [Admin](https://discord.com/channels/565508242843631616/842458727416332308/848775392331956244)", color=0x00ff00)
        await message.channel.send(embed=embedVar)

      if "update" in x:
        embedVar1 = discord.Embed(title="Scrims News"  , description= "**1.** Our all Scrims and customs held  in new latest update of Battlegrounds Mobile India from 14 July.\n**2.** Read Detail announcement [here](https://discord.com/channels/565508242843631616/827725966905966612/864458708935639050)", color=0x00ff00)
        await message.channel.send(embed=embedVar1)

      if "t2proofs" in x:
        embedVar2 = discord.Embed(title="Tier 2 Proof Rules"  , description= "**1.** According to the category you have selected, you will have to send your achievements in the mail. \n**2.** We have a few selected esports to accept Tier 2 achievements, we do not accept all esport achievements at this time. If you want us to accept your achievements, you must verify your esports that you have submitted. check <#827306000112680960>. \n**3.** Your Team must have the same prefix for all players.  \n**4.** We do not accept screenshots taken by Room Spectator. Also We do not accept IDP, Slot list, without bar code certificates, or whatsapp screenshots as a valid proof. \n**5.** We do not accept old lineup achievements as a valid proof if your team have three same player you recruited only 1 player then we can accept your achievements. ", color=0x00ff00)
        await message.channel.send(embed=embedVar2)

      if "certificate" in x:
        embedVar4 = discord.Embed(title="Nice, this is good question?" , description= "may be you are finding your team certificate but real esports is awarding team's in these few topic \n- Top  3 Semi Finals of BGMISL \n- Top  3 Finals of BGMISL \n- Top  3 of Weekly Tier  2 Leaderboard", color=0x00ff00)
        await message.channel.send(embed=embedVar4)

      if "t2r" in x:
        embedVar5 = discord.Embed(title="Tier 2 Requirement"  , description= "**1.** REAL ESPORTS OFFICIAL TOURNAMENT SEMIFINALIST'S.\n**2.** OFFICIAL TOURNAMENT QUALIFIED \n**3.** SEMI FINALIST OF UNOFFICIAL TOURNAMENT WITH 15K+ PRIZEPOOL AND FINALIST OF 8K+ PRIZEPOOL \n**4.** PMCO TOP 100 (AFTER QUALIFIERS END) \n**5.** PMIT  SEMIFINALIST'S \n**6.** PMCO TOP 30 \n**7.** PLAYING T2 OF REPUTED ESPORTS LIST HERE <#827306000112680960>", color=0x00ff00)
        await message.channel.send(embed=embedVar5)
    
      if "t2time" in x and message.channel.id == 829663937179418624:
        
        embed=discord.Embed(title="Real Esports tier 2 time here", description="With a board meeting we decide tier 2 new time. bcz Tier 2 is off due to some busy events, After a long time period real esports starting again the tier 2 which is happening in BGMI. \n `Note` - Tier 2 happening only on : Monday to Saturday \n You can see new timeline -  ", color=0x01c2e4)
        embed.add_field(name="INSTA LINK ", value="[RealEsports](https://www.instagram.com/realesports5/)", inline=False)
        embed.add_field(name="Registration Start :", value="10 AM [ SUNDAY ]", inline=True)
        embed.add_field(name="Registration off :", value="10 PM [ SUNDAY ]", inline=True)
        embed.add_field(name="IDP AT :", value="01:05 PM/ 02:05 PM", inline=True)
        embed.add_field(name="START AT  :", value="01:15 PM / 02:15 PM", inline=True)
        embed.add_field(name="Results : ", value="10 PM [ In Insta ] ", inline=True)
        embed.set_footer(text="This is by  tier 2 team")

        try:
          await message.author.create_dm()
          await message.author.dm_channel.send(embed =  embed)
          await message.channel.send("Check Your DM")
        except:
          await message.reply(f"I couldn't dm you! \nMake sure you dms are open.")

      if "subscription" in x and message.channel.id == 829663937179418624:
        embed=discord.Embed(title="Championship Scrims League 2021 Subscription plan ", description=" Currently we only have one week subscription for Tier-2 Teams.\n If they've missed registration of tier 2 and they need slot in T2 for a week they need to pay :  200 Rs. On Gpay/Phonepe or Paytm _ 6376731053 ( This is not contact or support call number)", color=0x01c2e4)

        try:
          await message.author.create_dm()
          await message.author.dm_channel.send(embed =  embed)
          await message.channel.send("Check Your DM")
        except:
          await message.reply(f"I couldn't dm you! \nMake sure you dms are open.")

      if "t2rules" in x and message.channel.id == 829663937179418624:
        embed=discord.Embed(title="CSL Tier 2 Rules", description=" **New tier 2 guidelines released read all rules be careful.** \n**1.** Your Team must have the same prefix for all players. \n**2.** A team all members id must be minimum 25+ Level.\n**3.** If your team entering the room with 1 or 2 players then your results not countable. \n**4.** Certificate Valid only for 6 Months.\n**5.** Your team must have the same logo for all members.\n**6.** When You Entered In-Room You need to take 2 Screenshots for your team to check the example in   <#850033810318032947>. and send in <#844845058812411924> . If you miss this process then your results not counting. `Note - Team IGL can send these Screenshot.`\n**7.** Make sure your all player is registered and allowed for t2 from admin.\n🆕**8.** Make sure your team doesn't finish in the first zone if you finshed in first zone then results not counted.", color=0x01c2e4)

        try:
          await message.author.create_dm()
          await message.author.dm_channel.send(embed =  embed)
          await message.reply("**Read Rules be carefully in your DM **")
        except:
          await message.reply(f"I couldn't dm you! \nMake sure you dms are open.")

      if "t1rules" in x and message.channel.id == 857501729213120531:
        embed=discord.Embed(title="These are New tier 1 guidelines for admission, **Read all rules carefully.**", description="1. All 4 Team members must have the same prefix in their In game name\n 2. All 4 Team member's Game IDs must be above level 25\n 3. All 4 Team members must have same In-game avatar.\n 4. Atleast one team member must stream their T1 Match gameplay on youtube\n 5. You need to send your achievements when asked for, but if your achievements are not valid for t1 or we get fake achievements then you will be banned for 7 days.\n 6. Your Team Must have played atleast a single tournament with 50k prizepool", color=0x66d9ff)
        try:
          await message.author.create_dm()
          await message.author.dm_channel.send(embed =  embed)
          await message.reply("**Read Rules be carefully in your DM **")
        except:
          await message.reply(f"I couldn't dm you! \nMake sure you dms are open.")

      if "t1r" in x and message.channel.id == 857501729213120531:
        embed=discord.Embed(title="**Tier 1 Requirement**", description="1. PMCO SEMI FINALIST & FINALISTS.\n 2. PMIT SEMIFINALIST & FINALISTS.\n 3. TOP 2 FOR 2 CONSECUTIVE MONTHS IN REAL ESPORTS T2\n 4. TOP 100 IN ANY TOURNAMENT HOSTED BY PUBG or BGMI Official.\n 5. ATLEAST ONE OF YOUR TEAM MEMBER OWNS A BGMI YOUTUBE CHANNEL WITH < 20k SUBS", color=0x66d9ff)
        try:
          await message.author.create_dm()
          await message.author.dm_channel.send(embed =  embed)
          await message.reply("**Read Requirements be carefully in your DM **")
        except:
          await message.reply(f"I couldn't dm you! \nMake sure you dms are open.")

      if "t1waittime" in x or "t1wait" in x and message.channel.id == 857501729213120531:
        
        embedVar = discord.Embed(title="Tier 1 Normal Waiting time", description="**Real Esports** always welcome you in Tier 1 Normally waiting time is   **2 Day** but at present time **8 of teams are in Queue** so it may take at least **10 to 15 days.** When we reach to Your team we will contact you ourselves. You will get a **DM** on behalf of tier 1 the bot of Real Esports will be alert you in your dm \nOtherwise you can contact to [Admin](https://discord.com/channels/565508242843631616/842458727416332308/848775392331956244)", color=0x00ff00)
        await message.channel.send(embed=embedVar)

        

def setup(client):
    client.add_cog(other(client))
