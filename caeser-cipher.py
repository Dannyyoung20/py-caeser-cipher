# Creating the ceaser's cypher
# encryption algorithm

class CaeserCipher():

    allowed_alpha = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self):
        self.encryptedText = ""
        self.clearText = ""

    def encryption(self, clearmsg):
        # Loop through all the characters given in the message

        for char in clearmsg:
            # check if the character exists in the alphabets

            if char in self.allowed_alpha:
                newCharPos = (self.allowed_alpha.find(char) + 13) % 26
                self.encryptedText += self.allowed_alpha[newCharPos]
            else:
                self.encryptedText += char
        return self.encryptedText

    def decrypter(self, encrypted):
        for char in encrypted:
            if char in self.allowed_alpha:
                charPos = (self.allowed_alpha.find(char) - 13) % 26
                self.clearText += self.allowed_alpha[charPos]
            else:
                self.clearText += char
        return self.clearText

    def getUserText(self):
        msg = raw_input("Write Your text please: ")
        msg = msg.lower()

        # Check if user wants to encrpt or decrypt
        status = raw_input("Press E if you want to encrypt or D if you want to decrypt:")
        status = status.lower()
        if status == 'e':
            text = self.encryption(msg)
            print text
        elif status == 'd':
            self.decrypter(msg)
            text = self.encryption(msg)
            print text
        else:
            print('Invalid token given...')
            print """Exiting..."""
            return

test = CaeserCipher()
test.getUserText()
