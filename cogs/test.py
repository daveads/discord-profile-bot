from discord.ext import commands
import discord
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

    @commands.command()
    async def check(self, ctx, user: discord.Member):
        #await ctx.message.delete()
        #await ctx.channel.send("My prefix")
        await ctx.reply('Hello!')
        await ctx.reply(user)

    
    @check.error
    async def check_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please pass all required arguments")
    

async def setup(bot):
    await bot.add_cog(Test(bot))
