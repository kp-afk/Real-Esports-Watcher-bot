import discord
from discord.ext import commands
import variables
import asyncio


class other(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong! {round(self.client.latency * 1000)}ms')

    @commands.command()
    @commands.has_any_role(variables.botaccess1, variables.botaccess2,
                           variables.botaccess3, variables.botaccess4)
    async def help(self, ctx):

        helpembed = discord.Embed(title="Watcher Bot Command Categories:",
                                  color=0xff0000)
        helpembed.add_field(
            name="T3",
            value=
            f"addprime `<user>` `<team_name>` `<timings>` `<expire_date>` \n removeprime `<user>`",
            inline=False)
        helpembed.add_field(
            name="T2",
            value=
            f"accept `<user>` `<team_name>` \n reject `<user>` `<team_name>` `<reason>` \n t2transfer `<oldowner>` `<newowner>` `<team_name>` \n checkdm `<user>` \n proofsent `<user>` ",
            inline=False)
        helpembed.add_field(
            name="PMSL",
            value=
            f"pmslaccept `<user>` `<team_name>` \n pmslreject `<team_name>` `<reason>` \n pmslalert `<user>`",
            inline=False)
        helpembed.add_field(name="Others",
                            value=f"ping \ndm `<user>` `<message>`",
                            inline=False)
        await ctx.send(embed=helpembed)


    @commands.command()
    @commands.has_any_role(variables.botaccess1, variables.botaccess2,
                           variables.botaccess3, variables.botaccess4)
    async def dm(self, ctx, user: discord.User, *, arg1):
        i = discord.AllowedMentions(everyone = False, users=False)
        try:
            await user.create_dm()
            await user.dm_channel.send(arg1)
        except:
            await ctx.send(content=f"Couldn't dm {user.mention}", allowed_mentions=i)
        else:
            await ctx.send('DMd user successfully')
        
    @commands.command(description="Used to add Roles to a large number of users.")
    @commands.has_guild_permissions(ban_members=True)
    async def massrole(self, ctx, role : discord.Role, *argv : discord.Member):
        i = discord.AllowedMentions(everyone = False, users=False)
        for arg in argv:
          try:
            await arg.add_roles(role, reason=f"Massrole command by {ctx.message.author.name}", atomic=True)
            await ctx.send(content=f"Role added to {arg.mention}", allowed_mentions=i)
          except:
            await ctx.send(content=f"Couldn't add role to {arg.mention}", allowed_mentions=i)

    @commands.command()
    async def reju(self, ctx):
      
      await ctx.send(content=f"U r Noob {ctx.message.author.mention}", allowed_mentions = allowed_mentions) 
    

      






def setup(client):
    client.add_cog(other(client))
