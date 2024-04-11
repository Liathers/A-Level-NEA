import tkinter as tk
import tkinter.ttk as ttk

from BaseClass import *
from GUIFramework.MainWindow import *
from GUIFramework.ChatWindow import *

class WindowManager(BaseClass):
#Creates the base variables for window management
    def __init__(self, version):
        super().__init__()

        self.version = version
        self.windowRoot = None
        self.windowNotebook = None

#These refer to the respective frames for each respective window
        self.mainWindow = None
        self.chatWindow = None
        self.connectionWindow = None

#Allows for print statements to be traced to specific classes easier
    def output(self, message):
        super().output(message)

        if self.mainWindow is not None and self.mainWindow.debugMessageLabel is not None:
            self.mainWindow.debugMessageLabel.config(text=f"[WindowManager] {message}")

#Complete the initial setup for the window, inclusing the size and window
    def createWindow(self):
        self.output("Creating Window")
        self.windowRoot = tk.Tk()
        self.windowRoot.resizable(0, 0)
        self.windowRoot.geometry("854x480")
        self.windowRoot.title(f"Computer Science NEA Project | {self.version}")

#Create the notebook widget in preparation for the respective frames
        self.windowNotebook = ttk.Notebook(self.windowRoot)
        self.windowNotebook.pack(expand=True, fill="both", anchor=tk.CENTER)

#Ensure that the program does things gracefully when the window gets closed
        self.windowRoot.protocol("WM_DELETE_WINDOW", self.closeWindow)

#Do things once the window gets closed by the user
    def closeWindow(self):
        self.output("Window closed; exiting program")
        exit(0)

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
        self.chatWindow = ChatWindow(self.windowNotebook, False)
        self.chatWindow.addToParent()
#=====================================================================================