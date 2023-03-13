import discord
from core.config_parser import BotConfigs

bot_configs = BotConfigs()

#premium level
async def premiumR(interaction):
    level1 = discord.utils.get(interaction.guild.roles, id=bot_configs.premium("level1"))
    level2 = discord.utils.get(interaction.guild.roles, id=bot_configs.premium("level2"))
    level3 = discord.utils.get(interaction.guild.roles, id=bot_configs.premium("level3"))
    level4 = discord.utils.get(interaction.guild.roles, id=bot_configs.premium("level4"))
    level5 = discord.utils.get(interaction.guild.roles, id=bot_configs.premium("level5"))

    premObj = [level1, level2, level3, level4, level5 ]

    return premObj

