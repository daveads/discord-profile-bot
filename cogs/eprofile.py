import asyncio
import discord
from discord.ext import commands
from model import queries

update_user = queries.PROFILEque()

class Eprofile(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 


    @commands.command()
    @commands.cooldown(1, 604800, commands.BucketType.user) #once a week for everyone 
    async def editp(self, ctx):
        dic_key = ['id','username','username_id','name','location','height','dating_status','looking_for','hobbies','biography','premium_day','profile_date']
        user_d = update_user.get_user(ctx.author.id)
        user_data ={}

        for i in range(len(dic_key)):
            user_data[dic_key[i]] = user_d[i]       
        
        print(user_data)


        embed=discord.Embed(title="PROFILE", url="", description="Type in a number to edit a particular field", color=discord.Color.blue())
        #embed.set_image(url=(author.avatar_url))
        embed.set_thumbnail(url=ctx.author.avatar)
        embed.add_field(name="(1) NAME ", value=f"{user_data['name']}", inline=True)
        embed.add_field(name="(2) LOCATION", value=f"{user_data['location']}", inline=True)
        embed.add_field(name="(3) HEIGHT", value=f"{user_data['height']}", inline=True)
        embed.add_field(name="(4) DATING STATUS", value=f"{user_data['dating_status']}", inline=True)
        embed.add_field(name="(5) LOOKING FOR", value=f"{user_data['looking_for']}", inline=True)
        embed.add_field(name="(6) HOBBIES", value=f"{user_data['hobbies']}",inline=True)
        embed.add_field(name="(7) BIOGRAPHY", value=f"{user_data['biography']}", inline=True)
        embed.set_footer(text="profile can only be edited once a week",icon_url=ctx.author.avatar)
        await ctx.send(embed=embed)
        

        #NOT SO GOOD 
        msg_timer=60
        while(True):
            
            try:
                msg = await self.bot.wait_for("message", timeout=msg_timer)       
                   #name
                if msg.content == '1':
                    await ctx.send("what's your name ?")
                    await asyncio.sleep(2)
                    msg1 = await self.bot.wait_for("message", timeout=msg_timer)
                    await ctx.send(msg1.content)
                    update_user.update('name', msg1.content, ctx.author.id)
                
                     #location
                elif msg.content == '2':
                    await ctx.send("where are you from ?")
                    await asyncio.sleep(2)
                    msg1 = await self.bot.wait_for("message", timeout=msg_timer)
                    await ctx.send(msg1.content)
                    update_user.update('location', msg1.content, ctx.author.id)
                
                    #height
                elif msg.content == '3':
                    await ctx.send("How tall are you? ")
                    await asyncio.sleep(2)
                    msg1 = await self.bot.wait_for("message", timeout=msg_timer)
                    await ctx.send(msg1.content)
                    update_user.update('height', msg1.content, ctx.author.id)

                    #status
                elif msg.content ==  '4':
                    await ctx.send("Briefly say your dating status! ")
                    await asyncio.sleep(2)
                    msg1 = await self.bot.wait_for("message", timeout=msg_timer)
                    await ctx.send(msg1.content)
                    update_user.update('dating_status', msg1.content, ctx.author.id)
                
                    #looking_for
                elif msg.content ==  '5':
                    await ctx.send("What are you looking for? Type None if you don't want to share!")
                    await asyncio.sleep(2)
                    msg1 = await self.bot.wait_for("message", timeout=msg_timer)
                    await ctx.send(msg1.content)
                    update_user.update('looking_for', msg1.content, ctx.author.id)

                    #hobbies
                elif msg.content ==  '6':
                    await ctx.send("What are your hobbies?")
                    await asyncio.sleep(2)
                    msg1 = await self.bot.wait_for("message", timeout=msg_timer)
                    await ctx.send(msg1.content)
                    update_user.update('hobbies', msg1.content, ctx.author.id)

                    #biography
                elif msg.content ==  '7':
                    await ctx.send("Please write a biography, under 200 characters!")
                    await asyncio.sleep(2)
                    msg1 = await self.bot.wait_for("message", timeout=msg_timer)
                    await ctx.send(msg1.content)
                    update_user.update('biography', msg1.content, ctx.author.id)


                elif msg.content.lower() == "done":
                    
                    await ctx.send("data saved")
                    user_d = update_user.get_user(ctx.author.id)
            
                    # shadowing is possible easily here lol
                    user_data ={}
                    for i in range(len(dic_key)):
                        user_data[dic_key[i]] = user_d[i] 

                    Uembed=discord.Embed(title="PROFILE UPDATED!!!", url="", description="Type !help to check out full commands", color=discord.Color.blue())
                    Uembed.set_thumbnail(url=ctx.author.avatar)
                    Uembed.add_field(name="(1) NAME ", value=f"{user_data['name']}", inline=True)
                    Uembed.add_field(name="(2) LOCATION", value=f"{user_data['location']}", inline=True)
                    Uembed.add_field(name="(3) HEIGHT", value=f"{user_data['height']}", inline=True)
                    Uembed.add_field(name="(4) DATING STATUS", value=f"{user_data['dating_status']}", inline=True)
                    Uembed.add_field(name="(5) LOOKING FOR", value=f"{user_data['looking_for']}", inline=True)
                    Uembed.add_field(name="(6) HOBBIES", value=f"{user_data['hobbies']}",inline=True)
                    Uembed.add_field(name="(7) BIOGRAPHY", value=f"{user_data['biography']}", inline=True)
                    Uembed.set_footer(text="profile can only be edited once a week",icon_url=ctx.author.avatar)
                    await ctx.send(embed=Uembed)

                    update_user.con.commit()
                    update_user.con.close()
                    break

                elif msg.content.lower() == "exit":
                    await ctx.send("cancelled")
                    break
                
                else:
                    await ctx.send("value can only in numbers above")
          

                

            except asyncio.TimeoutError: #test
                    await ctx.send("Time out")
                    await ctx.send("You were too slow to answer!")
                    break                

   
    @editp.error
    async def bump_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
                cd = round(error.retry_after)
                hours = str(cd // 3600)
                minutes = str(cd % 60)
                await ctx.send(f"You have {hours} hours {minutes} minutes left")
                await ctx.send("you can only edit your profile once a week")
                #await ctx.send(f"{round(error.retry_after, 2)} seconds left")

async def setup(bot):
    await bot.add_cog(Eprofile(bot))