from discord.ext import commands
import discord
from view.profile_btn import Profile

#bot_configs = BotConfigs()

import logging
from rich.logging import RichHandler

logging.basicConfig(format='::: %(message)s', handlers=[RichHandler()])
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class ProfileBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        description = '''Discord profile bot '''
        super().__init__(command_prefix=commands.when_mentioned_or('$'), intents=intents, description=description)

    async def setup_hook(self) -> None:
        #self.add_view(StartVerify(self))
        self.add_view(Profile(self))

    async def on_ready(self):
        #print()
        logger.info(f'Logged in as {self.user}')

        logger.info('------')
        #c = self.get_guild(bot_configs.guild_id())
        #print("guild**********", c)
        logger.info('------')