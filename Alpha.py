from string import ascii_uppercase, ascii_lowercase
class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters
    def print(self):
        for i in self.letters:
            print(i, end=" ")
    def letters_num(self):
        print(len(self.letters))

al1 = Alphabet("eng", "ABCDE")
al1.print()
al1.letters_num()

class EngAlphabet(Alphabet):
    def __init__(self, lang, letters):
        super().__init__(lang, letters)
        self.cnt = len(letters)
    def is_en_alpha(self, lett):
        for i in self.letters:
            if i == lett:
                return True
        return False
    @staticmethod
    def text():
        return "Hello there"


al2 = EngAlphabet('eng', ascii_uppercase + ascii_lowercase)
print(al2.is_en_alpha('h'))
print(al2.cnt)
print(al2.text())
