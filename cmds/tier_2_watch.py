import discord
from discord.ext import commands
import variables


class t2watch(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=[
        'accepted',
        'yes',
        'valid',
    ])
    @commands.has_any_role(variables.botaccess1, variables.botaccess2,
                           variables.botaccess3, variables.botaccess4)
    async def accept(self, ctx, user: discord.Member, *, arg1):

        tier2role = ctx.guild.get_role(variables.tier_2_role_id)
        channel = ctx.guild.get_channel(variables.tier_2_logs_channel_id)
        embed = discord.Embed(title=' Tier-2 Team Confirmation',
                              colour=0x00ff00)
        embed.add_field(name=f'Team - **{arg1}**',
                        value=f'Accepted in Tier-2 \n{user.mention}',
                        inline=False)
        embed.set_footer(
            text='Copyright ©  2021 REAL Esports- All Rights Reserved.')
        await channel.send(embed=embed)
        try:
            await user.create_dm()
            await user.dm_channel.send(embed=embed)
        except:
            await ctx.send(f"Couldn't dm {user.mention}")
        t2role = discord.utils.find(lambda r: r.id == variables.tier_2_role_id,
                                    ctx.message.guild.roles)
        if t2role not in user.roles:
            await ctx.send(f'Team {arg1} accepted Successfully!')
            await user.add_roles(tier2role, reason=f"accept command by {ctx.message.author.name}", atomic=True)
            await ctx.send(f'Role added successfully! to {user.mention}')
        elif t2role in user.roles:
            await ctx.send(
                f'Warning! user already has tier-2 role \n Team {arg1} accepted Successfully!'
            )

            await ctx.send(f'Role added successfully! to {user.mention}')

    @commands.command(aliases=['rejected', 'deny', 'no', 'invalid'])
    @commands.has_any_role(variables.botaccess1, variables.botaccess2,
                           variables.botaccess3, variables.botaccess4)
    async def reject(self, ctx, user: discord.Member, arg1, *, arg2):

        channel = ctx.guild.get_channel(variables.tier_2_logs_channel_id)
        tier2role = ctx.guild.get_role(variables.tier_2_role_id)
        embed = discord.Embed(title=' Tier-2 Team Confirmation',
                              colour=0xff0000)
        embed.add_field(name=f'Team - **{arg1}**',
                        value=f'Rejected in Tier-2 \n{user.mention}',
                        inline=False)
        embed.add_field(name=f'Reason', value=arg2, inline=True)
        embed.add_field(
            name=f'Reapply',
            value=
            ('To Resubmit Application [Clickhere!](https://docs.google.com/forms/d/1Qdyo0xSw5XKdkBlwiFYu0gdOrUkId0ZhFRVW44v3WHU/edit?usp=forms_home&ths=true)'
             ),
            inline=False)
        embed.set_footer(
            text='Copyright ©  2021 REAL Esports- All Rights Reserved.')

        await channel.send(embed=embed)
        try:
            await user.create_dm()
            await user.dm_channel.send(embed=embed)
        except:
            await ctx.send(f"Couldn't dm {user.mention}")
        await user.remove_roles(tier2role, atomic=True)
        await ctx.send(f'Team {arg1} rejected Successfully!')

    @commands.command(aliases=['give', 'new', 't2transfer'])
    @commands.has_any_role(variables.botaccess1, variables.botaccess2,
                           variables.botaccess3, variables.botaccess4)
    async def transfer(self, ctx, user: discord.Member,
                       newuser: discord.Member, *, arg1):
        tier2role = ctx.guild.get_role(variables.tier_2_role_id)
        await user.remove_roles(tier2role, reason=f'transfer command by {ctx.message.author.name}', atomic=True)
        if tier2role not in newuser.roles and tier2role in user.roles:
            await newuser.add_roles(tier2role, reason=f"transfer command by {ctx.message.author.name}", atomic=True)
            await ctx.send(f'Ownership transferred successfully')
            try:
                await user.create_dm()
                await user.dm_channel.send(
                    f'You are no longer the owner of team : {arg1} For Tier 2')
            except:
                await ctx.send(f"Couldn't dm {user.mention}")
            try:
                await newuser.create_dm()
                await newuser.dm_channel.send(
                    f'You Are Owner Team {arg1} For Tier 2')
            except:
                await ctx.send(f"Couldn't dm {newuser.mention}")
        elif tier2role not in newuser.roles and tier2role not in user.roles:
            await ctx.send(f'Both Users Do not have Tier-2 role')
        elif tier2role in newuser.roles and tier2role not in user.roles:
            await ctx.send('newuser is already owner and has tier-2 role')

    @commands.command(aliases=[
        'alert1',
        'email',
        'checkmail',
    ])
    @commands.has_any_role(variables.botaccess1, variables.botaccess2,
                           variables.botaccess3, variables.botaccess4)
    async def checkdm(self, ctx, user: discord.User):
        embed = discord.Embed(title=' Real Esports Tier-2 ', colour=0x29e6ff)
        embed.add_field(
            name=f'Real Esports Tier-2 Application',
            value='Check Your Email Inbox Regarding Tier-2 Application ',
            inline=False)
        embed.set_footer(
            text='Copyright ©  2021 REAL Esports- All Rights Reserved.')
        try:
            await user.create_dm()
            await user.dm_channel.send(embed=embed)
        except:
            await ctx.send(f"Couldn't dm {user.mention}")
        else:
            await ctx.send(f'Alert sent to {user.mention}')

    @commands.command(aliases=['proofsent', 'alert2'])
    @commands.has_any_role(variables.botaccess1, variables.botaccess2,
                           variables.botaccess3, variables.botaccess4)
    async def verifying(self, ctx, user: discord.User):

        embed = discord.Embed(title=' Real Esports Tier-2 ', colour=0x29e6ff)
        embed.add_field(
            name=f'Wait for 2 to 3 days',
            value='Staff is verifying your data, wait for next response',
            inline=False)
        embed.set_footer(
            text='Copyright ©  2021 REAL Esports- All Rights Reserved.')
        try:
            await user.create_dm()
            await user.dm_channel.send(embed=embed)
        except:
            await ctx.send(f"Couldn't dm {user.mention}")
        else:
            await ctx.send(f'alert sent! to {user.mention}')


def setup(client):
    client.add_cog(t2watch(client))
