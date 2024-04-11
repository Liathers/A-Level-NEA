from pygit2 import Repository

from BaseClass import *
from WindowManager import *
from SocketsFramework import *
from EncryptionFramework.EncryptionHandler import *


class Client(BaseClass):
#Creates the base variables for the client
    def __init__(self):
        super().__init__()
        self.output(f"Commit; {self.getBranchCommit()}")

#Initialise the WindowManager so GUI-relate things can be done
        self.windowManager = WindowManager(self.getBranchCommit())
        self.encryptionHandler = EncryptionHandler()

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

    def encryptionTest(self):
        self.output("This is an encryption test!")
        self.encryptionHandler.encrypt(0, "0", "This is a test")

client = Client()
#client.devStart()
client.encryptionTest()