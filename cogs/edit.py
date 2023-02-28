import asyncio
from email import message
from typing import Optional
from discord.ext import commands
import discord
from discord import app_commands 
from model import queries
from core.profile_data import profile_embed

user_in_db = queries.PROFILEque()

class Edit(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    # /slash command


    def cooldown_for_everyone_but_me(interaction: discord.Interaction) -> Optional[app_commands.Cooldown]:
        if interaction.user.id == 840152379122384896:
            return None
        
        return app_commands.Cooldown(1, 259200) #3 days 

    """
    @commands.Cog.listener()
    async def on_message(self, message):
        print(message.content)
    """
        

    @app_commands.checks.dynamic_cooldown(cooldown_for_everyone_but_me)
    @app_commands.command(name="edit", description="edit profile")
    async def edit(self, interaction: discord.Interaction):
        """ /edit """

        dic_key = ['id','username','username_id','name','location','looking_for','hobbies','biography','premium_day','profile_date']
     
        user = await self.bot.fetch_user(interaction.user.id)  


    


        async def user_reply(user, bot, chh):
            def check(message):
                return message.author == user and bool(message.content)
            
                    
            try:
                resp = await bot.wait_for('message', check=check , timeout=65.0)


            except  asyncio.TimeoutError:
                await chh.send(f"Time out {user.mention}")
                await asyncio.sleep(20)
                
                    
     
            return resp


        if user_in_db.get_user(interaction.user.id):

            user_d = user_in_db.get_user(interaction.user.id)
            user_data ={}
                
            for i in range(len(dic_key)):
                user_data[dic_key[i]] = user_d[i]


            embed=discord.Embed(title=f"PROFILE `{interaction.user}`",  description="Type in a number to edit a particular field \n *Default* `Timeout: 1mins` ", color=discord.Color.blue())
            #embed.set_image(url=(author.avatar_url))
            embed.set_thumbnail(url=interaction.user.avatar)
            embed.add_field(name="(1) NAME ", value=f"{user_data['name']}", inline=True)
            embed.add_field(name="(2) LOCATION", value=f"{user_data['location']}", inline=True)
            embed.add_field(name="(3) LOOKING FOR", value=f"{user_data['looking_for']}", inline=True)
            embed.add_field(name="(4) HOBBIES", value=f"{user_data['hobbies']}",inline=True)
            embed.add_field(name="(5) BIOGRAPHY", value=f"{user_data['biography']}", inline=True)
            embed.set_footer(text="profile can only be edited once a week",icon_url=interaction.user.avatar)
            

            await interaction.response.send_message(embed=embed, ephemeral=True)


            #NOT SO GOOD 
            msg_timer=60
            while(True):
                try:
                    
                    def check(msg):
                        return msg.author == user and msg.channel
                    

                    msg = await self.bot.wait_for("message", check=check, timeout=msg_timer)
                    

                    #Name
                    if msg.content == '1':
                        await msg.delete()
                        await interaction.followup.send('what your name', ephemeral=True)
                        await asyncio.sleep(2)
                        msg1 = await self.bot.wait_for("message", check=check, timeout=msg_timer)

                        if msg1.content:
                            await msg1.delete()
                            await interaction.followup.send("Name field updated", ephemeral=True)
                            user_in_db.update('name', msg1.content, user.id)
                            user_in_db.con.commit()
                            
                        else:
                            await interaction.followup.send("Field can not be empty", ephemeral=True)
                        
                        
                    #location
                    elif msg.content == '2':
                        await msg.delete()
                        await interaction.followup.send("where are you from ?", ephemeral=True)
                        await asyncio.sleep(2)
                        msg2 = await self.bot.wait_for("message", check=check, timeout=msg_timer)


                        if msg2.content:
                            await msg2.delete()
                            await interaction.followup.send("Location Field updated", ephemeral=True)
                            user_in_db.update('location', msg2.content, user.id)
                            user_in_db.con.commit()
                        
                        else:
                            await interaction.followup.send("Field can not be empty", ephemeral=True)


                        
                    #looking_for
                    elif msg.content ==  '3':
                        await msg.delete()
                        await interaction.followup.send("What are you looking for? Type None if you don't want to share!", ephemeral=True)
                        await asyncio.sleep(2)
                        msg3 = await self.bot.wait_for("message", check=check, timeout=msg_timer)
                        
                        if msg3.content:
                            await msg3.delete()
                            await interaction.followup.send("Looking_for field updated", ephemeral=True)
                            user_in_db.update('looking_for', msg1.content, user.id)
                            user_in_db.con.commit()
                            
                        else:
                            await interaction.followup.send("Field can not be empty", ephemeral=True)

                    #hobbies
                    elif msg.content ==  '4':
                        await msg.delete()
                        await interaction.followup.send("What are your hobbies?", ephemeral=True)
                        await asyncio.sleep(2)
                        msg4 = await self.bot.wait_for("message", check=check, timeout=msg_timer)

                        if msg4.content:
                            await msg4.delete()
                            await interaction.followup.send("hobbies field updated", ephemeral=True)
                            user_in_db.update('hobbies', msg4.content, user.id)
                            user_in_db.con.commit()
                        else:
                            await interaction.followup.send("Field can not be empty", ephemeral=True)

                    #biography
                    elif msg.content ==  '5':
                        await msg.delete()
                        await interaction.followup.send("Please write a biography, under 200 characters!", ephemeral=True)
                        await asyncio.sleep(2)
                        msg5 = await self.bot.wait_for("message", check=check, timeout=msg_timer)
                            
                        if msg5.content:
                            await msg5.delete()
                            await interaction.followup.send("Biography field updated", ephemeral=True)
                            user_in_db.update('biography', msg1.content, user.id)
                            user_in_db.con.commit()
                            
                        else:
                            await interaction.followup.send("Field can not be empty", ephemeral=True)



                    else:
                        await msg.delete()
                        await interaction.followup.send("value can only in numbers above", ephemeral=True)
          
                except asyncio.TimeoutError:
                    break

        else:
            await interaction.response.send_message("YOU HAVE NO PROFILE TO EDIT", ephemeral=True)
            #await interaction.response.defer()

    @edit.error
    async def on_test_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(str(error), ephemeral=True)
            #app_commands.AppCommandError
            #app_commands.CommandInvokeError




async def setup(bot):
    await bot.add_cog(Edit(bot))