from discord.ext import commands
from core import json_data


data = json_data.Datajson()

class Owner(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def check_if_it_is_me(ctx):   
        owner_bool = ctx.message.author.id in data.owner
        return owner_bool

    @commands.command()
    @commands.check(check_if_it_is_me)
    async def owner(self, ctx):
        await ctx.send("Bot owner")


async def setup(bot):
    await bot.add_cog(Owner(bot))
