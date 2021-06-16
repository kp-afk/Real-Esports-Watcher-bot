import discord
from discord.ext import commands


class moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        toproleauthor = ctx.message.author.top_role
        toprolemember = member.top_role

        if toproleauthor >= toprolemember and ctx.message.author != member:

            await member.kick(reason=reason)
            await ctx.send(f'Member{member.mention} Kicked')

        else:
            ctx.send("You can't kick this member")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        toproleauthor = ctx.message.author.top_role
        toprolemember = member.top_role

        if toproleauthor > toprolemember and ctx.message.author != member:

            ban_embed = discord.Embed(title=' MODERATION ACTION NOTICE',
                                      colour=0xff0000)

            ban_embed.add_field(name=f'{member.mention} YOU HAVE BEEN BANNED',
                                value='Reason : {arg1} ',
                                inline=False)
            ban_embed.add_field(
                name=f'Reapply',
                value=
                ('To appeal the ban  [Clickhere](https://docs.google.com/forms/d/e/1FAIpQLScGnpgjzNO2neFsolAR-94L2YTW_y5lHkp6RB9VOHsVgvn7oQ/viewform)'
                 ),
                inline=False)
            ban_embed.set_footer(
                text='Copyright ©  2021 REAL Esports- All Rights Reserved.')
            banreason = (f'Banned by {ctx.message.author} for {reason}')
            await member.ban(reason=banreason)
            try:
                await member.create_dm()
                await member.dm_channel.send(embed=ban_embed)
            except:
                await ctx.send(f"Couldn't dm {member.mention}")
            await ctx.send(f'{member.mention} Banned! for {reason}')
        elif ctx.message.author == member:
            await ctx.send("You can't ban yourself!")
        elif toproleauthor == toprolemember:
            await ctx.send("That user has the same role as you!")
        elif toproleauthor < toprolemember:
            await ctx.send("That user's role is higher than you!")

        else:
            ctx.send("Error")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user: discord.User):

        await ctx.guild.unban(user)
        await ctx.send(f'Member{user.mention} Unbanned')


def setup(client):
    client.add_cog(moderation(client))
