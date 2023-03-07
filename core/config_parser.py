from pprint import pprint

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib


import logging
from rich.logging import RichHandler

logging.basicConfig(format='%(levelname)s ::: %(message)s', handlers=[RichHandler()])


class BotConfigs:
    def __init__ (self):
        with open("bot_config.toml", "rb") as f:
            self.data = tomllib.load(f)
        
    def profile_image(self):
        image = "img/" + self.data['image']['profile_image']
        return image


    def role(self, role):
        if role in self.data["user_roles"]:
            return self.data["user_roles"][role]


    def admin(self, chn):
        if  chn in self.data['admins']:
            return self.data["admins"][chn]


    def channel(self, chn):
        if chn in self.data['channels']:
            return self.data['channels'][chn]


    def gender(self, gender):
        if gender in self.data["gender"]:
            return self.data['gender'][gender]


    def age(self, age):
        if age in self.data['age']:
            return self.data['age'][age]


    def orientaion(self,orient):
        if orient in self.data["orientation"]:
            return self.data['orientation'][orient]


    def datingstatus(self, status):
        if status in self.data["datingstatus"]:
            return self.data["datingstatus"][status]


    def dmstatus(self, status):
        if status in self.data['dmstatus']:
            return self.data['dmstatus'][status]


    def height(self, heig):
        if heig in self.data['height']:
            return self.data['height'][heig]