from discord.ext import commands

class Eprofile(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 


    @commands.command()
    async def editp(self, ctx):

        await ctx.send("edit profile")


async def setup(bot):
    await bot.add_cog(Eprofile(bot))