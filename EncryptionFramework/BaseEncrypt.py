from BaseClass import *

#This class serves as a base for all encryption algorithms that will be used within the program
class BaseEncrypt(BaseClass):
    def __init__(self, action, key, message):
        super().__init__()

#Define local variables for the used key, message sent, and what action is to be performed
        self.action = action
        self.key = key
        self.message = message

#This function attemptes to do an action based on the int recieved, it also returns the
#results of the action, or the original action if an invalid actions is provided by the user
    def doAction(self):
        if self.action == 0:
            return self.encrypt()
        elif self.action == 1:
            return self.decrypt()
        else:
            self.output("[Error] Improper action: Provided action is invalid, returning provided message")
            return self.message

#This is a base function for encrypting a message, this is defined in case the parent class doesn't have one defined
    def encrypt(self):
        self.output("[Warning] Encryption function not created!")

#This is a base function for decrypting a message, this is defined in case the parent class doesn't have one defined
    def decrypt(self):
        self.output("[Warning] Decryption function not created!")