from random import *

SpecialCharactersList = ["#", "@", "!", "£", "$", "%", "&", "*",]

LettersList = ["q", "w", "q","q","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l",
           "z","x","c","v","b","n","m"]

NumbersList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

PasswordLength = int(input("Please enter the length of the password(must be at least 6)\n"))


while True:
    if(PasswordLength <= 5):
        PasswordLength=int(input('Password Length MUST be at least 6, please try again\n'))
    else:
        LettersNo = int(input("Please enter the number of letters you want in your password\n"))
        SpecialCharactersNo = int(input("Please enter the number of special characters you want in your password\n"))
        break

NumbersNo = PasswordLength - LettersNo - SpecialCharactersNo
Letters = []
SpecialCharacters = []
Numbers = []
Password = []
Counter = 1

while Counter <= LettersNo:
    Letters.append(LettersList[randrange(0,len(LettersList))])
    Counter += 1

print(Letters)
Counter = 1

for l in Letters:
    Chance = randrange(0,1)
    if Chance == 0:
        pass
    else:
        pass
while Counter <= SpecialCharactersNo:
    SpecialCharacters.append(SpecialCharactersList[randrange(0,len(SpecialCharactersList))])
    Counter += 1

print(SpecialCharacters,"\n")
Counter = 1

while Counter <= NumbersNo:
    Numbers.append(NumbersList[randrange(0,len(NumbersList))])
    Counter += 1

Counter = 1
print(Numbers,"\n")
Password = Letters + SpecialCharacters + Numbers
print(Password)
shuffle(Password)
print(Password)
