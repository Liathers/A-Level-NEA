from EncryptionFramework.BaseEncrypt import *

class CaesarCipherEncrypt(BaseEncrypt):
    def __init__(self, key, message):
        super().__init__(key, message)