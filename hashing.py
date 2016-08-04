from hashlib import *

loginDict = {}

def login(loginDict):
  	loginDict.append(username)

def makeHash(password):
  return sha256(password.encode('utf-8')).hexdigest()

def prompt():
	user = input("What is your username?")
	password = input("What is your password?")
	if user in loginDict:
		pw = input("What is your password?")
		hashed_pw = makeHash(pw)
		if loginDict[user] == hashed_pw:
			print("Congrats! You're in.")
		else:
			print("Password incorrect")
	else: 
		username = input ("Please enter a username to sign up:")
		append.loginDict()
		pw = input("Please enter a 3 letter password to sign up:")
		hashed_pw == makeHash()
		loginDict[username] = hashed_pw 
done = False
while not done:
	prompt()
	