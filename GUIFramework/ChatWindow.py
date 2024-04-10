from GUIFramework.BaseWindow import *

class ChatWindow(BaseWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = "Connection IP:Port"
        
        self.chatText = None
        self.chatLines = 1

        self.inputMessage = tk.StringVar()

    def addFrames(self):
#Create a frame what will hold the live chat
        self.chatFrame = ttk.LabelFrame(self.frame)
        self.chatFrame.config(text="Chat", height=391, width=620)
        self.chatFrame.grid(column=0, row=0, padx=(10,5),pady=4)
        self.chatFrame.grid_propagate(False)

#Create a frame that will contain the inputs for the chat
        self.inputFrame = ttk.LabelFrame(self.frame)
        self.inputFrame.config(text="Input Message", height=51, width=830)
        self.inputFrame.grid(column=0, row=1, columnspan=2, padx=10, pady=(0,4))
        self.inputFrame.grid_propagate(False)

#Create a frame that will contain all currently connected users
        self.usersFrame = ttk.LabelFrame(self.frame)
        self.usersFrame.config(text="Connected Users", height=391, width=200)
        self.usersFrame.grid(column=1, row=0, padx=(5,10), pady=4)
        self.usersFrame.grid_propagate(False)

        self.output("Appended frames")

    def addWidgets(self):
        self.output("Apending Widgets..")
        self.addInputWidgets()
        self.addChatWidgets()

    def addInputWidgets(self):
        inputTextEntry = ttk.Entry(self.inputFrame)
        inputTextEntry.config(textvariable=self.inputMessage, width=119)
        inputTextEntry.grid(column=0, row=0, padx=7)

        inputSubmitEntry = ttk.Button(self.inputFrame)
        inputSubmitEntry.config(text="Send Message")
        inputSubmitEntry.grid(column=1, row=0, padx=(0,7))

        self.output("Appended inputFrame widgets")

    def addChatWidgets(self):
        self.chatText = tk.Text(self.chatFrame)
        self.chatText.config(state=tk.DISABLED, height=22, width=74)
        self.chatText.grid(column=0, row=0, padx=10, pady=4)

        self.output("Appended chatFrame widgets")

    def addChatText(self, name, message):
        self.output(f"Adding text: '{message}' to {self.name.lower()} from '{name}'")

        self.chatText.config(state=tk.NORMAL)
        self.chatText.insert(f"{self.chatLines}.0", f"{name}: {message}\n")
        self.chatText.config(state=tk.DISABLED)

        self.chatLines += 1