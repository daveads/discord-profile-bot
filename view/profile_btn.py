import asyncio
import discord
from model import queries
from core import embed
from discord.ext import commands


# class initialized
user_in_db = queries.PROFILEque()
user_embed = embed.Embed()
#data = configs.Datajson()

from core.config_parser import BotConfigs
bot_configs = BotConfigs()

from model import user_profile_image_query
image_query = user_profile_image_query.Imageque()

#button callbacks
from view.btns_callback.create import create
from view.btns_callback.edit import edit
from view.btns_callback.preview import preview
from view.btns_callback.bump import bump
from view.btns_callback.upload import upload

from view.btns_callback.dm_upload_handler import dm_upload_data

class Profile(discord.ui.View):
    
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot
        self.dic_key = ['id','username','username_id','name','location','looking_for','hobbies','biography','premium_day','profile_date']
        self.seconds =  43200 # 12 hours      '''259200 #3days'''
        self.cooldown = commands.CooldownMapping.from_cooldown(1, self.seconds, commands.BucketType.member)
        self.cooldownEdit = commands.CooldownMapping.from_cooldown(3, 259200, commands.BucketType.member) #>>1hr  '''259200 #3days'''

        
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
    @discord.ui.button(label='Upload', style=discord.ButtonStyle.blurple, emoji='📁', custom_id='upload', row=1)
    async def upload(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        try:
            
            await upload(self.bot, interaction, button)
        
        except:

            user = await self.bot.fetch_user(interaction.user.id)
            
            image_count = image_query.total_user_images(user.id)

            from core import premium_roles

            roles = await premium_roles.premiumR(interaction)
            prem = any(R in interaction.user.roles for R in roles)

            if user_in_db.get_user(interaction.user.id): 

                if prem:  # premium roles
                    if image_count != 3:  # images != 3
                        
                        await interaction.response.defer()
                        await dm_upload_data(user, self.bot)
                        

                    else:
                        await interaction.response.send_message("Image Limit exceeded")
                        await asyncio.sleep(5)
                        await interaction.delete_original_response()

                # normal users
                elif prem == False:
                    if image_count != 0:
                        await interaction.response.send_message(
                            "Image Limit exceeded for normal user"
                        )
                        await asyncio.sleep(5)
                        await interaction.delete_original_response()

                    else:
                        await dm_upload_data(user, self.bot)
                        await interaction.response.defer()

            else:
                try:
                    await user_embed.user_reply(
                        user, "YOU NEED TO BE SELFIE VERIFIED TO USE THE UPLOAD BUTTON"
                    )
                    await interaction.response.defer()

                except:
                    await interaction.response.send_message(
                        "YOU NEED TO BE SELFIE VERIFIED TO USE THE UPLOAD BUTTON",
                        ephemeral=True,
                    )
                    await asyncio.sleep(30)
                    await interaction.delete_original_response()


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