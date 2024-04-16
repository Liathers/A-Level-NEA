#Using this class as a base for all allows for global functions that don't need to be repeated several times
class BaseClass:
    def __init__(self):
        self.title = self.__class__.__name__
        print(f"Initialising Class:{self.title}")

    #Allows for print statements to be traced to specific classes easier
    def output(self, message):
        print(f"[Class:{self.title}] {message}")