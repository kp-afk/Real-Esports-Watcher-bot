import discord
from discord.ext import commands
import variables
import asyncio
from discord.utils import get

import os
import re
from cmds import utils

class admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def convert(self, ctx, *, member):
      try:
        member = int(member)
        member = ctx.guild.get_member(member)
      except:
        member = str(member)
        member = ctx.guild.get_member_named(member)
      await ctx.reply(member.mention)

    @commands.command()
    async def nub(self, ctx, m : discord.Member):
      await ctx.reply(m.roles)

      

        

          

 
  


    @commands.command()
    @commands.has_any_role(variables.botaccess1, variables.botaccess2,
                           variables.botaccess3, variables.botaccess4)
    async def listrolemembers(self, ctx, role : discord.Role):
      xlist = []
      for discord.Member in role.members:
        userid = discord.Member.id
        xstring = f"<@{userid}>"
        xlist.append(xstring)
      x = "\n".join(xlist)
      await ctx.send(x)

    @commands.command()
    @commands.has_any_role(variables.botaccess1, variables.botaccess2,
                           variables.botaccess3, variables.botaccess4)
    async def say(self, ctx, channel : discord.TextChannel, *, msg ):
      await channel.send(msg)
      try:
        await ctx.message.delete()
      except:
        pass




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

    

    # Massrole command
    @commands.command(description="Used to add a single role to a large number of users.")
    @commands.has_any_role(variables.botaccess1, variables.botaccess2,
                           variables.botaccess3, variables.botaccess4)
    async def massrole(self, ctx, arg1 , members: commands.Greedy[discord.Member]):
        i = discord.AllowedMentions(everyone = False, users=False)
        role = discord.utils.get(ctx.guild.roles, name=arg1)
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
      for discord.Role in roles:
        await user.remove_roles(discord.Role, atomic=True)
      await ctx.reply("Removed!")


    @commands.command()
    @commands.has_any_role(variables.botaccess1, variables.botaccess2,
                           variables.botaccess3, variables.botaccess4)
    async def addmentionrole(self, ctx, role , messageid):
      role = discord.utils.get(ctx.guild.roles, name=role)
      channel = ctx.message.channel
      x = await channel.fetch_message(messageid)
      mentions = x.mentions
      for discord.Member in mentions:
        try:
          await discord.Member.add_roles(role, atomic = True)
        except:
          await ctx.send(f"Couldn't add role to {discord.Member.mention}")
      y = len(mentions)
      await x.reply(f"Added Role - {role.name} to {y} Mentioned Members! ")

    @commands.command()
    @commands.has_any_role(variables.botaccess1, variables.botaccess2,
                           variables.botaccess3, variables.botaccess4)
    async def find(self, ctx,*, arg1):
      role = discord.utils.get(ctx.guild.roles, name=arg1)
      await ctx.reply(f" {role.mention} \n{role.id}")
      for discord.Member in role.members:
        await ctx.send(f"{discord.Member.name}\n{discord.Member.id}")


    

def setup(client):
    client.add_cog(admin(client))