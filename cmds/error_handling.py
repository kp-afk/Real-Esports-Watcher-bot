from discord.ext import commands

class error_handling(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("Sorry, You can't use this command!")
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send('Command does not exist.')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You Don't have the correct Permission")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please enter all required Arguments")
        elif isinstance(error, commands.TooManyArguments):
            await ctx.send("Please Enter arguments properly, \n Too many arguments have been given.")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send("Bot is missing permissions.")
        elif isinstance(error, commands.MissingRole):
            await ctx.send("Sorry, You can't use this command!")
        elif isinstance(error, commands.UserNotFound):
            await ctx.send("User not found")
        elif isinstance(error, commands.MemberNotFound):
          await ctx.send("Member not found")
        

def setup(client):
    client.add_cog(error_handling(client))
