from BaseClass import *
from WindowManager import *

class Client(BaseClass):
#Creates the base variables for the client
    def __init__(self):
        super().__init__()

#Initialise the WindowManager so GUI-relate things can be done
        self.windowManager = WindowManager()

#Allows for print statements to be traced to specific classes easier

#This function is used during development for starting the script for debugging
    def devStart(self):
        self.windowManager.createWindow()
        self.windowManager.createMainWindow()
        #windowManager.createChatWindow()
        #windowManager.createConnectionWindow()
        self.windowManager.loopWindow()

client = Client()
client.devStart()