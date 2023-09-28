import asyncio

from core import embed
from model import queries
from view.modal.profile_modal import Creatprofile
from view.btns_callback.funcs import gender, age, orientation, datingstatus, dmstatus, height

# Class initialized
user_in_db = queries.PROFILEque()
user_embed = embed.Embed()


async def create(bot, interaction, button):
    # gender, orientation, datingstatus, dmstatus, height

    # missing some needed objests from the libary 
    user = await bot.fetch_user(interaction.user.id)
    userG = await interaction.guild.fetch_member(interaction.user.id)


    #Needed roles
    gender_roles = await gender(interaction)
    orientation_roles = await orientation(interaction)
    datingstatus_roles = await datingstatus(interaction)
    dmstatus_roles = await dmstatus(interaction)
    height_roles = await height(interaction)
    
    import numpy as np

    # CHECKS IF ROLE is in User object
    gender_check = np.isin(gender_roles, userG.roles) 
    orientation_check = np.isin(orientation_roles, userG.roles)
    datingstatus_check = np.isin(datingstatus_roles, userG.roles)
    dmstatus_check = np.isin(dmstatus_roles, userG.roles)
    height_check = np.isin(height_roles, userG.roles)

    needrole = [dmstatus_check, gender_check, height_check, orientation_check, datingstatus_check]
        
    def check_roles(array):
        dm = []

        for j in array:
            if True in j:
                dm.append(True)
           
        return dm

    if user_in_db.get_user(interaction.user.id):

        try:
            await interaction.response.defer()
            await user_embed.user_reply(user,"You Have a Profile Created Already")
            

        except:
            await interaction.response.send_message("You Have a Profile Created Already", ephemeral=True)
            await asyncio.sleep(30)
            await interaction.delete_original_response()

                         
    else:
        
        if len(check_roles(needrole)) == 5:
            
            await interaction.response.send_modal(Creatprofile())

        else:
            
            try:
                await interaction.response.defer()
                await user_embed.user_reply(user,"You Are Missing Some Roles")
                

            except:
                await interaction.response.send_message("You Are Missing Some Roles", ephemeral=True)
                await asyncio.sleep(60)
                await interaction.delete_original_response()
    