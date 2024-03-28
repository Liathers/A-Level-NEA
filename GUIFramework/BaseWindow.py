import tkinter as tk
import tkinter.ttk as ttk

#This class serves as the base for every different window within the program
class BaseWindow:
    def __init__(self, parent):
        print(f"Initialising Class:{self.__class__.__name__}")
        self.name = None
        self.parent = parent

#Creates the frame that everything on the window will be based upon
        self.frame = ttk.Frame(self.parent)
        self.frame.pack(expand=True, fill="both")

#Allows for print statements to be traced to specific classes easier
    def output(self, message):
        print(f"[Class:{self.__class__.__name__}] {message}")

#Appends to frame to the parent provided to the class
    def addToParent(self):
        self.output(f"Appending tab \"{self.name}\" to WindowNotebook")
        self.parent.add(self.frame, text=self.name)
        self.addFrames()
        self.addWidgets()

#Define function in case parent class does not define
    def addFrames(self):
        self.output("[Warning] No frames have been defined!")

#Define function in case parent class does not define
    def addWidgets(self):
        self.output("[Warning] No widgets have been appended!")