
import pyrebase
import pyautogui
import time
import getpass
from math import sqrt, pi

class FBData:
	def __init__(self):
		self.config = {
			"apiKey": "AIzaSyDtENByjPjjrXyoBWEr7Tr4to9ypS_EU38",
			"authDomain": "decisionkitchen.firebaseapp.com/",
			"databaseURL": "https://decisionkitchen.firebaseio.com/",
			"storageBucket": "decisionkitchen.appspot.com"
		}

		self.firebase = pyrebase.initialize_app(self.config)
		self.db = self.firebase.database()

	def start(self):
		print("hello")
		users = self.db.child("groups").child('2120b04c-bd1e-42c8-abf1-08fd4fde8133').get()
		print(users.val())

	def streamHandler(self, post):
		print("back")


FBData().start()