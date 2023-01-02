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

async def gender(interaction):
    role_male =  discord.utils.get(interaction.guild.roles, id=bot_configs.gender('male')) 
    role_female =  discord.utils.get(interaction.guild.roles, id=bot_configs.gender("female"))
    role_trans_female =  discord.utils.get(interaction.guild.roles, id=bot_configs.gender("trans_female"))
    role_non_binary =  discord.utils.get(interaction.guild.roles, id=bot_configs.gender("non_binary"))
    role_agender =  discord.utils.get(interaction.guild.roles, id=bot_configs.gender("agender"))
    role_bigender = discord.utils.get(interaction.guild.roles, id=bot_configs.gender("bigender"))
    role_genderfluid = discord.utils.get(interaction.guild.roles, id=bot_configs.gender("genderfluid"))

    genObj = [role_male, role_female, role_trans_female, role_non_binary, role_agender, role_bigender, role_genderfluid]
    
    return genObj

async def age(interaction):
    a18_22 = discord.utils.get(interaction.guild.roles, id=bot_configs.age('18-22')) 
    a23_27 = discord.utils.get(interaction.guild.roles, id=bot_configs.age('23-27')) 
    a28_30 = discord.utils.get(interaction.guild.roles, id=bot_configs.age('28-30+')) 
    ageObj = [a18_22, a23_27, a28_30]
    return ageObj


async def orientation(interaction):
    hetorsexual = discord.utils.get(interaction.guild.roles, id=bot_configs.orientaion('hetorsexual'))
    homosexual = discord.utils.get(interaction.guild.roles, id=bot_configs.orientaion('homosexual'))
    bisexual = discord.utils.get(interaction.guild.roles, id=bot_configs.orientaion('bisexual'))
    pansexual = discord.utils.get(interaction.guild.roles, id=bot_configs.orientaion('pansexual'))
    asexual = discord.utils.get(interaction.guild.roles, id=bot_configs.orientaion('asexual'))
    demisexual = discord.utils.get(interaction.guild.roles, id=bot_configs.orientaion('demisexual'))
    bicurious = discord.utils.get(interaction.guild.roles, id=bot_configs.orientaion('bicurious'))
    
    oriObj = [hetorsexual, homosexual, asexual, bicurious, bisexual, demisexual, pansexual]

    return oriObj

#datingstatus  dmstatus height_roles

async def dmstatus(interaction):
    
    dmOpen = discord.utils.get(interaction.guild.roles, id=bot_configs.dmstatus('dmOpen'))
    dmOpenNoNsfw =discord.utils.get(interaction.guild.roles, id=bot_configs.dmstatus('dmOpenNoNsfw'))
    dmAsk = discord.utils.get(interaction.guild.roles, id=bot_configs.dmstatus('dmAsk'))
    dmOpenVerifiedOnly = discord.utils.get(interaction.guild.roles, id=bot_configs.dmstatus('dmOpenVerifiedOnly'))
    dmClosed = discord.utils.get(interaction.guild.roles, id=bot_configs.dmstatus('dmClosed'))
    
    dsObj = [dmAsk, dmClosed, dmOpen, dmOpenNoNsfw, dmOpenVerifiedOnly]

    return dsObj 

async def datingstatus(interaction):

    single = discord.utils.get(interaction.guild.roles, id=bot_configs.datingstatus("single"))
    taken =discord.utils.get(interaction.guild.roles, id=bot_configs.datingstatus("taken"))
    complicated = discord.utils.get(interaction.guild.roles, id=bot_configs.datingstatus("complicated"))
    searching = discord.utils.get(interaction.guild.roles, id=bot_configs.datingstatus("searching"))
    nsearching = discord.utils.get(interaction.guild.roles, id=bot_configs.datingstatus("nsearching"))
    polyamorous = discord.utils.get(interaction.guild.roles, id=bot_configs.datingstatus("polyamorous"))

    dsObj = [single, taken, complicated, searching, nsearching, polyamorous]

    return dsObj

