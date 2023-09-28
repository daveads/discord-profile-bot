import discord
import asyncio
from core.config_parser import BotConfigs

botconfig = BotConfigs()


class Announce(discord.ui.Modal, title="Profile Bot"):
    Title = discord.ui.TextInput(
        label="Title",
        style=discord.TextStyle.short,
        required=True,
        max_length=100,
    )

    announcement = discord.ui.TextInput(
        label="Announcement",
        style=discord.TextStyle.long,
        required=True,
        max_length=300,
    )

    async def on_submit(self, interaction: discord.Interaction):
        announce_chn = discord.utils.get(
            interaction.guild.channels, id=botconfig.channel("announcement_chn")
        )

        embed = discord.Embed(
            title=f"{self.Title.value}",
            color=discord.Colour(0x2F3136),
        )

        embed.add_field(name="INFO", value=self.announcement.value)
        embed.set_footer(text="From @daveads")

        await announce_chn.send(embed=embed)
        await interaction.response.send_message(
            "**Announcement Sent!**", ephemeral=True
        )
        await asyncio.sleep(20)
        await interaction.delete_original_response()
