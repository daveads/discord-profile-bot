from view.profile_modal import Creatprofile
import discord
from model import profile
from model import queries
from core import embed
from discord.ext import commands
import asyncio
from core import configs


# class initialized
user_in_db = queries.PROFILEque()
user_embed = embed.Embed()
#data = configs.Datajson()

from core.config_parser import BotConfigs
bot_configs = BotConfigs()

async def get_element(array):
    element = None
    for i in range(len(array)):
        if array[i] == True:
            element = i
            #print(i)
               
    return element

class Profile(discord.ui.View):
    
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot
        self.dic_key = ['id','username','username_id','name','location','looking_for','hobbies','biography','premium_day','profile_date']
        self.seconds = 259200 #3days
        self.cooldown = commands.CooldownMapping.from_cooldown(1, self.seconds, commands.BucketType.member)
        

        
    # CREATE BUTTON 
    @discord.ui.button(label='Create', style=discord.ButtonStyle.green, emoji='✅', custom_id='create', row=1)
    async def create(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        print(f'user profile id {interaction.user.id}') 
        user = await self.bot.fetch_user(interaction.user.id)


        if user_in_db.get_user(interaction.user.id):
            await interaction.response.defer()
            await user_embed.user_reply(user,"you have a profile created already")

        else:

            await interaction.response.send_modal(Creatprofile())







    # EDIT BUTTON
    @discord.ui.button(label='Edit', style=discord.ButtonStyle.grey, emoji='📝' ,custom_id='edit', row=1)
    async def edit(self, interaction: discord.Interaction, button: discord.ui.Button):
        
      
        user = await self.bot.fetch_user(interaction.user.id)  
        
        if user_in_db.get_user(interaction.user.id):
            await interaction.response.defer()
            await user_embed.user_reply(user,"you have a profile created already")


            user_d = user_in_db.get_user(interaction.user.id)
            user_data ={}
          
            for i in range(len(self.dic_key)):
                user_data[self.dic_key[i]] = user_d[i]


            embed=discord.Embed(title=f"PROFILE `{interaction.user}`",  description="Type in a number to edit a particular field \n *Default* `Timeout: 1mins` ", color=discord.Color.blue())
                #embed.set_image(url=(author.avatar_url))
            embed.set_thumbnail(url=interaction.user.avatar)
            embed.add_field(name="(1) NAME ", value=f"{user_data['name']}", inline=True)
            embed.add_field(name="(2) LOCATION", value=f"{user_data['location']}", inline=True)
            embed.add_field(name="(3) LOOKING FOR", value=f"{user_data['looking_for']}", inline=True)
            embed.add_field(name="(4) HOBBIES", value=f"{user_data['hobbies']}",inline=True)
            embed.add_field(name="(5) BIOGRAPHY", value=f"{user_data['biography']}", inline=True)
            embed.set_footer(text="profile can only be edited once a week",icon_url=interaction.user.avatar)
            await user.send(embed=embed)

            
            #NOT SO GOOD 
            msg_timer=60
            while(True):
                
                try:
                    def check(msg):
                        return msg.author == user
                      
                    msg = await self.bot.wait_for("message", check=check, timeout=msg_timer)       
                          
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


                    
                    #looking_for
                    elif msg.content ==  '3':
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
                    elif msg.content ==  '4':
                        await user.send("What are your hobbies?")
                        await asyncio.sleep(2)
                        if msg1.content:
                            msg1 = await self.bot.wait_for("message", check=check, timeout=msg_timer)
                            user_in_db.update('hobbies', msg1.content, user.id)
                            user_in_db.con.commit()
                        else:
                            await user_embed.user_reply(user,"field can not be empty")

                    #biography
                    elif msg.content ==  '5':
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

            await user_embed.user_reply(user,"YOU NO PROFILE TO EDIT")
    









    # BUMP BUTTON 
    @discord.ui.button(label='Bump', style=discord.ButtonStyle.blurple, emoji='📢', custom_id='bump', row=1)
    async def bump(self, interaction: discord.Interaction, button: discord.ui.Button):

        # idk
        self.user = await interaction.guild.fetch_member(interaction.user.id)

        #gender roles
        self.role_male =  discord.utils.get(interaction.guild.roles, id=bot_configs.gender('male')) 
        self.role_female =  discord.utils.get(interaction.guild.roles, id=bot_configs.gender("female"))
        self.role_trans_female =  discord.utils.get(interaction.guild.roles, id=bot_configs.gender("trans_female"))
        self.role_non_binary =  discord.utils.get(interaction.guild.roles, id=bot_configs.gender("non_binary"))
        self.role_agender =  discord.utils.get(interaction.guild.roles, id=bot_configs.gender("agender"))
        self.role_bigender = discord.utils.get(interaction.guild.roles, id=bot_configs.gender("bigender"))
        self.role_genderfluid = discord.utils.get(interaction.guild.roles, id=bot_configs.gender("genderfluid"))
       

        #age roles 
        self.a18_22 = discord.utils.get(interaction.guild.roles, id=bot_configs.age('18-22')) 
        self.a23_27 = discord.utils.get(interaction.guild.roles, id=bot_configs.age('23-27')) 
        self.a28_30 = discord.utils.get(interaction.guild.roles, id=bot_configs.age('28-30+')) 


        #orientation
        """
        self.hetorsexual
        self.homosexual
        self.bisexual
        self.pansexual
        self.asexual
        self.demisexual
        self.bicurious
        """

        #height
        """
        4'6-4'8 |     137-142cm
        4'8- 4'10 |   142-147cm
        4'10 - 5'10 | 147-152cm
        5'0 - 5'2 |   152-157cm
        5'2 - 5'4 |   157-162cm
        5'4 - 5'8 |   162-167cm
        5'8 - 5'10 |  167-177cm
        5'10 - 6'0 |  177-182cm
        6'0 - 6'2 |   182-187cm
        6'2 - 6'4 |   187-193cm
        6'4+ | 193cm+
        """



        #DMs status
        """
        dm-open  *
        dm-open[no-nsfw]  
        dm-ask  * 
        dm-open[verified-only]   
        dm-closed *
        """

        #dating status
        """
        single
        taken
        it's complicated
        search
        not searching
        polyamorous
        """

        #verification level

        gender_roles = [self.role_male, self.role_female, self.role_trans_female, self.role_non_binary, self.role_agender, self.role_bigender, self.role_genderfluid]
       
        age_roles = [self.a18_22, self.a23_27, self.a28_30]


        import numpy as np
        gender_check = np.isin(gender_roles, self.user.roles)
        age_check = np.isin(age_roles, self.user.roles)

        age_get = await get_element(age_check)
        gender_get = await get_element(gender_check)

        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        
        
        #minutes = str(retry % 60)
        # , {minutes} minutes {round(retry, 1)} seconds

        user = await self.bot.fetch_user(interaction.user.id)
        role = discord.utils.get(interaction.guild.roles, id=bot_configs.role('premium_role_id')) 
        

        if role in interaction.user.roles:
            await user.send("premium user should use the !bumpp commands")
            bucket.reset()

        else:

            if user_in_db.get_user(interaction.user.id):
         
                if retry:
                    second = round(retry, 1)
                    hours = (retry // 3600)
                    minutes = (hours * 60)

                    day = hours / 24
            

                    await interaction.response.send_message(f"try again in {round(day)} Days {hours} hours {minutes} minutes, {second} seconds", ephemeral=True)        

            
                else:
                    await interaction.response.send_message("OK", ephemeral=True)

                    user_d = user_in_db.get_user(interaction.user.id)
                    user_data ={}
                    for i in range(len(self.dic_key)):
                        user_data[self.dic_key[i]] = user_d[i] 

                    print(user_data)
                    
                    male = discord.utils.get(interaction.guild.roles, id=bot_configs.gender('male'))
                    female = discord.utils.get(interaction.guild.roles, id=bot_configs.gender('female'))
                    #others = discord.utils.get(interaction.guild.roles, id=1053923859105067019)

                    channel_male = self.bot.get_channel(bot_configs.channel('male_channel'))
                    channel_female = self.bot.get_channel(bot_configs.channel('female_channel'))
                    channel_other = self.bot.get_channel(bot_configs.channel('others_channel'))

                    """
                    Embed 
                    """
                    embed=discord.Embed(title=f"User: <@{user.id}>", url="", description="", color=discord.Color.red())
                    embed.set_thumbnail(url=user.avatar)
                    embed.set_author(name=f"{user}", icon_url=(user.avatar))
                    embed.add_field(name="Name", value=f"{user_data['name']}", inline=True)
                    embed.add_field(name="Age", value=f"{gender_roles[gender_get]}", inline=True)
                    embed.add_field(name="Gender", value=f"{age_roles[age_get]}", inline=True)
                    #embed.add_field(name="Orientation", value=f"Straight", inline=True)
                    embed.add_field(name="Location", value=f"{user_data['location']}", inline=True)
                    #embed.add_field(name="DMs status", value=f"dm status", inline=True)
                    #embed.add_field(name="Verification level", value=f"Not verified", inline=True)
                    #height
                    #dating status
                    embed.add_field(name="Looking for ", value=f"{user_data['looking_for']}", inline=True)
                    embed.add_field(name="Hobbies ", value=f"{user_data['hobbies']}", inline=True)
                    embed.add_field(name="About me ", value=f"{user_data['biography']}", inline=False)
                    embed.set_footer(text=f"{interaction.guild.name}", icon_url=interaction.guild.icon.url)

                    #await channel.send(f"{interaction.user.mention}")
                    #await channel.send(embed=embed)
                    
                    if male in interaction.user.roles:
                        await channel_male.send(f"{user.mention}")
                        await channel_male.send(embed=embed)

                    elif female in interaction.user.roles:
                        await channel_female.send(f"{user.mention}")
                        await channel_female.send(embed=embed)

                    else:
                        await channel_other.send(f"{user.mention}")
                        await channel_other.send(embed=embed)




            else:
                await interaction.response.send_message("you don't have a profile", ephemeral=True)
                bucket.reset()






    # PREVIEW BUTTON
    #@commands.cooldown(1, 259200, commands.BucketType.user) #next 3days 
    @discord.ui.button(label='Preview', style=discord.ButtonStyle.grey, emoji='🔎' ,custom_id='preview' , row=1)
    async def preview(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        user = await self.bot.fetch_user(interaction.user.id)

        if user_in_db.get_user(interaction.user.id):

            user_d = user_in_db.get_user(interaction.user.id)
            user_data ={}
            for i in range(len(self.dic_key)):
                user_data[self.dic_key[i]] = user_d[i]

            print(user_data)
            embed=discord.Embed(title=f"PROFILE `{user_data['username']}` ", description="Your current profile details", color=discord.Color.blue())
            embed.set_thumbnail(url=user.avatar)
            embed.add_field(name="NAME ", value=f"{user_data['name']}", inline=True)
            embed.add_field(name="LOCATION", value=f"{user_data['location']}", inline=True)
            embed.add_field(name="LOOKING FOR", value=f"{user_data['looking_for']}", inline=True)
            embed.add_field(name="HOBBIES", value=f"{user_data['hobbies']}",inline=True)
            embed.add_field(name="BIOGRAPHY", value=f"{user_data['biography']}", inline=True)
            embed.set_footer(text="profile can only be edited once a week",icon_url=user.avatar)
            await user.send(embed=embed)
            await interaction.response.defer()

        else:
            await interaction.response.defer()
            await user_embed.user_reply(user,"YOU DONT HAVE A PROFILE YET")



# Gender,  age  __


# sexuality   
"""
hetorsexual
homosexual
bisexual
pansexual
asexual
demisexual
bicurious ****
"""

# height 
"""
4'6-4'8 |     137-142cm
4'8- 4'10 |   142-147cm
4'10 - 5'10 | 147-152cm
5'0 - 5'2 |   152-157cm
5'2 - 5'4 |   157-162cm
5'4 - 5'8 |   162-167cm
5'8 - 5'10 |  167-177cm
5'10 - 6'0 |  177-182cm
6'0 - 6'2 |   182-187cm
6'2 - 6'4 |   187-193cm
6'4+ | 193cm+
"""

# dm status   
"""
dm-open  *
dm-open[no-nsfw]  
dm-ask  * 
dm-open[verified-only]   
dm-closed *
"""

# dating status
"""
single
taken
it's complicated
search
not searching
polyamorous
"""

# occupation
"""
* in high school
* in college /studing
* Employed
* unemployed
"""

# location 
"""
north america
south america
europe
africa
middle east
"""

# preferecence
"""
What's you preference

Age | prefer Younger(18+)
Prefer same age
prefer older
prefer shorter
perfer taller

"""


# pronoun 
"""
he/him
she/her
they/them
any pronouns
Ask pronouns
"""
# pick only one, pick all, reset


# for profile 
# age gender orientation Location dating-status height dm-status verification_level[verified, half-verified, not-verified]  