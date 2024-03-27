from GUIFramework.BaseWindow import *

class ChatWindow(BaseWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = "127.0.0.1:12345"