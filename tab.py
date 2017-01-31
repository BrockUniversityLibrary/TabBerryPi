
# TabBerryPi #

import ConfigParser

b1,b2,b3,b4 = [dict()]*4



def init_setup():
	"""
	Setup payload of buttons
	"""
	c = ConfigParser.ConfigParser()
	c.read("settings.py")
	b1[c.get('b1','label')]= c.get('b1','url')

def check_connect():
	"""
	Checks if connection still good
	"""

def tab_loop():
	"""
	Main bulk of program
	"""


if __name__ == "__main__":
	init_setup()
	tab_loop()
