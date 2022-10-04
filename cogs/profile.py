from discord.ext import commands
import time
import asyncio

class Profile(commands.Cog):
    
    def __init__(self, bot):
        
        self.bot = bot
        self.pre= True 
    
    @commands.command()
    @commands.cooldown(1, 259200, commands.BucketType.user)
    async def profile(self, ctx):
        
        await ctx.send("check dm")
        await ctx.channel.purge(limit=200)   
        print(f'user profile {ctx.author.id}')

        questions = {

        "name" : "what's your name ?",
        "location": "where are you from ?",
        "Status" : "Briefly say your dating status! ",
        "height" : "How tall are you? ",
        "search_for":"What are you looking for? Type None if you don't want to share!",
        "hobbies" : "What are your hobbies?",
        "biography" : "Please write a biography, under 200 characters!"
        }

        user = await self.bot.fetch_user(ctx.author.id)
        print(user)
        profile_data = {}
        
        for ques in questions:
            
            try:
                await asyncio.sleep(1)
                await user.send(questions[ques])
                await asyncio.sleep(2)

            
                msg = await self.bot.wait_for("message", timeout=65.0)
            
                print(msg.content)

                if msg.content:
                    profile_data[ques] = msg.content
                    await asyncio.sleep(2)
                
                else:
                    await user.send("Technical issues ")
                    await user.send("Contact the Admin or Engineer")
                    break 
       

            except asyncio.TimeoutError: #test
                await user.send("Time out")
                await user.send("You were too slow to answer!")
                break

        if profile_data:
            print(profile_data)
            await user.send("Done!")
        else:
            ctx.command.reset_cooldown(ctx)
            
            

    
    @profile.error
    async def profile_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
                await ctx.send("if you are a premium user use the !bumpp command")
                cd = round(error.retry_after)
                hours = str(cd // 3600)
                minutes = str(cd % 60)
                await ctx.send(f"You have {hours} hours {minutes} minutes left")
                

    

async def setup(bot):
    await bot.add_cog(Profile(bot))



