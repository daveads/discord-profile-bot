import asyncio
import discord

from core import embed
from model import queries
from view.modal.profile_modal import Creatprofile

# Class initialized
user_in_db = queries.PROFILEque()
user_embed = embed.Embed()




async def edit(bot, cooldown, interaction, button):

    #cooldown shit
    interaction.message.author = interaction.user
    bucket = cooldown.get_bucket(interaction.message)
    retry = bucket.update_rate_limit()

    dic_key = ['id','username','username_id','name','location','looking_for','hobbies','biography','age','profile_date']
        
    user = await bot.fetch_user(interaction.user.id)  
        
    if user_in_db.get_user(interaction.user.id):

        if retry:
            second = round(retry, 1)
            hours = retry // 3600
            minutes = hours * 60

            day = hours / 24
            await interaction.response.send_message(
                f"try again in {round(day)} Days {hours} hours {minutes} minutes, {second} seconds",
                ephemeral=True,
            )
        
        else:
            
            await interaction.response.defer()

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
            embed.add_field(name="(5) AGE", value=f"{user_data['age']}", inline=True)
            embed.add_field(name="(6) BIOGRAPHY", value=f"{user_data['biography']}", inline=True)
            embed.set_footer(text="profile can only be edited once a week",icon_url=interaction.user.avatar)
                
            try:
                await user.send(embed=embed)

            except:
                await interaction.response.send_message(embed=embed, ephemeral=True)
                # Testing a scenario

            #NOT SO GOOD 
            msg_timer=60
            while(True):
                try:
                    
                    def check(msg):
                        return msg.author == user and not msg.guild
                            
                    msg = await bot.wait_for("message", check=check, timeout=msg_timer)       
                                
                    #name
                    if msg.content == '1':
                        await user.send("what's your name ?")
                        await asyncio.sleep(2)
                        msg1 = await bot.wait_for("message", check=check, timeout=msg_timer)
                                
                        if msg1.content:
                            await user_embed.user_reply(user,"Name field updated")
                            user_in_db.update('name', msg1.content, user.id)
                            user_in_db.con.commit()
                            
                        else:
                            await user_embed.user_reply(user,"field can not be empty")
                        
                        
                    #location
                    elif msg.content == '2':
                        await user.send("where are you from ?")
                        await asyncio.sleep(2)
                        msg2 = await bot.wait_for("message", check=check, timeout=msg_timer)
                                
                        if msg2.content:
                            await user_embed.user_reply(user,"Location field updated")
                            user_in_db.update('location', msg2.content, user.id)
                            user_in_db.con.commit()
                        
                        else:
                            await user_embed.user_reply(user,"field can not be empty")


                        
                    #looking_for
                    elif msg.content ==  '3':
                        await user.send("What are you looking for? Type None if you don't want to share!")
                        await asyncio.sleep(2)
                        msg3 = await bot.wait_for("message", check=check, timeout=msg_timer)
                        
                        if msg3.content:
                            await user_embed.user_reply(user,"Looking_for field updated")
                            user_in_db.update('looking_for', msg3.content, user.id)
                            user_in_db.con.commit()
                            
                        else:
                            await user_embed.user_reply(user,"field can not be empty")

                    #hobbies
                    elif msg.content ==  '4':
                        await user.send("What are your hobbies?")
                        await asyncio.sleep(2)
                        msg4 = await bot.wait_for("message", check=check, timeout=msg_timer)
                            
                        if msg4.content:
                            await user_embed.user_reply(user,"hobbies field updated")
                            user_in_db.update('hobbies', msg4.content, user.id)
                            user_in_db.con.commit()

                        else:
                            await user_embed.user_reply(user,"field can not be empty")


                    #age
                    elif msg.content ==  '5':
                        await user.send("What's your age ?")
                        await asyncio.sleep(2)
                        msg5 = await bot.wait_for("message", check=check, timeout=msg_timer)
                            
                        if msg5.content:
                            await user_embed.user_reply(user,"Age field updated")
                            user_in_db.update('age', msg5.content, user.id)
                            user_in_db.con.commit()
                            
                        else:
                            await user_embed.user_reply(user,"field can not be empty")

                    #biography
                    elif msg.content ==  '6':
                        await user.send("Please write a biography, under 200 characters!")
                        await asyncio.sleep(2)
                        msg5 = await bot.wait_for("message", check=check, timeout=msg_timer)
                            
                        if msg5.content:
                            await user_embed.user_reply(user,"Biography field updated")
                            user_in_db.update('biography', msg5.content, user.id)
                            user_in_db.con.commit()
                            
                        else:
                            await user_embed.user_reply(user,"field can not be empty")



                    else:
                        await user.send("value can only in numbers above")
          
                except asyncio.TimeoutError:
                    break
                            

    else:
        try:
            await user_embed.user_reply(user,"YOU HAVE NO PROFILE TO EDIT")
            await interaction.response.defer()

        except:
            await interaction.response.send_message("YOU HAVE NO PROFILE TO EDIT", ephemeral=True)
            await asyncio.sleep(60)
            await interaction.delete_original_response()