import tkinter as tk
import tkinter.ttk as ttk

#Initialises class
class WindowManager:
    def __init__(self):
        self.windowRoot = None
        self.debugMessageLabel = None
        print("Initialising WindowManager.py")

#Output message with name of class for easy debugging once all the classes are being used in conjunction
    def output(self, message):
        print(f"[WindowManager] {message}")

#This will update the text within the DebugFrame once it has been created within the window
        if self.debugMessageLabel is not None:
            self.debugMessageLabel.config(text=f"WindowManager: {message}")

#Creates the window and configures parameters
    def createWindow(self):
        self.output("Creating Window")
        self.windowRoot = tk.Tk()
        self.windowRoot.resizable(0, 0)
        self.windowRoot.geometry("854x480")
        self.windowRoot.title("NEA Project | v1")

#Creates frames for the windowRoot
    def createWindowFrames(self):
        self.output("Creating Frames")
#This will be used for options and inputs reguarding entering a chatroom
        self.connectRoomFrame = ttk.LabelFrame(self.windowRoot)
        self.connectRoomFrame.config(text="Connect to Chatroom", height=212, width=560)
        self.connectRoomFrame.grid(column=0, row=0, padx=10, pady=2)
        self.connectRoomFrame.grid_propagate(False)

#This will be used for options and inputs reguarding creating a chatroom
        self.createRoomFrame = ttk.LabelFrame(self.windowRoot)
        self.createRoomFrame.config(text="Create a Chatroom", height=212, width=560)
        self.createRoomFrame.grid(column=0, row=1, padx=10)
        self.createRoomFrame.grid_propagate(False)

#This will be used alongside console outputs once setup
        self.debugFrame = ttk.LabelFrame(self.windowRoot)
        self.debugFrame.config(text="Debug Information", height=40, width=560)
        self.debugFrame.grid(column=0, row=2, padx=10, pady=2)
        self.debugFrame.grid_propagate(False)

#This will be used to allow the user to alter and edit settings surrounding the program
        self.settingsFrame = ttk.LabelFrame(self.windowRoot)
        self.settingsFrame.config(text="Program Settings", height=468, width=264)
        self.settingsFrame.grid(column=1, row=0, rowspan=3, pady=2)
        self.settingsFrame.grid_propagate(False)

#Appends widgets to the DebugFrame
    def createDebugFrameWidgets(self):
        self.output("Creating DebugFrame Widgets")
        self.debugMessageLabel = ttk.Label(self.debugFrame)
        self.debugMessageLabel.config(text="None", width=92)
        self.debugMessageLabel.grid(column=0, row=0)

#Appends widgets to settingsFrame
    def createSettingsFrameWidgets(self):
        self.output("Creating SettingsFrame Widgets")

#Loops the window
    def loopWindow(self):
        self.output("Looping Window")
        self.windowRoot.mainloop()

#Constructs the window by calling different functions within the Class
    def constructWindow(self):
        self.output("Constructing Window")
        self.createWindow()
        self.createWindowFrames()

        self.createDebugFrameWidgets()
        self.createSettingsFrameWidgets()

        self.loopWindow()

window = WindowManager()
window.constructWindow()