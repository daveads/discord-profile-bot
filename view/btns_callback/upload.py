import asyncio
import discord

# DB
from model import queries
from model import user_profile_images_inputd
from model import user_profile_image_query


from core.config_parser import BotConfigs
from core import embed

# Class initialized
user_in_db = queries.PROFILEque()
upload_db = user_profile_images_inputd
image_query = user_profile_image_query.Imageque()

bot_configs = BotConfigs()
user_embed = embed.Embed()

from view.btns_callback.upload_handler import handle_upload_data

async def upload(bot, interaction , button):
    
    user = await bot.fetch_user(interaction.user.id)
    image_count = image_query.total_user_images(user.id)

   

    if user_in_db.get_user(user.id):
        # handles users with premium roles
        prem = True
        if prem: # premium roles  
            if image_count != 3 : # images != 3
                await handle_upload_data(user, interaction, bot)
                    
            else:
                await interaction.response.send_message("Image Limit exceeded")

        
        # normal users 
        if(image_count == 1): # if image == 1:
            await interaction.followup.send("Image Limit exceeded for normal user")
            #interaction.followup.send
        elif (image_count == 0 ):
            await handle_upload_data(user, interaction, bot)
            #upload....


    else:

        try:
            await user_embed.user_reply(user,"YOU NEED TO BE SELFIE VERIFIED TO USE THE UPLOAD BUTTON")
            await interaction.response.defer()

        except:
            await interaction.response.send_message("YOU NEED TO BE SELFIE VERIFIED TO USE THE UPLOAD BUTTON", ephemeral=True)
            await asyncio.sleep(60)
            await interaction.delete_original_response()