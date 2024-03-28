from GUIFramework.BaseWindow import *

class MainWindow(BaseWindow):
    def __init__(self, parent):
        super().__init__(parent)

        self.name = "Home"
        self.debugMessageLabel = None
        #self.frame is the frame required by the tab
        self.connectionIPInput = tk.StringVar()
        self.connectionPortInput = tk.StringVar()
        self.connectionKeyInput = tk.StringVar()

#Append the frames that will be used within this window
    def addFrames(self):
#Create the frame that will allow users to connect to different chatrooms
        self.connectionFrame = ttk.LabelFrame(self.frame)
        self.connectionFrame.config(text="Connect to a chatroom", height=197, width=360)
        self.connectionFrame.grid(column=0, row=0, padx=(10,5), pady=4)
        self.connectionFrame.grid_propagate(False)

#Create the frame that will change settings related to connecting to a chatroom
        self.connectionSettingsFrame = ttk.LabelFrame(self.frame)
        self.connectionSettingsFrame.config(text="Connection Encryption Type", height=197, width=186)
        self.connectionSettingsFrame.grid(column=1, row=0, padx=(5,5))
        self.connectionSettingsFrame.grid_propagate(False)

#Create the frame that will allow the user to create a chatroom for others to join
        self.creationFrame = ttk.LabelFrame(self.frame)
        self.creationFrame.config(text="Host a chatroom", height=197, width=360)
        self.creationFrame.grid(column=0, row=1, padx=(10,5))
        self.creationFrame.grid_propagate(False)

#Create the frame that will change settings related to connecting to a chatroom
        self.creationSettingsFrame = ttk.LabelFrame(self.frame)
        self.creationSettingsFrame.config(text="Host Encryption Type", height=197, width=186)
        self.creationSettingsFrame.grid(column=1, row=1, padx=(5,5))
        self.creationSettingsFrame.grid_propagate(False)

#Create the frame that will display basic output information relating to the program
        self.debugFrame = ttk.LabelFrame(self.frame)
        self.debugFrame.config(text="Program Log", height=40, width=560)
        self.debugFrame.grid(column=0, row=2, columnspan=2, padx=(10,5), pady=4)
        self.debugFrame.grid_propagate(False)

#Create the frame that will be used to control settings related to the program
        self.settingsFrame = ttk.LabelFrame(self.frame)
        self.settingsFrame.config(text="Program Settings", height=442, width=260)
        self.settingsFrame.grid(column=2, row=0, rowspan=3, padx=(5,10), pady=4)
        self.settingsFrame.grid_propagate(False)
#TODO Fix slight padding inconsistencies on padding for frames
        self.output("Appended frames")

#Append the widgets that will be used within this window
    def addWidgets(self):
        self.output("Appending Widgets..")
        self.addConnectionWidgets()
        self.addDebugWidgets()

#Create the label for the program output, which will be edited when outputs are created
    def addDebugWidgets(self):
        self.debugMessageLabel = ttk.Label(self.debugFrame)
        self.debugMessageLabel.config(text="None", width=92)
        self.debugMessageLabel.grid(column=0, row=0)
        self.output("Appended debugFrame widgets")

#Creates the widgets for the connectionFrame
    def addConnectionWidgets(self):
        connectionLabelHeading = ttk.Label(self.connectionFrame)
        connectionLabelHeading.config(text="This will allow you to connect to a preexisting chatroom.")
        connectionLabelHeading.grid(column=0, row=0, padx=5)

        connectionIPEntryHeading = ttk.Label(self.connectionFrame)
        connectionIPEntryHeading.config(text="Chatroom IP:")
        connectionIPEntryHeading.grid(column=0, row=1, padx=5, sticky=tk.W)

        connectionIPEntry = ttk.Entry(self.connectionFrame)
        connectionIPEntry.config(textvariable=self.connectionIPInput, width=30)
        connectionIPEntry.grid(column=0, row=2, padx=5, sticky=tk.W)

        connectionPortEntryHeading = ttk.Label(self.connectionFrame)
        connectionPortEntryHeading.config(text="Chatroom Port:")
        connectionPortEntryHeading.grid(column=0, row=3, padx=5, sticky=tk.W)

        connectionPortEntry = ttk.Entry(self.connectionFrame)
        connectionPortEntry.config(textvariable=self.connectionPortInput, width=30)
        connectionPortEntry.grid(column=0, row=4, padx=5, sticky=tk.W)

        connectionKeyEntryHeading = ttk.Label(self.connectionFrame)
        connectionKeyEntryHeading.config(text="Chatroom Key:")
        connectionKeyEntryHeading.grid(column=0, row=5, padx=5, sticky=tk.W)

        connectionKeyEntry = ttk.Entry(self.connectionFrame)
        connectionKeyEntry.config(textvariable=self.connectionKeyInput, width=30)
        connectionKeyEntry.grid(column=0, row=6, padx=5, sticky=tk.W)

        connectionSubmitEntry = ttk.Button(self.connectionFrame)
        connectionSubmitEntry.config(text="Submit Connection")
        connectionSubmitEntry.grid(column=0, row=7, padx=5, pady=(7,0), sticky=tk.W)
        self.output("Appended connectionFrame widgets")