from BaseClass import *

from EncryptionFramework.CaesarCipherEncrypt import *

class EncryptionHandler(BaseClass):
    def __init__(self):
        super().__init__()

    def encrypt(self, algorithm, key, message):
        self.output("Performing an encryption")
        if algorithm == 0:
            CaesarCipherEncrypt(key, message).encrypt()