from GUIFramework.BaseWindow import *

class MainWindow(BaseWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = "Home"
        self.debugMessageLabel = None
        #self.frame is the fram required by the tab

#Append the frames that will be used within this window
    def addFrames(self):
        self.output("Appending Frames")

#Create the frame that will allow users to connect to different chatrooms
        self.connectionFrame = ttk.LabelFrame(self.frame)
        self.connectionFrame.config(text="Connect to a chatroom", height=197, width=560)
        self.connectionFrame.grid(column=0, row=0, padx=(10,5), pady=4)
        self.connectionFrame.grid_propagate(False)

#Create the frame that will allow the user to create a chatroom for others to join
        self.creationFrame = ttk.LabelFrame(self.frame)
        self.creationFrame.config(text="Create a chatroom", height=197, width=560)
        self.creationFrame.grid(column=0, row=1, padx=(10,5))
        self.creationFrame.grid_propagate(False)

#Create the frame that will display basic output information relating to the program
        self.debugFrame = ttk.LabelFrame(self.frame)
        self.debugFrame.config(text="Program Log", height=40, width=560)
        self.debugFrame.grid(column=0, row=2, padx=(10,5), pady=4)
        self.debugFrame.grid_propagate(False)

#Create the frame that will be used to control settings related to the program
        self.settingsFrame = ttk.LabelFrame(self.frame)
        self.settingsFrame.config(text="Program Settings", height=442, width=260)
        self.settingsFrame.grid(column=1, row=0, rowspan=3, padx=(5,10), pady=4)
        self.settingsFrame.grid_propagate(False)
#TODO Fix slight padding inconsistencies on padding for frames

#Append the widgets that will be used within this window
    def addWidgets(self):
        self.output("Appending widgets")

#Create the label for the program output, which will be edited when outputs are created
        self.debugMessageLabel = ttk.Label(self.debugFrame)
        self.debugMessageLabel.config(text="None", width=92)
        self.debugMessageLabel.grid(column=0, row=0)