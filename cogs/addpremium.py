import discord
from discord.ext import commands
from core import configs
from core import premiumdate

#json 
data = configs.Datajson()

class Addpremium(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #premium_p
    @commands.command()
    @commands.has_any_role('admin', 'moderator')
    async def addbumpp(self, ctx, user: discord.Member, role = "premium_p", month=1):
        roleObj = discord.utils.get(ctx.guild.roles, name=role)

        if True: ## admin command channel
            if True: ## if user has a profile
                if roleObj in user.roles:
                    #print(role.id)

                    await ctx.send("user already have this role")

                else:
                    if role == "premium_p":
                        #print(user.id)
                        await user.add_roles(roleObj)
                        await ctx.send(f"{user.name} has been giving {roleObj.name} access")
                    else:
                        await ctx.send("You are only allowed to give **premium_p** role with this bot")
            else:
                await ctx.send("user doesn't have a profile")
        else:
            await ctx.send("command has to be run in the adminCommand channel")


    @commands.command()
    @commands.has_role('admin')
    async def mute(self, ctx, user: discord.Member, role="premium_p"):

        roleObj = discord.utils.get(ctx.guild.roles, name=role)
        if True: #admin command channel
            if True: #if user has role and user has a profile

                if roleObj in user.roles:

                    if role == "premium_p":
                        await user.remove_roles(roleObj)
                        await ctx.send("{} has been muted".format(user))

                    else:
                        await ctx.send("You are only allowed to give **premium_p** role with this bot")
                else:
                    await ctx.send("you doesn't have the role")

        else:
            await ctx.send("command can only be used in the admin channel")


    @addbumpp.error
    async def addbumpp_error(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            await ctx.send("only admin and moderator has the right to use this commands")

async def setup(bot):
    await bot.add_cog(Addpremium(bot))
