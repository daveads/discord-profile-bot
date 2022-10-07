from discord.ext import commands
import asyncio
from model import profile

from model import queries

# class initialized
user_in_db = queries.PROFILEque()

class Profile(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot 
        self.profile_data = {}


    @commands.guild_only()
    @commands.command()
    async def profile(self, ctx):
        
        await ctx.send("check dm")
        await ctx.channel.purge(limit=2)   
        print(f'user profile id {ctx.author.id}')

        questions = {

        "name" : "what's your name ?",
        "location": "where are you from ?",
        "height" : "How tall are you? ",
        "dating_status" : "Briefly say your dating status! ",
        "looking_for":"What are you looking for? Type None if you don't want to share!",
        "hobbies" : "What are your hobbies?",
        "biography" : "Please write a biography, under 200 characters!"
        }

        user = await self.bot.fetch_user(ctx.author.id)
        print(user, "username!!!!!!!!!!!!", ctx.author)

        if user_in_db.get_user(ctx.author.id):
            await user.send("you have a profile created already")

        else:

            for ques in questions:
            
                try:
                    #await asyncio.sleep(1)
                    await user.send(questions[ques])
                    await asyncio.sleep(2)

                    msg = await self.bot.wait_for("message", timeout=65.0)

                    if msg.content:
                        self.profile_data[ques] = msg.content
                        await asyncio.sleep(2)
                        continue
                
                    else:
                        await user.send("Technical issues ")
                        await user.send("Contact the Admin or Engineer")
                        break 
       

                except asyncio.TimeoutError: #test
                    await user.send("Time out")
                    await user.send("You were too slow to answer!")
                    break


            if len(self.profile_data.keys()) == 7:
                print(self.profile_data)
                profile.profile_data(str(ctx.author),
                                     str(ctx.author.id),
                                     self.profile_data['name'],
                                     self.profile_data['location'],
                                     self.profile_data['height'],
                                     self.profile_data['dating_status'],
                                     self.profile_data['looking_for'],
                                     self.profile_data['hobbies'],
                                     self.profile_data['biography'],
                )

                await user.send("Profile created !")
                

            else:
                pass

    @profile.error
    async def profile_command_error(self, ctx, error):

        #comment out
        if isinstance(error, commands.CommandInvokeError):
            user = await self.bot.fetch_user(ctx.author.id)
            await user.send("can't execute action on DM")

                

    

async def setup(bot):
    await bot.add_cog(Profile(bot))