import asyncio
import discord

from discord.ext import commands
from core import embed
from model import queries
from core.config_parser import BotConfigs


bot_configs = BotConfigs()

from core.profile_data import profile_embed

# Class initialized
user_in_db = queries.PROFILEque()
user_embed = embed.Embed()


async def bump(bot, cooldown, interaction , button):

    #cooldown shit
    interaction.message.author = interaction.user
    bucket = cooldown.get_bucket(interaction.message)
    retry = bucket.update_rate_limit()

    user = await bot.fetch_user(interaction.user.id)
    role = discord.utils.get(
        interaction.guild.roles, id=bot_configs.role("premium_role_id")
    )

    if role in interaction.user.roles:
        await user.send("premium user should use the /bump commands")
        bucket.reset()

    else:
        if user_in_db.get_user(user.id):
            if retry:
                second = round(retry, 1)
                hours = retry // 3600
                minutes = hours * 60

                day = hours / 24
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


                profile_embed_data = await profile_embed(user, interaction)

                async def chn_send(channel):

                    embed, file = profile_embed_data
                    
                    if file:
                        await channel.send(file=file, embed=embed)
                    
                    else:
                        await channel.send(embed=embed)


                if male in interaction.user.roles:
                    await channel_male.send(f"{user.mention}")
                    await chn_send(channel_male)

                elif female in interaction.user.roles:
                    await channel_female.send(f"{user.mention}")
                    await chn_send(channel_female)

                else:
                    await channel_other.send(f"{user.mention}")
                    await chn_send(channel_other)
                    
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
