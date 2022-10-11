from discord.ext import commands

#json data
from core import configs

# class initialized
data = configs.Datajson()

class ready(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    
    #@commands.guild_only()
    @commands.Cog.listener()
    async def on_message(self, message):
        """
        if message.author.id == self.bot.user.id:
            return 
        """

        
        if message.content.lower() == "help":
            return '' #await message.author.send("help on the way")
    

    @commands.Cog.listener()
    async def on_ready(self):
        channel = self.bot.get_channel(data.profile_channel)
        print(f'{self.bot.user}:Bot Logged In')
        await channel.send("!run")

    

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandNotFound):
            await ctx.send("command not found")


async def setup(bot):
    await bot.add_cog(ready(bot))
