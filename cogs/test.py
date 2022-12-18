from discord.ext import commands
import discord
import asyncio

yes_thumb = '👍'
no_thumb = "👎"

class Test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.message.delete()
        msg = await ctx.send("pong")
        #message = await ctx.send('test')
        
        pencil = "⚠️"
        laugh = "😍"
        add = "💔"
        await msg.add_reaction(yes_thumb)
        await msg.add_reaction(no_thumb)
        #await msg.add_reaction(pencil)

        #await msg.add_reaction(add)
        #await msg.add_reaction(laugh)
    
    """
    #events
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, ctx):
        if reaction.message.author.bot:     
            if reaction.emoji == yes_thumb :
                await ctx.send("yep")
                
            elif reaction.emoji == no_thumb:
                await ctx.send("hello")
    """

    @commands.command()
    async def check(self, ctx, user: discord.Member):
        #await ctx.message.delete()
        #await ctx.channel.send("My prefix")
        await ctx.reply('Hello!')
        await ctx.reply(user)

    
    @check.error
    async def check_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please pass all required arguments")
    


    @commands.command() #name='feedback', help='Ask person for feedback'
    async def roll(self, ctx):
        message = await ctx.send('Are you enjoying this bot? \n :thumbsup: :-1: ')

        thumb_up = '👍'
        thumb_down = '👎'

        await message.add_reaction(thumb_up)
        await message.add_reaction(thumb_down)

        def check(reaction, user):
            return user == ctx.author and str(
            reaction.emoji) in [thumb_up, thumb_down]

        member = ctx.author

        
        try:
            reaction, user = await self.bot.wait_for("reaction_add", timeout=10.0, check=check)

            if str(reaction.emoji) == thumb_up:
                await ctx.send('Thank you for your feedback')


            if str(reaction.emoji) == thumb_down:
                await ctx.send('Sorry you feel that way')

        except:
            return ''

async def setup(bot):
    await bot.add_cog(Test(bot))
