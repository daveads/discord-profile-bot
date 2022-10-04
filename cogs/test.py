from discord.ext import commands

class Test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.message.delete()
        msg = await ctx.send("pong")
        #message = await ctx.send('test')
        yes_thumb = '👍'
        no_thumb = "👎"
        await msg.add_reaction(yes_thumb)
        await msg.add_reaction(no_thumb)


async def setup(bot):
    await bot.add_cog(Test(bot))
