import discord
from discord.ext import commands

class bump(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 259200, commands.BucketType.user) #next 3days 
    async def bump(self, ctx):
        await ctx.send("Bump done")

    
    @bump.error
    async def bump_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
                cd = round(error.retry_after)
                hours = str(cd // 3600)
                minutes = str(cd % 60)
                embed=discord.Embed(title="bumps!!!", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0xFF5733)
                await ctx.send(embed=embed)
                await ctx.send(f"You have {hours} hours {minutes} minutes left")
                await ctx.send("if you are a premium user use the !bumpp command")
                #await ctx.send(f"{round(error.retry_after, 2)} seconds left")
    

async def setup(bot):
    await bot.add_cog(bump(bot))