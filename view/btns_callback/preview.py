import asyncio
import discord
from core import embed
from model import queries
from view.modal.profile_modal import Creatprofile
from view.btns_callback.funcs import gender, age, orientation, datingstatus, dmstatus, height

# Class initialized
user_in_db = queries.PROFILEque()
user_embed = embed.Embed()

async def preview(bot, interaction, button):
    dic_key = ['id','username','username_id','name','location','looking_for','hobbies','biography','premium_day','profile_date']

    user = await bot.fetch_user(interaction.user.id)

    if user_in_db.get_user(interaction.user.id):
        
        user_d = user_in_db.get_user(interaction.user.id)
        user_data ={}
        for i in range(len(dic_key)):
            user_data[dic_key[i]] = user_d[i]

           
        embed=discord.Embed(title=f"PROFILE `{user_data['username']}` ", description="Your current profile details", color=discord.Color.blue())
        embed.set_thumbnail(url=user.avatar)
        embed.add_field(name="NAME ", value=f"{user_data['name']}", inline=True)
        embed.add_field(name="LOCATION", value=f"{user_data['location']}", inline=True)
        embed.add_field(name="LOOKING FOR", value=f"{user_data['looking_for']}", inline=True)
        embed.add_field(name="HOBBIES", value=f"{user_data['hobbies']}",inline=True)
        embed.add_field(name="BIOGRAPHY", value=f"{user_data['biography']}", inline=True)
        embed.set_footer(text="profile can only be edited once a week",icon_url=user.avatar)

        try:
            await user.send(embed=embed)
            await interaction.response.defer()
            
        except:
            await interaction.response.send_message(embed=embed, ephemeral=True)
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