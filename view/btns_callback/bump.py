import asyncio
import discord

from discord.ext import commands
from core import embed
from model import queries
from core.config_parser import BotConfigs


bot_configs = BotConfigs()

from view.btns_callback.funcs import (
    gender,
    age,
    orientation,
    datingstatus,
    dmstatus,
    height,
    get_element,
)

# Class initialized
user_in_db = queries.PROFILEque()
user_embed = embed.Embed()


async def bump(bot, cooldown, interaction , button):

    dic_key = ['id','username','username_id','name','location','looking_for','hobbies','biography','premium_day','profile_date']

    # idk
    userG = await interaction.guild.fetch_member(interaction.user.id)

    # Needed roles
    gender_roles = await gender(interaction)
    age_roles = await age(interaction)
    orientation_roles = await orientation(interaction)
    datingstatus_roles = await datingstatus(interaction)
    dmstatus_roles = await dmstatus(interaction)
    height_roles = await height(interaction)

    import numpy as np

    # CHECKS IF ROLE is in User object
    gender_check = np.isin(gender_roles, userG.roles)
    age_check = np.isin(age_roles, userG.roles)
    orientation_check = np.isin(orientation_roles, userG.roles)
    datingstatus_check = np.isin(datingstatus_roles, userG.roles)
    dmstatus_check = np.isin(dmstatus_roles, userG.roles)
    height_check = np.isin(height_roles, userG.roles)

    # array index
    age_get = await get_element(age_check)
    gender_get = await get_element(gender_check)
    orientation_get = await get_element(orientation_check)
    datingstatus_get = await get_element(datingstatus_check)
    dmstatus_get = await get_element(dmstatus_check)
    height_get = await get_element(height_check)

    interaction.message.author = interaction.user
    bucket = cooldown.get_bucket(interaction.message)
    retry = bucket.update_rate_limit()

    # minutes = str(retry % 60)
    # , {minutes} minutes {round(retry, 1)} seconds

    user = await bot.fetch_user(interaction.user.id)
    role = discord.utils.get(
        interaction.guild.roles, id=bot_configs.role("premium_role_id")
    )

    if role in interaction.user.roles:
        await user.send("premium user should use the !bumpp commands")
        print("premium")
        bucket.reset()

    else:
        if user_in_db.get_user(user.id):
            print("retry")
            if retry:
                print("1")
                second = round(retry, 1)
                hours = retry // 3600
                minutes = hours * 60

                day = hours / 24
                print("check timer")
                await interaction.response.send_message(
                    f"try again in {round(day)} Days {hours} hours {minutes} minutes, {second} seconds",
                    ephemeral=True,
                )

            else:
                try:
                    await interaction.response.defer()

                except:
                    await interaction.response.send_message(
                        "Something went wrong \n **Try Again or Contact The Dev**",
                        ephemeral=True,
                    )
                    await asyncio.sleep(60)
                    await interaction.delete_original_response()

                user_d = user_in_db.get_user(user.id)
                user_data = {}
                for i in range(len(dic_key)):
                    user_data[dic_key[i]] = user_d[i]

                male = discord.utils.get(
                    interaction.guild.roles, id=bot_configs.gender("male")
                )
                female = discord.utils.get(
                    interaction.guild.roles, id=bot_configs.gender("female")
                )

                channel_male = bot.get_channel(bot_configs.channel("male_channel"))
                channel_female = bot.get_channel(
                    bot_configs.channel("female_channel")
                )
                channel_other = bot.get_channel(
                    bot_configs.channel("others_channel")
                )

                """
                Embed 
                """

                embed = discord.Embed(
                    title=f"User: <@{user.id}>",
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
                embed.add_field(name="Age", value=f"{age_roles[age_get]}", inline=True)
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
                embed.add_field(
                    name="Hobbies ", value=f"{user_data['hobbies']}", inline=True
                )
                embed.add_field(
                    name="About me ", value=f"{user_data['biography']}", inline=False
                )
                embed.set_footer(
                    text=f"{interaction.guild.name}",
                    icon_url=interaction.guild.icon.url,
                )

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
            try:
                await user_embed.user_reply(
                    user,
                    "You Don't Have a Profile \n Click the `CREATE` button to create a profile",
                )
                await interaction.response.defer()
                bucket.reset()

            except:
                await interaction.response.send_message(
                    "You Don't Have a Profile \n Click the `CREATE` button to create a profile",
                    ephemeral=True,
                )
                await asyncio.sleep(60)
                await interaction.delete_original_response()
                bucket.reset()
