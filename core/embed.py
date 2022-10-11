import discord

class Embed():

    def __init__(self):

        self.test = None

    async def user_reply(self, user, msg ):

        embed=discord.Embed(title="profile bot", description=f"{msg}", color=0xFF5733)
        #user = await self.bot.fetch_user(ctx.author.id)
        await user.send(embed=embed)


    async def user_profile_dm(self, ctx, title, desc):

        embed=discord.Embed(title=f"{title}", url="", description=f"{desc}", color=discord.Color.blue())
        #embed.set_image(url=(author.avatar_url))
        embed.set_thumbnail(url=ctx.author.avatar)
        
        pass