from discord.ext import commands
import discord
import asyncio
from discord import app_commands


class Cooldown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self.cooldown = CooldownMapping()

    @app_commands.describe(
        first_value="Input user id",
    )
    @app_commands.command(name="cooldownuser", description="search for a user profile")
    async def cooldwn(self, interaction: discord.Interaction, first_value: str):
        """/cooldown"""

        try:
            convert_id = int(first_value)

            user = await self.bot.fetch_user(convert_id)

            # self.cooldown.reset_cooldown(user)

        except:
            await interaction.response.send_message("Not working")


async def setup(bot):
    await bot.add_cog(Cooldown(bot))
