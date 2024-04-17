from pygit2 import Repository

import random
import time

from BaseClass import *
from WindowManager import *
from SocketsFramework import *
from EncryptionFramework.EncryptionHandler import *
from SocketsFramework.SocketsHandler import *


class Client(BaseClass):
#Creates the base variables for the client
    def __init__(self):
        super().__init__()
        self.output(f"Commit; {self.getBranchCommit()}")

#Initialise the WindowManager so GUI-relate things can be done
        self.windowManager = WindowManager(self.getBranchCommit())
        self.encryptionHandler = EncryptionHandler()
        self.socketsHandler = SocketHandler()

#This is used for local version control using github branches
#This will potentially be depreciated when the project is completed
    def getBranchCommit(self):
        try:
            repo = Repository("./")
            headRef = repo.head
            currentBranch = headRef.shorthand

            headCommit = repo.revparse_single('HEAD')
            commitSha = headCommit.hex[:7]
            return f"{currentBranch}_{commitSha}"
        except:
            return "branch_commit not found; missing repo?"

#This function is used during development for starting the script for debugging
    def devStart(self):
        self.windowManager.createWindow()
        self.windowManager.createMainWindow()
        self.windowManager.createChatWindow()
        #windowManager.createConnectionWindow()
        
        self.windowManager.loopWindow() #Nothing can be processed beyond this point
        #TODO: Threading might be useful for logic

#This function is used during development to test the functionality of the Ecryption Framework
    def encryptionTest(self):
        self.output("This is an encryption test!")
        encrypted = self.encryptionHandler.doAction(0, 0, "9", "This is pretty cool!")
        decrypted = self.encryptionHandler.doAction(1, 0, "9", encrypted)
        self.output(f"Encrypted message: {encrypted}")
        self.output(f"Decrypted message: {decrypted}")

#This function is used during development to test the functionality of the Socket Framework server
    def socketServerTest(self):
        self.output("This is a socket server test!")
        self.socketsHandler.createSocketSession("0.0.0.0", 20000)

#This function is used during development to test the functionality of the Socket Framework client
    def socketClientTest(self):
        self.output("This is a socket client test!")
        self.socketsHandler.connectToSocketServerSession("127.0.0.1", 20000, f"Test_User_{random.randint(1,999)}")
        
        self.output("Allowing user input")
        test = True
        while test:
            time.sleep(0.5)
            message = input()
            if message == "standby":
                self.output("Looping indefinately")
                while True:
                    1 == 1
            if message == "exit":
                self.socketsHandler.clientSocket.stop()
                self.output("Closing socket manually")
                exit(0)
            else:
                self.socketsHandler.clientSocket.sendMessage(message)

    def socketClientTest2(self):
        self.output("This is a socket client test!")
        self.socketsHandler.connectToSocketServerSession("127.0.0.1", 20000, f"Test_User_{random.randint(1,999)}")

client = Client()
#client.devStart()
#client.encryptionTest()
#client.socketServerTest()
client.socketClientTest()