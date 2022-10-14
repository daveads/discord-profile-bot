import asyncio
from discord.ext import commands
import discord

from model import queries
from core import configs
from core import embed

# class initialized
data = configs.Datajson()
user_in_db = queries.PROFILEque()
user_embed = embed.Embed()


class Viewprofile(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.dic_key = ['id','username','username_id','name','location','height','dating_status','looking_for','hobbies','biography','premium_day','profile_date']

    @commands.guild_only()
    @commands.command() 
    async def edit(self, ctx):
        await ctx.channel.purge(limit=1)

        #send msg in user dm
        user = await self.bot.fetch_user(ctx.author.id)

        if ctx.author.id == self.bot.user.id:
            return

        if ctx.channel.id == data.profile_channel:

            if user_in_db.get_user(ctx.author.id):
                
                user_d = user_in_db.get_user(ctx.author.id)
                user_data ={}

                for i in range(len(self.dic_key)):
                    user_data[self.dic_key[i]] = user_d[i]
                
                embed=discord.Embed(title=f"PROFILE `{ctx.author}`",  description="Type in a number to edit a particular field \n *Default* `Timeout: 1mins` ", color=discord.Color.blue())
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
                await user.send(embed=embed)

                #NOT SO GOOD 
                msg_timer=60
                while(True):

                    try:
                        def check(msg):
                            return msg.author == user
                      
                        msg = await self.bot.wait_for("message", check=check, timeout=msg_timer)       
                        #print(msg.author)
                        #print(user)
                          
                        #name
                        if msg.content == '1':
                            await user.send("what's your name ?")
                            await asyncio.sleep(2)
                            msg1 = await self.bot.wait_for("message", check=check, timeout=msg_timer)
                            
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
                            msg1 = await self.bot.wait_for("message", check=check, timeout=msg_timer)
                            
                            if msg1.content:
                                await user_embed.user_reply(user,"Location field updated")
                                user_in_db.update('location', msg1.content, user.id)
                                user_in_db.con.commit()
                            else:
                                await user_embed.user_reply(user,"field can not be empty")


                        #height
                        elif msg.content == '3':
                            await user.send("How tall are you? ")
                            await asyncio.sleep(2)
                            msg1 = await self.bot.wait_for("message", check=check, timeout=msg_timer)
                            if msg1.content:
                                await user_embed.user_reply(user,"Height field updated")
                                user_in_db.update('height', msg1.content, user.id)
                                user_in_db.con.commit()
                            else:
                                await user_embed.user_reply(user,"field can not be empty")
                            

                        #status
                        elif msg.content ==  '4':
                            await user.send("Briefly say your dating status! ")
                            await asyncio.sleep(2)
                            msg1 = await self.bot.wait_for("message", check=check, timeout=msg_timer)
                            if msg1.content:
                                await user_embed.user_reply(user,"Dating status field updated")
                                user_in_db.update('dating_status', msg1.content, user.id)
                                user_in_db.con.commit()
                            else:
                                await user_embed.user_reply(user,"field can not be empty")

                
                    
                        #looking_for
                        elif msg.content ==  '5':
                            await user.send("What are you looking for? Type None if you don't want to share!")
                            await asyncio.sleep(2)
                            msg1 = await self.bot.wait_for("message", check=check, timeout=msg_timer)
                            if msg1.content:
                                await user_embed.user_reply(user,"Looking_for field updated")
                                user_in_db.update('looking_for', msg1.content, user.id)
                                user_in_db.con.commit()
                            else:
                                await user_embed.user_reply(user,"field can not be empty")

                        #hobbies
                        elif msg.content ==  '6':
                            await user.send("What are your hobbies?")
                            await asyncio.sleep(2)
                            if msg1.content:
                                msg1 = await self.bot.wait_for("message", check=check, timeout=msg_timer)
                                user_in_db.update('hobbies', msg1.content, user.id)
                                user_in_db.con.commit()
                            else:
                                await user_embed.user_reply(user,"field can not be empty")

                        #biography
                        elif msg.content ==  '7':
                            await user.send("Please write a biography, under 200 characters!")
                            await asyncio.sleep(2)
                            msg1 = await self.bot.wait_for("message", check=check, timeout=msg_timer)
                            if msg1.content:
                                await user_embed.user_reply(user,"Biography field updated")
                                user_in_db.update('biography', msg1.content, user.id)
                                user_in_db.con.commit()
                            else:
                                await user_embed.user_reply(user,"field can not be empty")
                
                        
                        else:
                            await user.send("value can only in numbers above")
          
                    except asyncio.TimeoutError:
                        break

            else:
                await user.send("you don't have a profile")

        else:
            await user.send("command can only be used in the profile_command channel")






    @commands.Cog.listener()
    async def on_message(self, message):

        #bot only
        if message.author == self.bot.user:

            if message.content.startswith('!run'):
                channel = self.bot.get_channel(data.profile_channel)
                await channel.purge(limit=2000)

                await channel.send(file=discord.File('profile.jpg'))
                msg = await channel.send(
                                """**Create your own profile to describe yourself and start meeting others!** \n\n  📝 ➤ Edit Profile \n  `Update your information` \n\n 🔎 ➤ Preview Profile \n  `Preview your current profile!` \n\n **To Bump the server user the `!bump` command** \n  `cooldown: (Nomal 3d)` 
                                \n **For premium user should use the `!bumpp` command** \n *The `!bumpp command cost $3 monthly` message moderators to get more details on that* \n  `cooldown: (Normal: 12hrs)` 
                                \n Type `!create` to create a profile \n Type `!edit` to edit profile
                                """)

                edit='📝'
                preview= '🔎'
                await msg.add_reaction(edit)
                await msg.add_reaction(preview)


                def check(reaction, user):
            
                    return user and str(reaction.emoji) in [edit, preview]

                #user = await self.bot.fetch_user(ctx.author.id)
                while True:
                    try:
                        reaction, user = await self.bot.wait_for("reaction_add", check=check)
                       
                        if str(reaction.emoji) == edit:
                    
                            if user_in_db.get_user(user.id):
                        
                                await user.send('edit')

                        #userr = await self.bot.fetch_user(user.id)

                        if str(reaction.emoji) == preview:
                            try:
                                user_in_db.get_user(user.id)
                                user_d = user_in_db.get_user(user.id)

                                
                                user_data ={}
                                for i in range(len(self.dic_key)):
                                    user_data[self.dic_key[i]] = user_d[i]

                                Uembed=discord.Embed(title=f"PROFILE `{user_data['username']}` ", description="Type `!edit:` *To edit profile in the profile_channel*  ", color=discord.Color.blue())
                                Uembed.set_thumbnail(url=user.avatar)
                                Uembed.add_field(name="NAME ", value=f"{user_data['name']}", inline=True)
                                Uembed.add_field(name="LOCATION", value=f"{user_data['location']}", inline=True)
                                Uembed.add_field(name="HEIGHT", value=f"{user_data['height']}", inline=True)
                                Uembed.add_field(name="DATING STATUS", value=f"{user_data['dating_status']}", inline=True)
                                Uembed.add_field(name="LOOKING FOR", value=f"{user_data['looking_for']}", inline=True)
                                Uembed.add_field(name="HOBBIES", value=f"{user_data['hobbies']}",inline=True)
                                Uembed.add_field(name="BIOGRAPHY", value=f"{user_data['biography']}", inline=True)
                                Uembed.set_footer(text="profile can only be edited once a week",icon_url=user.avatar)
                                await user.send(embed=Uembed)

                            except:
                                await user.send("you don't have a profile to view")


                    except:
                        print("something is wrong with the emotions ")
                
async def setup(bot):
    await bot.add_cog(Viewprofile(bot))
