from EncryptionFramework.BaseEncrypt import *

class CaesarCipherEncrypt(BaseEncrypt):
    def __init__(self, action, key, message):
        super().__init__(action, key, message)

    def encrypt(self):
        self.output("Encrypting message..")
        return self.changeShift(True)
    
    def decrypt(self):
        self.output("Decrypting message..")
        return self.changeShift(False)

    def changeShift(self, encrypting):
        messageShifted = ""

        try:
            self.key = int(self.key)
        except:
            self.output("[Error] Improper key: Provided key is not able to be determined into a shift, returning provided message")
            return self.message

        for character in self.message:
            if character.isalpha():
                characterShift = ord(character.lower()) - ord('a')

                if encrypting:
                    characterShifted = chr((characterShift + self.key) % 26 + ord('a'))
                else:
                    characterShifted = chr((characterShift - self.key) % 26 + ord('a'))

                messageShifted += characterShifted.upper() if character.isupper() else characterShifted
            else:
                messageShifted += character
            
        return messageShifted