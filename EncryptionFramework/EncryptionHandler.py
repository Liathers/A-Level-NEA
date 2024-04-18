from BaseClass import *

from EncryptionFramework.CaesarCipherEncrypt import *

#This class is used to handle the ecryption-related actions within the program
class EncryptionHandler(BaseClass):
    def __init__(self):
        super().__init__()

#TODO ACTIONS
#Action 0 is encrypt
#Action 1 is decrypt

#When an action is needed, allow the user to select the algorithm used, the key, the action done and also the message
#to be encrypted
    def doAction(self, action, algorithm, key, message):
#If algorithm is 0, use a caesar chipher to encrypt the message
        if algorithm == "caesarcipher":
            return CaesarCipherEncrypt(action, key, message).doAction()
#If the provided algorithm is incorrect, notify the user and return the original message
        else:
            self.output("[Error] Improper algorithm: Provided algorithm is invalid, returning provided message")
            return message