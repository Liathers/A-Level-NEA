from BaseClass import *

from EncryptionFramework.CaesarCipherEncrypt import *

#This class is used to handle the ecryption-related actions within the program
class EncryptionHandler(BaseClass):
    def __init__(self):
        super().__init__()

    def doAction(self, action, algorithm, key, message):
        self.output("Performing an encryption")
        self.output(f"Using algorithm {algorithm}")

        if algorithm == 0:
            return CaesarCipherEncrypt(action, key, message).doAction()
        else:
            self.output("[Error] Improper algorithm: Provided algorithm is invalid, returning provided message")
            return message