async def height(interaction):

    H4_6_4_8 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H4_6_4_8'))
    H4_8_4_10 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H4_8_4_10'))
    H4_10_5_10 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H4_10_5_10'))
    H5_0_5_2 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H5_0_5_2'))
    H5_2_5_4 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H5_2_5_4'))
    H5_4_5_8 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H5_4_5_8'))
    H5_8_5_10 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H5_8_5_10'))
    H5_10_6_0 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H5_10_6_0'))
    H6_0_6_2 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H6_0_6_2'))
    H6_2_6_4 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H6_2_6_4'))
    H6_4_ = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H6_4_'))

    heigObj = [H4_6_4_8, H4_8_4_10, H4_10_5_10, H5_0_5_2, H5_2_5_4, H5_4_5_8, H5_8_5_10, H5_10_6_0, H6_0_6_2, H6_2_6_4, H6_4_] 

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

    return heigObj

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
        
        # gender, age, orientation, datingstatus, dmstatus, height
        
        print(f'user profile id {interaction.user.id}') 
        user = await self.bot.fetch_user(interaction.user.id)

        
        self.user = await interaction.guild.fetch_member(interaction.user.id)


        #Needed roles
        gender_roles = await gender(interaction)
        age_roles = await age(interaction)
        orientation_roles = await orientation(interaction)
        datingstatus_roles = await datingstatus(interaction)
        dmstatus_roles = await dmstatus(interaction)
        height_roles = await height(interaction)
        import numpy as np

        # CHECKS IF ROLE is in User object
        gender_check = np.isin(gender_roles, self.user.roles) 
        age_check = np.isin(age_roles, self.user.roles)
        orientation_check = np.isin(orientation_roles, self.user.roles)
        datingstatus_check = np.isin(datingstatus_roles, self.user.roles)
        dmstatus_check = np.isin(dmstatus_roles, self.user.roles)
        height_check = np.isin(height_roles, self.user.roles)

        needrole = [age_check, dmstatus_check, gender_check, height_check, orientation_check, datingstatus_check]
        
        def check_roles(array):
            dm = []

            #for i in range(5):
            for j in array:
                if True in j:
                    dm.append(True)
           
            return dm

        if user_in_db.get_user(interaction.user.id):
            await interaction.response.defer()
            await user_embed.user_reply(user,"you have a profile created already")

                         
        else:

            if len(check_roles(needrole)) == 6:
                await interaction.response.send_modal(Creatprofile())

            else:
                await user_embed.user_reply(user,"missing some roles")
                await interaction.response.defer()
        






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


        #Needed roles
        gender_roles = await gender(interaction)
        
        age_roles = await age(interaction)

        orientation_roles = await orientation(interaction)

        datingstatus_roles = await datingstatus(interaction)

        dmstatus_roles = await dmstatus(interaction)

        height_roles = await height(interaction)


        import numpy as np

        # CHECKS IF ROLE is in User object
        gender_check = np.isin(gender_roles, self.user.roles)
        age_check = np.isin(age_roles, self.user.roles)
        orientation_check = np.isin(orientation_roles, self.user.roles)
        datingstatus_check = np.isin(datingstatus_roles, self.user.roles)
        dmstatus_check = np.isin(dmstatus_roles, self.user.roles)
        height_check = np.isin(height_roles, self.user.roles)
        
        # array index
        age_get = await get_element(age_check)
        gender_get = await get_element(gender_check)
        orientation_get = await get_element(orientation_check)
        datingstatus_get = await get_element(datingstatus_check)
        dmstatus_get = await get_element(dmstatus_check)
        height_get = await get_element(height_check)

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
                    embed.add_field(name="Gender", value=f"{gender_roles[gender_get]}", inline=True)
                    embed.add_field(name="Age", value=f"{age_roles[age_get]}", inline=True)
                    embed.add_field(name="Orientation", value=f"{orientation_roles[orientation_get]}", inline=True)
                    embed.add_field(name="Location", value=f"{user_data['location']}", inline=True)
                    #embed.add_field(name="Verification level", value=f"Not verified", inline=True)
                    embed.add_field(name="Height", value=f"{height_roles[height_get]}", inline=True)
                    embed.add_field(name="DMs status", value=f"{dmstatus_roles[dmstatus_get]}", inline=True)
                    embed.add_field(name="dating status", value=f"{datingstatus_roles[datingstatus_get]}", inline=True)
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


    # CREATE BUTTON 
    @discord.ui.button(label='Upload', style=discord.ButtonStyle.green, emoji='📁', custom_id='upload', row=1)
    async def upload(self, interaction: discord.Interaction, button: discord.ui.Button):

        pass 



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