import asyncio
import discord
from core import embed
from model import queries

from core.profile_data import profile_embed

# Class initialized
user_in_db = queries.PROFILEque()
user_embed = embed.Embed()

async def preview(bot, interaction, button):
    
    user = await bot.fetch_user(interaction.user.id)

    if user_in_db.get_user(interaction.user.id):

        profile_embed_data = await profile_embed(user, interaction)


        try:
            await user.send(embed=profile_embed_data)
            await interaction.response.defer()
            
        except:
            await interaction.response.send_message(embed=profile_embed_data, ephemeral=True)
            await asyncio.sleep(60)
            await interaction.delete_original_response()



    else:

        try:
            await user_embed.user_reply(user,"YOU DONT HAVE A PROFILE YET")
            await interaction.response.defer()
                

        except:
            await interaction.response.send_message("YOU DONT HAVE A PROFILE YET", ephemeral=True)
            await asyncio.sleep(60)
            await interaction.delete_original_response()