from GUIFramework.BaseWindow import *

class ConnectionWindow(BaseWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = "Connecting"
        #This is probably not needed