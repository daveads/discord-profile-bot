from discord.ext import commands

class Owner(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def check_if_it_is_me(ctx):
        return ctx.message.author.id == 840152379122384896

    @commands.command()
    @commands.check(check_if_it_is_me)
    async def owner(self, ctx):
        await ctx.send("Bot owner")


async def setup(bot):
    await bot.add_cog(Owner(bot))
