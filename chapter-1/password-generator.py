# imports and variables
from abc import ABC,abstractmethod
import string
import random

# create password generator abstract class
class PasswordGeneratorAbstract(ABC):
    @abstractmethod
    def generate_password(self,length=8):
        pass


# generic numeric password generator
class NumericPasswordGenerator(PasswordGeneratorAbstract):
    letters=string.digits
    
    def generate_password(self, length=8):
        result=""
        for _ in range(length):
            result+= str(random.choice(self.letters))
        return result
    
    def generate_password1(self, length=8):
        return "".join(str(random.choice(self.letters)) for _ in range(length))

# create letters password generator

class LetterPasswordGenerator(PasswordGeneratorAbstract):
    def generate_password(self, length=8):
        letters=string.ascii_letters
        return "".join(str(random.choice(letters)) for _ in range(length))

# generic mixed password generator

class MixPasswordGenerator(PasswordGeneratorAbstract):
    def generate_password(self, length=8):
        letters=string.ascii_letters+string.digits
        return "".join(str(random.choice(letters)) for _ in range(length))

# run the application 
numericGenerator=NumericPasswordGenerator()
print(numericGenerator.generate_password1())


letterGenerator=LetterPasswordGenerator()
print(letterGenerator.generate_password())



mixGenerator=MixPasswordGenerator()
print(mixGenerator.generate_password())
