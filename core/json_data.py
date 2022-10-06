import json
f = open('./config.json')
data = json.load(f)

class Datajson():

    def __init__(self):

        self.profile_channel = data.get('profile_channel') 
        self.profile_commands_admin = data.get('profile_commands_admin')
        self.male_channel = data.get('male_channel')
        self.female_channel = data.get('female_channel')
        self.others_channel = data.get('others_channel')
        self.owner = data.get('owner')