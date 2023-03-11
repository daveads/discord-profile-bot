MY_CONSTANT = 42


"""
constant variable....
"""


import sqlite3
from datetime import datetime
from os.path import exists

con = sqlite3.connect("profile.db")
CUR = con.cursor()