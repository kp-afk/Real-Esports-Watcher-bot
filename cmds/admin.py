import discord
from discord.ext import commands
import variables
import asyncio

class admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Dm command
    @commands.command()
    @commands.has_any_role(variables.botaccess1, variables.botaccess2,
                           variables.botaccess3, variables.botaccess4)
    async def dm(self, ctx, user: discord.User, *, arg1):
        try:
            await user.create_dm()
            await user.dm_channel.send(arg1)
        except:
            await ctx.reply(content=f"Couldn't dm {user.mention}")
        else:
            await ctx.reply('DMd user successfully')

    """
    @commands.command()
    async def royal(self, ctx):
      await ctx.reply('https://tenor.com/view/sex-gif-19580480')
    """

    # Massrole command
    @commands.command(description="Used to add a single role to a large number of users.")
    @commands.has_any_role(variables.botaccess1, variables.botaccess2,
                           variables.botaccess3, variables.botaccess4)
    async def massrole(self, ctx, role : discord.Role, members: commands.Greedy[discord.Member]):
        i = discord.AllowedMentions(everyone = False, users=False)
        for discord.Member in members:
          try:
            await discord.Member.add_roles(role, reason=f"Massrole command by {ctx.message.author.name}", atomic=True)
            await ctx.send(content=f"Role added to {discord.Member.mention}", allowed_mentions=i)
          except:
            await ctx.send(content=f"Couldn't add role to {discord.Member.mention}", allowed_mentions=i)

    @commands.command()
    @commands.has_any_role(variables.botaccess1, variables.botaccess2,
                           variables.botaccess3, variables.botaccess4)
    async def removerole(self, ctx, user : discord.Member, roles: commands.Greedy[discord.Role]):
      await user.remove_roles(roles, atomic=True)
      await ctx.reply("Removed!")

    
        



def setup(client):
    client.add_cog(admin(client))