import discord
from discord.ext import commands
import variables
import random


class pmsl(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(
        aliases=['pmslyes', 'pmslaccept', 'apmsl'], )
    @commands.has_any_role(variables.botaccess1, variables.botaccess2,
                           variables.botaccess3, variables.botaccess4)
    async def pmsla(self, ctx, user: discord.Member, *, arg1):

        emoteslist = ["<a:yessad:738983674242007140> ",
                      "<a:verify:742940239403941930> ",
                      "<a:verifykr:763258119169900574> ",
                      "<:ATD_vortexScam:801698916373495819> ",
                      "<a:tik:746576569652346890> ",
                      "<a:emoji_7:790546540217237514> ",
                      "<a:safetik:781344436872675339> ",
                      "<a:brxpurple:836960052358676480>",
                      "<a:op16:789552412260171777> ",
                      "<a:yhh:743698122362060810> " ]
        random_emote = random.choice(emoteslist)
        pmslrole = ctx.guild.get_role(variables.pmsl_confirmrole)
        channel = ctx.guild.get_channel(variables.pmsl_logs)
        embed = discord.Embed(title=' PMSL Team Confirmation', colour=0x00ff00)
        embed.add_field(name=f'Team - **{arg1}**',
                        value=f'PMSL *Accepted* {random_emote} \n{user.mention}',
                        inline=False)
        embed.set_footer(
            text='Copyright ©  2021 REAL Esports- All Rights Reserved.')
        await channel.send(embed=embed)
        try:
            await user.create_dm()
            await user.dm_channel.send(embed=embed)
            await ctx.send(f'Team {arg1} accepted in PMSL <a:verifykr:763258119169900574> ')
        except:
            await ctx.send(f"Couldn't dm {user.mention} <a:warn:789554164731478108> ")
        await user.add_roles(
            pmslrole,
            reason=f"pmsla command by {ctx.message.author.name}",
            atomic=True)
        await ctx.send(f'Role added to {user.mention} <a:whitemusic:789550966776528977> ')

    @commands.command(
        aliases=['pmslreject'], )
    @commands.has_any_role(variables.botaccess1, variables.botaccess2,
                           variables.botaccess3, variables.botaccess4)
    async def pmslr(self, ctx, user: discord.Member, arg1, *, arg2):

        channel = ctx.guild.get_channel(variables.pmsl_logs)
        pmslrole = ctx.guild.get_role(variables.pmsl_confirmrole)
        embeduser = discord.Embed(title=' PMSL Confirmation', colour=0xff0000)
        embeduser.add_field(name=f'Team - **{arg1}**',
                            value='Rejected in PMSL ',
                            inline=False)
        embeduser.add_field(name=f'Reason', value=arg2, inline=True)
        embeduser.add_field(
            name=f'Reapply',
            value=
            ('To Resubmit Application [Clickhere!](https://forms.gle/yx1mp5QWHxYSs8DJ7)'
             ),
            inline=False)
        embeduser.set_footer(
            text='Copyright ©  2021 REAL Esports- All Rights Reserved.')
        embedlogs = discord.Embed(title=' PMSL Confirmation', colour=0xff0000)
        embedlogs.add_field(name=f'Team - **{arg1}**',
                            value='Rejected in PMSL ',
                            inline=False)
        embedlogs.set_footer(
            text='Copyright ©  2021 REAL Esports- All Rights Reserved.')
        await channel.send(embed=embedlogs)
        try:
            await user.create_dm()
            await user.dm_channel.send(embed=embeduser)
        except:
            await ctx.send(f"Couldn't dm {user.mention}")
        await user.remove_roles(
            pmslrole,
            reason=f"pmslreject command by {ctx.message.author.name}",
            atomic=True)
        await ctx.send(f'Team {arg1} rejected Successfully!')

    @commands.command()
    @commands.has_any_role(variables.botaccess1, variables.botaccess2,
                           variables.botaccess3, variables.botaccess4)
    async def pmslalert(self, ctx, user: discord.User):
        embed = discord.Embed(title=' Real Esports PMSL Confirmation ',
                              colour=0x29e6ff)
        embed.add_field(
            name=f'Real Esports PMSL Application',
            value=
            'Staff is reviewing your registration for PMSL wait if you can join vc then join <#827380944532668456>',
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


def setup(client):
    client.add_cog(pmsl(client))
