from BaseClass import *

class BaseEncrypt(BaseClass):
    def __init__(self, key, message):
        super().__init__()

        self.key = key
        self.message = message

    def encrypt(self):
        self.output("[Warning] Encryption function not created!")

    def decrypt(self):
        self.output("[Warning] Decryption function not created!")