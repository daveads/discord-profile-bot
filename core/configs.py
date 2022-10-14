import json
import logging
from rich.logging import RichHandler

#logging.basicConfig(format='%(levelname)s ::: %(message)s')
logging.basicConfig(format='::: %(message)s', handlers=[RichHandler()])

# json
f = open('./config.json')
data = json.load(f)

class Datajson():

    def __init__(self):

        #channels
        self.profile_channel = data.get('profile_channel') 
        self.profile_commands_admin = data.get('profile_commands_admin')
        self.male_channel = data.get('male_channel')
        self.female_channel = data.get('female_channel')
        self.others_channel = data.get('others_channel')

        #owner id
        self.owner = data.get('owners_id')

        #roles
        self.premium_role = data.get('premium_role_id')
        self.male_role = data.get('male')
        self.female_role = data.get('female')



for i in data:

    if data.get(i):
        pass

    else:
        logging.warning(f"<<<{i.upper()}>>> CONFIG MISSING")