from discord.ext import commands
import discord



#bot_configs = BotConfigs()


class ProfileBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        description = '''Discord profile bot '''
        super().__init__(command_prefix=commands.when_mentioned_or('$'), intents=intents, description=description)

    async def setup_hook(self) -> None:
        #self.add_view(StartVerify(self))
        pass

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        #c = self.get_guild(bot_configs.guild_id())
        #print("guild**********", c)
        print('------')