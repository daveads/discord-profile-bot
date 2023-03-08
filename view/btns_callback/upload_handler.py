import discord
import asyncio
import os
from core.config_parser import BotConfigs

from discord.ui import Button, View
from core import embed

# DB
from model import user_images_inputd

# Class initialized
upload_db = user_images_inputd
bot_configs = BotConfigs()
user_embed = embed.Embed()




async def user_reply(user, bot, chh, channel_created):

    def check(message):
        return message.author == user and bool(message.attachments)
           
           
    try:
        resp = await bot.wait_for('message', check=check , timeout=30.0)

        d = str(resp.attachments[0])
        format = ['png', 'jpg', 'jpeg', 'heic']

        
        if d[-3:] in format:     
            return resp.attachments[0]

        else:
            return None

    except  asyncio.TimeoutError:
        await chh.send(f"Time out {user.mention}")
        await asyncio.sleep(20)
        await channel_created.delete()
           
    
    return False




async def handle_upload_data(user, interaction, bot):
    
    selfie_verf = discord.utils.get(interaction.guild.roles, id=bot_configs.role("selfie_verf"))

    if selfie_verf in interaction.user.roles:

        guild = interaction.guild

        admin_role = guild.get_role(bot_configs.admin('admin'))
        

        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            admin_role: discord.PermissionOverwrite(view_channel=True),
            guild.me: discord.PermissionOverwrite(view_channel=True, read_messages=True),
            interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages = True, attach_files = True) 
        }

        category = discord.utils.get(interaction.guild.categories, id=bot_configs.channel('profile_category'))

        channel_name = f"pics_upload-{interaction.user.id}"

        #Pending Channel

        userverify_channels = []

        for i in category.channels:
            userverify_channels.append(i.name)


        def user_in_profchn(userverify_channels):            
            for i in userverify_channels:                  
                if str(user.id) in i:
                    return True

            return False 
        
        user_in_chn = user_in_profchn(userverify_channels)

        if user_in_chn:
            await interaction.response.send_message(content="You Have a Pending Profile Upload Channel", )
            
        else:
            await guild.create_text_channel(channel_name,  category=category, overwrites=overwrites)
            channel_created = discord.utils.get(guild.channels, name=channel_name)
            button = Button(label="Go to Channel", url=f"https://discord.com/channels/{interaction.guild.id}/{channel_created.id}" ,  style=discord.ButtonStyle.grey)
            view = View()
            view.add_item(button)

            await interaction.response.send_message(content="Selfie Upload channel created, click the button below to get to the channel!", view=view, ephemeral=True)

            #THE CHANNEL
            chh = discord.utils.get(guild.channels, name=channel_name)
            
            # interaction.user.mention
            await chh.send(interaction.user.mention)
        

            #Upload Pics
            embed_first=discord.Embed(color=discord.Color.blue())
            embed_first.set_author(name=f"{interaction.guild.name} Upload Selfie", icon_url=f"{interaction.guild.icon.url}")
            embed_first.add_field(name="First picture", value=f"Upload a Selfie you which to displayed on your profile \n\n  **UPLOADED FILE SHOULD ONLY BE PICTURES**", inline=True)
            
            embed_wanning = discord.Embed(color=discord.Color.blue())
            embed_wanning.set_author(name=f"{interaction.guild.name}", icon_url=f"{interaction.guild.icon.url}")
            embed_wanning.add_field(name="------------------------",value="Waiting for image  \n\n  **Timeout in 5 minutes**", inline=True)
            
            await chh.send(embed=embed_first)
            await chh.send(embed=embed_wanning)

            await asyncio.sleep(2)

            image1 = await user_reply(user, bot, chh, channel_created)

            # Needs refactory
            while(True):

                if image1 == None:
                    await chh.send("uploaded file can only be a image file")
                    image1 = await user_reply(user, bot, chh, channel_created)
                
                elif image1 !=None:
                    break

            
            if (image1):
                Ori_filename = image1.filename

                img_length = len(Ori_filename) - 4
                image = f"{user.name}-{Ori_filename[:img_length]}{Ori_filename[-4:]}"
                folder_name = "UserImages"

                #database
                upload_db.image_data(
                    str(user.id),
                    image,
                )

                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                    await image1.save(fp=f"{folder_name}/{image}")
                

                try:
                    await user_embed.user_reply(user,"Image Uploaded")
                    await chh.send("Image Upload Successful")
                    
                except:
                    await chh.send("Image Uploaded")


                if os.path.isfile(os.path.join(folder_name, image)):
                    print("yesssss")

                await asyncio.sleep(20)
                await channel_created.delete()
