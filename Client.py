from pygit2 import Repository

from BaseClass import *
from WindowManager import *

class Client(BaseClass):
#Creates the base variables for the client
    def __init__(self):
        super().__init__()
        self.output(f"Commit; {self.getBranchCommit()}")

#Initialise the WindowManager so GUI-relate things can be done
        self.windowManager = WindowManager(self.getBranchCommit())

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
        self.windowManager.loopWindow()

client = Client()
client.devStart()