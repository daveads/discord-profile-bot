from discord.ext import commands
import discord

class bumpp(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.has_any_role('premium_p', 'admin')
    @commands.cooldown(1, 43200, commands.BucketType.user) #every 12hours 2times in a day
    async def bumpp(self, ctx):
        #print(ctx.author.roles)
        
        role = discord.utils.get(ctx.guild.roles, id=1026477250968834159)
        if role in ctx.author.roles:
            await ctx.send("you are a premium user, **bump**")
        else:
            await ctx.send("you are not verified")
            bumpp.reset_cooldown(ctx)

    @bumpp.error
    async def bumpp_error(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            await ctx.send("you are not a premium user")

        if isinstance(error, commands.CommandOnCooldown):
                cd = round(error.retry_after)
                hours = str(cd // 3600)
                minutes = str(cd % 60)
                embed=discord.Embed(title="bumps!!!", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0xFF5733)
                await ctx.send(embed=embed)
                await ctx.send(f"You have {hours} hours {minutes} minutes left")


async def setup(bot):
    await bot.add_cog(bumpp(bot))