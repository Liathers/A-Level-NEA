import tkinter as tk
import tkinter.ttk as ttk
from pygit2 import Repository

from GUIFramework.MainWindow import *
from GUIFramework.ConnectionWindow import *
from GUIFramework.ChatWindow import *

class WindowManager:
#Creates the base variables for window management
    def __init__(self):
        print(f"Initialising {__class__.__name__}")
        self.windowRoot = None
        self.windowNotebook = None

#These refer to the respective frames for each respective window
        self.mainWindow = None
        self.chatWindow = None
        self.connectionWindow = None

#Allows for print statements to be traced to specific classes easier
    def output(self, message):
        print(f"[Class:{self.__class__.__name__}] {message}")
        
        if self.mainWindow is not None and self.mainWindow.debugMessageLabel is not None:
            self.mainWindow.debugMessageLabel.config(text=f"[WindowManager] {message}")

#This is used for local version control using github branches
#This will be depreciated when the project is completed
    def getBranch(self):
        try:
            repo = Repository("./")
            headRef = repo.head
            currentBranch = headRef.shorthand

            headCommit = repo.revparse_single('HEAD')
            commitSha = headCommit.hex[:7]
            return f"{currentBranch}_{commitSha}"
        except:
            return "branch_commit not found"

#Complete the initial setup for the window, inclusing the size and window
    def createWindow(self):
        self.output("Creating Window")
        self.windowRoot = tk.Tk()
        self.windowRoot.resizable(0, 0)
        self.windowRoot.geometry("854x480")
        self.windowRoot.title(f"Computer Science NEA Project | {self.getBranch()}")

#Create the notebook widget in preparation for the respective frames
        self.windowNotebook = ttk.Notebook(self.windowRoot)
        self.windowNotebook.pack(expand=True, fill="both", anchor=tk.CENTER)

#Loop the window so it can be interacted with
    def loopWindow(self):
        self.output("Looping Window")
        self.windowRoot.mainloop()

#Initialise the Main Window, and add it to the notebook widget
    def createMainWindow(self):
        self.output("Creating Main Window")
        self.mainWindow = MainWindow(self.windowNotebook)
        self.mainWindow.addToParent()

#=====================================================================================
#This is temporary as the GUI gets developed
    def createChatWindow(self):
        self.output("Creating Chat Window")
        self.chatWindow = ChatWindow(self.windowNotebook)
        self.chatWindow.addToParent()

#This is temporary as the GUI gets developed
    def createConnectionWindow(self):
        self.output("Creating Connection Window")
        self.connectionWindow = ConnectionWindow(self.windowNotebook)
        self.connectionWindow.addToParent()
#=====================================================================================