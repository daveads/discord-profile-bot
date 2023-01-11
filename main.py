import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import asyncio
from model import profile
from view.profile_btn import Profile


from typing import Literal, Optional
from discord.ext.commands import Greedy, Context


# intializing database
profile.main()

load_dotenv()
token = os.getenv('TOKEN')


from core.config_parser import BotConfigs
bot_configs = BotConfigs()

from core.bot  import ProfileBot

load_dotenv()
bot = ProfileBot()

async def load():
    for f in os.listdir("./cogs"):
        if f.endswith(".py"):
            await bot.load_extension(f'cogs.{f[:-3]}')


@bot.command()
@commands.is_owner()
async def prep(ctx: commands.Context):
    #await ctx.message.channel.purge(limit=5)
    await ctx.message.channel.purge(limit=10)
    await ctx.send(file=discord.File(bot_configs.profile_image()))

    info = """** Create your own profile to describe yourself and start meeting others!** \n\n  📝 ➤ Edit Profile \n  `Update your information` \n\n 🔎 ➤ Preview Profile \n  `Preview your current profile!` \n\n 📢 ➤ Bump the server \n  `cooldown: (Normal 3d)` \n\n  📁 ➤ ~~Upload Selfies~~ \n `Must be selfie verified!` 
           \n **For premium, User's should use the `/bumpp` command *~~Coming soon~~* ** \n *The `/bumpp command cost $3 monthly` message moderators to get more details on that* \n  `cooldown: (Normal: 12hrs)` 
            \n **Required Roles to create a profile**\n`Gender, Age, Orientation, Dating-status, Dm-status, Height`  """

    await ctx.send(info, view=Profile(bot))

#https://gist.github.com/AbstractUmbra/a9c188797ae194e592efe05fa129c57f
@bot.command()
@commands.guild_only()
@commands.is_owner()
async def sync(
  ctx: Context, guilds: Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
    if not guilds:
        if spec == "~":
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "^":
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await ctx.bot.tree.sync()

        await ctx.send(
            f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
        )
        return

    ret = 0
    for guild in guilds:
        try:
            await ctx.bot.tree.sync(guild=guild)
        except discord.HTTPException:
            pass


        else:
            ret += 1

    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")


bot.remove_command('help')  
async def main():
    await load()
    await bot.start(token)

asyncio.run(main())