import discord
from core.config_parser import BotConfigs
from model import queries
from view.btns_callback.funcs import (
    gender,
    age,
    orientation,
    datingstatus,
    dmstatus,
    height,
    get_element,
)
from model import user_profile_image_query
from model import follower_following_query

# Class initialized
user_in_db = queries.PROFILEque()
bot_configs = BotConfigs()
image_query = user_profile_image_query.Imageque()
ffq = follower_following_query.Following_follower()

async def profile_embed(user, interaction):

    dic_key = ['id','username','username_id','name','location','looking_for','hobbies','biography','age','profile_date']

    # verification tag
    age_verf = discord.utils.get(interaction.guild.roles, id=bot_configs.age("age_verf"))
    selfie_verf = discord.utils.get(interaction.guild.roles, id=bot_configs.role("selfie_verf"))

    user_d = user_in_db.get_user(user.id)
    user_data = {}
    for i in range(len(dic_key)):
        user_data[dic_key[i]] = user_d[i]


    #user images 
    images_data = image_query.get_user_images(user.id)
    user_images = [img[0] for img in images_data]

    # idk
    userG = await interaction.guild.fetch_member(interaction.user.id)

    # Needed roles
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

    # array index
    gender_get = await get_element(gender_check)
    orientation_get = await get_element(orientation_check)
    datingstatus_get = await get_element(datingstatus_check)
    dmstatus_get = await get_element(dmstatus_check)
    height_get = await get_element(height_check)

    """
    Embed 
    """

    embed = discord.Embed(
        title=f"PROFILE `{user_data['username']}` ",
        url="",
        description="",
        color=discord.Color.red(),
    )
    embed.set_thumbnail(url=user.avatar)
    embed.set_author(name=f"{user}", icon_url=(user.avatar))
    embed.add_field(name="Name", value=f"{user_data['name']}", inline=True)
    embed.add_field(
        name="Gender", value=f"{gender_roles[gender_get]}", inline=True
    )
    embed.add_field(name="Age", value=f"{user_data['age']}", inline=True)
    embed.add_field(
        name="Orientation",
        value=f"{orientation_roles[orientation_get]}",
        inline=True,
    )
    embed.add_field(
        name="Location", value=f"{user_data['location']}", inline=True
    )
    # embed.add_field(name="Verification level", value=f"Not verified", inline=True)
    embed.add_field(
        name="Height", value=f"{height_roles[height_get]}", inline=True
    )
    embed.add_field(
        name="DMs status",
        value=f"{dmstatus_roles[dmstatus_get]}",
        inline=True,
    )
    embed.add_field(
        name="dating status",
        value=f"{datingstatus_roles[datingstatus_get]}",
        inline=True,
    )
    embed.add_field(
        name="Looking for ",
        value=f"{user_data['looking_for']}",
        inline=True,
    )

    following = ffq.total_following_count(interaction.user.id)
    followers = ffq.total_followers_count(interaction.user.id)
 
    embed.add_field( name="Following", value=f"{following}", inline=True)
    embed.add_field( name="Followers", value=f"{followers}", inline=True)


    # verification level
    if age_verf in interaction.user.roles and selfie_verf in interaction.user.roles:
        
        embed.add_field(
        name="Verification level",
        value=f"Selfie & Age verified",
        inline=False,
    )

    elif age_verf in interaction.user.roles:
        embed.add_field( name="Verification level", value=f"Age verified", inline=False,)

    elif selfie_verf in interaction.user.roles:
        embed.add_field( name="Verification level", value=f"Selfie verified", inline=False,)

    else:
        embed.add_field( name="Verification level", value=f"Not verified", inline=False,)

    embed.add_field(
        name="Hobbies ", value=f"{user_data['hobbies']}", inline=False
    )
    embed.add_field(
        name="About me ", value=f"{user_data['biography']}", inline=False
    )

    embed.set_footer(
        text=f"{interaction.guild.name}",
        icon_url=interaction.guild.icon.url,
    )

    from core.random_image import randomise_image

    if user_images:
        user_pic = randomise_image(user_images)

        file = discord.File(f"UserImages/{user_pic}")
        embed.set_image(url=f"attachment://{user_pic}")

        return embed, file

    file = None
    return embed, file