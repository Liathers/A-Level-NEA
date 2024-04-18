from EncryptionFramework.BaseEncrypt import *

#This class is what will be used for the Caesar Cipher Encryption Algorithm
class CaesarCipherEncrypt(BaseEncrypt):
    def __init__(self, action, key, message):
#Initialise the class using the functions that are provided from the BaseEncrypt module
        super().__init__(action, key, message)

#This will be called in order to encrypt a message, this will then call the changeShift function accordingly
    def encrypt(self):
        self.output("Encrypting message..")
        return self.changeShift(True)

#This will be called in order to decrypt a message, this will then call the changeShift function accordingly
    def decrypt(self):
        self.output("Decrypting message..")
        return self.changeShift(False)

#This is the main function that is used to encrypt a message, this will be done by shifting the alphanumeric
#characters of the string in the correct order based on arguments provided to the user
    def changeShift(self, encrypting):
#Define the variable ready to shift the characters provided
        messageShifted = ""

#Attempt to convert the provided key to an integer to be used for the shift, if an incorrect argument is
#provided, then output the warning, and return the original message
        try:
            self.key = int(self.key)
        except:
            self.output("[Error] Improper key: Provided key is not able to be determined into a shift, returning provided message")
            return self.message

#Cycle through each character within the string, and do actions based on whether it is alphanumeric or not
        for character in self.message:
            if character.isalpha():
#Get the shift of the character, by taking the unicode value and taking away the unicode value of "a"
                characterShift = ord(character.lower()) - ord('a')

#If encrypting is true, ensure that the shift changes the message positively
                if encrypting:
#Add the defined shift from self.key to characterShifted, ensuring that it stays within the alphanumeric values,
#then add the value of "a" to it
                    characterShifted = chr((characterShift + self.key) % 26 + ord('a'))
#If not encrypting, ensure that the shift changes the message negatively
                else:
#Remove the defined shift from self.key to characterShifted, ensuring that it stays within the alphanumeric values,
#then add the value of "a" to it
                    characterShifted = chr((characterShift - self.key) % 26 + ord('a'))

#If the original character is in uppercase, then ensure that the shifted character is also uppercase,
#if not, then just add the lowercase character
                messageShifted += characterShifted.upper() if character.isupper() else characterShifted
            else:
#If the character is not alphanumeric, then just add the current value to it
                messageShifted += character
            
#Return the shifted message to the user
        return messageShifted