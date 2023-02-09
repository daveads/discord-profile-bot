from view.modal.profile_modal import Creatprofile
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


#button callbacks
from view.btns_callback.create import create
from view.btns_callback.edit import edit
from view.btns_callback.preview import preview
from view.btns_callback.bump import bump

async def get_element(array):
    element = None
    for i in range(len(array)):
        if array[i] == True:
            element = i
            #print(i)
               
    return element

async def gender(interaction):    
    #gender roles id
    role_male =  discord.utils.get(interaction.guild.roles, id=bot_configs.gender("male")) 
    role_female =  discord.utils.get(interaction.guild.roles, id=bot_configs.gender("female"))
    role_trans_female =  discord.utils.get(interaction.guild.roles, id=bot_configs.gender("trans_female"))
    role_non_binary =  discord.utils.get(interaction.guild.roles, id=bot_configs.gender("non_binary"))
    role_agender =  discord.utils.get(interaction.guild.roles, id=bot_configs.gender("agender"))
    role_bigender = discord.utils.get(interaction.guild.roles, id=bot_configs.gender("bigender"))
    role_genderfluid = discord.utils.get(interaction.guild.roles, id=bot_configs.gender("genderfluid"))
    role_t_ftm = discord.utils.get(interaction.guild.roles, id=bot_configs.gender("t_ftm"))
    role_t_mtf = discord.utils.get(interaction.guild.roles, id=bot_configs.gender("t_mtf"))

    genObj = [role_male, role_female, role_trans_female, role_non_binary, role_agender, role_bigender, role_genderfluid, role_t_ftm, role_t_mtf]
    
    return genObj

async def age(interaction):
    #age roles 
    a18_21 = discord.utils.get(interaction.guild.roles, id=bot_configs.age('18-21')) 
    a22_25 = discord.utils.get(interaction.guild.roles, id=bot_configs.age('22-25')) 
    a26_30 = discord.utils.get(interaction.guild.roles, id=bot_configs.age('26-30')) 
    a31    = discord.utils.get(interaction.guild.roles, id=bot_configs.age('31+'))

    ageObj = [a18_21, a22_25, a26_30, a31]
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
    married = discord.utils.get(interaction.guild.roles, id=bot_configs.datingstatus("married"))
    in_a_relatiohship = discord.utils.get(interaction.guild.roles, id=bot_configs.datingstatus("in_a_relatiohship"))


    dsObj = [single, taken, complicated, searching, nsearching, polyamorous, married, in_a_relatiohship]

    return dsObj

async def height(interaction):

    H4_6_4_8 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H4_6_4_8'))
    H4_8_4_10 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H4_8_4_10'))
    H4_10_5_0 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H4_10_5_0'))
    H5_0_5_2 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H5_0_5_2'))
    H5_2_5_4 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H5_2_5_4'))
    H5_4_5_6 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H5_4_5_6'))
    H5_6_5_8 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H5_6_5_8'))
    H5_8_5_10 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H5_8_5_10'))
    H5_10_6_0 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H5_10_6_0'))
    H6_0_6_2 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H6_0_6_2'))
    H6_2_6_4 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H6_2_6_4'))
    H6_4_ = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H6_4_'))

    heigObj = [H4_6_4_8, H4_8_4_10, H4_10_5_0, H5_0_5_2, H5_2_5_4, H5_4_5_6, H5_6_5_8, H5_8_5_10, H5_10_6_0, H6_0_6_2, H6_2_6_4, H6_4_] 

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
        self.seconds =  43200 # 12 hours      '''259200 #3days'''
        self.cooldown = commands.CooldownMapping.from_cooldown(1, self.seconds, commands.BucketType.member)
        self.cooldownEdit = commands.CooldownMapping.from_cooldown(1, 259200, commands.BucketType.member) # '''259200 #3days'''

        
    # CREATE BUTTON 
    @discord.ui.button(label='Create', style=discord.ButtonStyle.green, emoji='✅', custom_id='create', row=1)
    async def create(self, interaction: discord.Interaction, button: discord.ui.Button):
        await create(self.bot, interaction, button)        


    # EDIT BUTTON
    @discord.ui.button(label='Edit', style=discord.ButtonStyle.grey, emoji='📝' ,custom_id='edit', row=1)
    async def edit(self, interaction: discord.Interaction, button: discord.ui.Button):
       await edit(self.bot, self.cooldownEdit, interaction, button)


    # BUMP BUTTON 
    @discord.ui.button(label='Bump', style=discord.ButtonStyle.blurple, emoji='📢', custom_id='bump', row=1)
    async def bump(self, interaction: discord.Interaction, button: discord.ui.Button):
        await bump(self.bot, self.cooldown, interaction, button)



    # PREVIEW BUTTON
    @discord.ui.button(label='Preview', style=discord.ButtonStyle.grey, emoji='🔎' ,custom_id='preview' , row=1)
    async def preview(self, interaction: discord.Interaction, button: discord.ui.Button):
        await preview(self.bot, interaction, button)


    # UPLOAD BUTTON 
    @discord.ui.button(label='Upload', style=discord.ButtonStyle.blurple, emoji='📁', disabled=True, custom_id='upload', row=1)
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