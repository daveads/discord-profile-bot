import discord
from discord.ext import commands

class Addpremium(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #premium_p
    @commands.command()
    @commands.has_any_role('admin', 'moderator')
    async def addbumpp(self, ctx, user: discord.Member, role: discord.Role):
        #print(role.id)
        if ctx.author.id == 840152379122384896:
            await user.add_roles(role)
            await ctx.send(f"{user.name} has been giving a role called: {role.name}")
        else:
            if role.name == "premium_p":
                await user.add_roles(role)
                #await ctx.send("user is now a premium user")
                await ctx.send(f"{user.name} has been giving {role.name} role for profile bot access")
            else:
                await ctx.send("You are only allowed to give **premium_p** role with this bot")


    @addbumpp.error
    async def addbumpp_error(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            await ctx.send("only admin and moderator has the right to use this commands")

async def setup(bot):
    await bot.add_cog(Addpremium(bot))
