#Using this class as a base for all allows for global functions that don't need to be repeated several times
class BaseClass:
    def __init__(self):
        print(f"Initialising Class:{self.__class__.__name__}")

    #Allows for print statements to be traced to specific classes easier
    def output(self, message):
        print(f"[Class:{self.__class__.__name__}] {message}")