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
            name="Moderation",
            value=
            f"ban `<user>` `<optional_reason>` \n unban `<user>` `<optional_reason>` \n kick `<user>` `<optional_reason>`",
            inline=False)
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
        try:
            await user.create_dm()
            await user.dm_channel.send(arg1)
        except:
            await ctx.send(f"Couldn't dm {user.mention}")
        else:
            await ctx.send('DMd user successfully')


def setup(client):
    client.add_cog(other(client))
