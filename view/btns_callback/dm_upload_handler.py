import asyncio
import os
import discord

from core import embed

# DB
from model import user_profile_images_inputd

# Class initialized
upload_db = user_profile_images_inputd
user_embed = embed.Embed()


async def user_imager(resp):
    d = str(resp.attachments[0])
    format = ["png", "jpg", "jpeg", "heic"]

    if d[-3:] in format:
        return resp.attachments[0]

    else:
        return None


async def dm_upload_data(user, bot):
    embed = discord.Embed(
        title=f"PROFILE Picture Upload`",
        description="*Default* `Timeout: 1mins` ",
        color=discord.Color.blue(),
    )
    # embed.set_image(url=(author.avatar_url))
    embed.set_thumbnail(url=user.avatar)
    embed.add_field(
        name="picture",
        value=f"Send a Picture you would like to display on your profile",
        inline=True,
    )

    await user.send(embed=embed)

    # NOT SO GOOD
    msg_timer = 60
    while True:
        try:

            def check(msg):
                return msg.author == user and bool(msg.attachments) and not msg.guild

            msg = await bot.wait_for("message", check=check, timeout=msg_timer)

            user_image = await user_imager(msg)

            if user_image == None:
                user.send("You are going to have to start all over again")

            elif user_image != None:
                Ori_filename = user_image.filename

                img_length = len(Ori_filename) - 4
                image = f"{user.name}-{Ori_filename[:img_length]}{Ori_filename[-4:]}"
                folder_name = "UserImages"

                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                    await user_image.save(fp=f"{folder_name}/{image}")

                    # database
                    upload_db.image_data(
                        str(user.id),
                        image,
                    )

                else:
                    await user_image.save(fp=f"{folder_name}/{image}")

                    # database
                    upload_db.image_data(
                        str(user.id),
                        image,
                    )

                try:
                    await user_embed.user_reply(user, "Image Upload Successful")

                except:
                    await user.send("Image Uploaded")

                if os.path.isfile(os.path.join(folder_name, image)):
                    print("yesssss")

        except asyncio.TimeoutError:
            break
