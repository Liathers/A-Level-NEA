from BaseClass import *

class BaseEncrypt(BaseClass):
    def __init__(self, action, key, message):
        super().__init__()

        self.action = action
        self.key = key
        self.message = message

    def doAction(self):
        if self.action == 0:
            return self.encrypt()
        elif self.action == 1:
            return self.decrypt()
        else:
            self.output("[Error] Improper action: Provided action is invalid, returning provided message")
            return self.message

    def encrypt(self):
        self.output("[Warning] Encryption function not created!")

    def decrypt(self):
        self.output("[Warning] Decryption function not created!")