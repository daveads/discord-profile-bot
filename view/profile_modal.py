import discord
from model import profile
import asyncio

class Creatprofile(discord.ui.Modal, title='profile'):
    
    name = discord.ui.TextInput(
        label='Name',
        placeholder='Your name here...',
    )

    location = discord.ui.TextInput(
        label='Location',
        style=discord.TextStyle.short,
        placeholder='Where are you from',
        required=False,
        max_length=300,
    )

    looking_for = discord.ui.TextInput(
        label='looking for',
        placeholder="What are you looking for? Type None if you don't want to share!",
    )

    hobbies = discord.ui.TextInput(
        label='hobbies',
        placeholder='What are your hobbies?',
    )
    

    biography = discord.ui.TextInput(
        label='biography',
        placeholder='Please write a biography, under 200 characters!',
    )
    

    async def on_submit(self, interaction: discord.Interaction):

        profile.profile_data(str(interaction.user),
                             str(interaction.user.id),
                             self.name.value,
                             self.location.value,
                             self.looking_for.value,
                             self.hobbies.value,
                             self.biography.value,
                )

        """
        print(interaction.user)
        print(interaction.user.id)
        print(self.name.value)
        print(self.location.value)
        print(self.looking_for.value)
        print(self.hobbies.value)
        print(self.biography.value)
        """

        await interaction.response.send_message(f'profile created', ephemeral=True)
        await asyncio.sleep(20)
        await interaction.delete_original_response()

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)
