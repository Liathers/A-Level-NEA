from WindowManager import *

class Client:
#Creates the base variables for the client
    def __init__(self):
        self.windowManager = None

#This function is used during development for starting the script for debugging
    def devStart(self):
        self.windowManager = WindowManager()
        self.windowManager.createWindow()
        self.windowManager.createMainWindow()
        #windowManager.createChatWindow()
        #windowManager.createConnectionWindow()
        self.windowManager.loopWindow()

client = Client()
client.devStart()