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
        await ctx.channel.purge(limit=1)
        if ctx.channel.id == data.profile_channel:
    
            user = await self.bot.fetch_user(ctx.author.id)
            print("user roles ",user)

            # Check premium Users         
            role = discord.utils.get(ctx.guild.roles, id=data.premium_role)
            if role in ctx.author.roles:
                
                await user.send("premium user should use the !bumpp commands")
                ctx.command.reset_cooldown(ctx)
                
            else:
                print(ctx.author.id)
                print("json", data.male_role)
                print("json", data.female_role)

                if user_in_db.get_user(ctx.author.id): #user_in:
                    
                    dic_key = ['id','username','username_id','name','location','height','dating_status','looking_for','hobbies','biography','premium_day','profile_date']
                    user_d = user_in_db.get_user(ctx.author.id)
                    user_data ={}
                    for i in range(len(dic_key)):
                        user_data[dic_key[i]] = user_d[i] 

                    print(user_data)

                    male = discord.utils.get(ctx.guild.roles, id=data.male_role)
                    female = discord.utils.get(ctx.guild.roles, id=data.female_role)

                    if male in ctx.author.roles:
                        channel = self.bot.get_channel(data.male_channel)
                        print("male")
                        print(ctx.author.roles)
                    elif female in ctx.author.roles:
                        channel = self.bot.get_channel(data.female_channel)
                    else:
                        user.send("you need a role to bump")

                    """
                    Embed 
                    """
                    await channel.send(f"{ctx.author.mention}")
                    embed=discord.Embed(title=f"User: <@{user.id}>", url="", description="", color=discord.Color.red())
                    #if True:
                    #=embed.set_image(url=(ctx.author.avatar))
                   
                    embed.set_thumbnail(url=user.avatar)
                    embed.set_author(name=f"{user}", icon_url=(user.avatar))
                    embed.add_field(name="Name", value=f"{user_data['name']}", inline=True)
                    
                    
                    embed.add_field(name="Age", value=f"24", inline=True)

                    if male in ctx.author.roles:
                        embed.add_field(name="Gender", value=f"{male}", inline=True)
                    
                    elif female in ctx.author.roles:
                        embed.add_field(name="Gender", value=f"{female}", inline=True)


                    embed.add_field(name="Orientation", value=f"Straight", inline=True)
                    embed.add_field(name="Location", value=f"{user_data['location']}", inline=True)
                    embed.add_field(name="Dating status", value=f"{user_data['dating_status']}", inline=True)
                    embed.add_field(name="Height", value=f"{user_data['height']}", inline=True)

                    embed.add_field(name="DMs status", value=f"dm status", inline=True)
                    embed.add_field(name="Verification level", value=f"Not verified", inline=True)

                    embed.add_field(name="Looking for ", value=f"{user_data['looking_for']}", inline=False)
                    embed.add_field(name="Hobbies ", value=f"{user_data['hobbies']}", inline=False)
                    embed.add_field(name="About me ", value=f"{user_data['biography']}", inline=False)

                    embed.set_footer(text=f"{ctx.guild.name}", icon_url=ctx.guild.icon.url)
                    await channel.send(embed=embed)
                    
                    
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