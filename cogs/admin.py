import discord
from discord.ext import commands

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.command()
    @commands.has_role("admin")
    async def admin(self, ctx):
        await ctx.send("have an admin role")

    @admin.error
    async def admin_mod_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send("you are not an admin!")
    

    @commands.command()
    @commands.has_role("admin")
    async def kick(self, ctx, userName: discord.Member, reason="No reason provided"):
        user = await self.bot.fetch_user(ctx.author.id)
        await userName.kick(reason=reason)
        await user.send("yea works")


    @commands.command()
    async def god(self, ctx):
        print(ctx.author)
        print(ctx.author.id)

        if (ctx.author.id == 840152379122384896):
            await ctx.send("hello sir")
        
        
async def setup(bot):
    await bot.add_cog(Admin(bot))