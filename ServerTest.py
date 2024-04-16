from pygit2 import Repository

import random
import time

from BaseClass import *
from WindowManager import *
from SocketsFramework import *
from EncryptionFramework.EncryptionHandler import *
from SocketsFramework.SocketsHandler import *


class ServerTest(BaseClass):
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

#This function is used during development to test the functionality of the Socket Framework server
    def socketServerTest(self):
        self.output("This is a socket server test!")
        self.socketsHandler.createSocketSession("0.0.0.0", 20000)

server = ServerTest()
server.socketServerTest()