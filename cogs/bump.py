import discord
from discord.ext import commands

#json data
from core import configs
from model import queries


# class initialized
data = configs.Datajson()
user_in_db = queries.PROFILEque()

class bump(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.command()
    @commands.cooldown(1, 259200, commands.BucketType.user) #next 3days 
    async def bump(self, ctx):
        
        if ctx.channel.id == data.profile_channel:


            # Check premium Users         
            role = discord.utils.get(ctx.guild.roles, id=data.premium_role)
            if role in ctx.author.roles:
                
                await ctx.send("premium user should use the !bumpp commands")
                ctx.command.reset_cooldown(ctx)
                
            else:

                if user_in_db.get_user(ctx.author.id): #user_in:
                    channel = self.bot.get_channel(data.male_channel)
                    await channel.send(f"Bump done {ctx.author.mention}")
                    
                    """
                    bump data

                    // discord data
                    * About me == biography
                    * Gender
                    * DMs status
                    * Verification level
                    * Orientation = sexual orientation
                    * Age


                    """


                else:
                    await ctx.send("you don't have a profile")
                    ctx.command.reset_cooldown(ctx)


        else:
            await ctx.send("command can only be used in the profile_command channel")
            ctx.command.reset_cooldown(ctx)

        



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