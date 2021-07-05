import discord
from discord.ext import commands
import variables


class t3watch(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Add Prime 
    @commands.command(aliases=['addp', 'add'])
    @commands.has_any_role(variables.botaccess1, variables.botaccess2,
                           variables.botaccess3, variables.botaccess4)
    async def addprime(self, ctx, user: discord.Member, arg1, arg2, arg3):
        channel = ctx.guild.get_channel(variables.primeteam)
        membership = ctx.guild.get_role(variables.primerole)
        embed = discord.Embed(title=' Tier-3 Subscription added',
                              colour=0xff0000)
        embed.add_field(name=f'Team - **{arg1}**',
                        value='Added Prime Plan ',
                        inline=False)
        embed.add_field(name=f'Time', value=arg2, inline=False)
        embed.add_field(name=f'Valid Up to', value=arg3, inline=False)
        embed.add_field(name=f'Tag of Prime team',
                        value=user.mention,
                        inline=False)
        embed.set_footer(
            text='Copyright ©  2021 REAL Esports- All Rights Reserved.')
        await channel.send(embed=embed)
        try:
            await user.create_dm()
            await user.dm_channel.send(embed=embed)
        except:
            await ctx.send(f"Couldn't dm {user.mention}")
        rolereason = (
            f"added to prime teams by {{ctx.message.author.user.name}}")
        await user.add_roles(membership, reason=rolereason, atomic=True)
        await ctx.send(
            f'Team {arg1} added in Prime Team <a:safetik:781344436872675339> ')

    # REMOVE PRIME
    @commands.command(aliases=['removeprime', 'primeremove', 'removep'])
    @commands.has_any_role(variables.botaccess1, variables.botaccess2,
                           variables.botaccess3, variables.botaccess4)
    async def forceremoveprime(self, ctx, user: discord.Member):
        membership = ctx.guild.get_role(variables.primerole)
        if membership not in user.roles:
            await ctx.send(
                f"{{user.mention}} already does not have prime role!!")
        elif membership in user.roles:
            rolereason = (
                f"Removed using 'forceremoveprime' command by {ctx.message.author.user.name}"
            )
            await user.remove_roles(membership, reason=rolereason, atomic=True)
            try:
                await user.create_dm()
                await user.dm_channel.send(
                    "Real Esports Prime Team membership has been removed from you."
                )
            except:
                await ctx.send(f"Couldn't dm {user.mention}")
            await ctx.send(
                f"Prime team role successfully removed from {{user.mention}} ")


def setup(client):
    client.add_cog(t3watch(client))
