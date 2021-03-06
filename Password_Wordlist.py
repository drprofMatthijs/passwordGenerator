import pandas as pd
from random import randrange
import itertools
import os


class passwordgenerator:

    def __init__(self, list, complexity, numbers, uppercase):
        self.list = list
        self.complexity = complexity # Complexity levels: 1 -> Only add numbers | 2 -> Numbers + one special character | 3 -> Numbers + few special characters | 4 -> Numbers + All special characters
        self.subs = {
            'a' : ['4', '@'],
            'e' : ['3'],
            'g' : ['6'],
            'i' : ['!', '1'],
            'o' : ['0'],
            's' : ['5', '$'],
            't' : ['7']

        }
        self.numberlist = self.numberList(numbers)
        self.uppercase = uppercase
        self.main()

    def numberList(self, repeat):
        numberlist = itertools.product([0,1,2,3,4,5,6,7,8,9], repeat=repeat)
        result = []
        if repeat == 1:
            result = [str(tup[0]) for tup in numberlist]
        if repeat == 2:
            result = [str(tup[0]) + str(tup[1]) for tup in numberlist]
        if repeat == 3:
            result = [str(tup[0]) + str(tup[1]) + str(tup[2]) for tup in numberlist]
        if repeat == 4:
            result = [str(tup[0]) + str(tup[1]) + str(tup[2]) + str(tup[3]) for tup in numberlist]

        return result

    def onlyFirstSpecChar(self,word):
        # replaces only the first encountered letter with its special character(s)
        result = []
        for index,letter in enumerate(word):
            if letter.lower() in self.subs.keys():
                for entries in self.subs[letter.lower()]:
                    temp = list(word)
                    temp[index] = entries
                    new = "".join(temp)
                    result = result + [new]
                break

        return list(dict.fromkeys(result))

    def onlyLastSpecChar(self,word):
        # replaces only the last encountered letter with its special character(s)
        result = []
        for index,letter in enumerate(reversed(word)):
            if letter.lower() in self.subs.keys():
                for entries in self.subs[letter.lower()]:
                    temp = list(word)
                    temp[len(temp) - index - 1] = entries
                    new = "".join(temp)
                    result = result + [new]
                break

        return list(dict.fromkeys(result))
    
    def allSpecialCharacterSub(self, word):
        # replaces all letters with its special character(s)
        result = []
        for index,letter in enumerate(word):
            if letter.lower() in self.subs.keys():
                for entries in self.subs[letter.lower()]:
                    temp = list(word)
                    temp[index] = entries
                    new = "".join(temp)
                    result = result + [new] + self.allSpecialCharacterSub(new)


        return list(dict.fromkeys(result))

    def addNumbers(self, word):
        # add all numbers at the end of a word
        result = []
        for number in self.numberlist:
            result.append(word + number)

        return result 

    def capitalStart(self, word):
        if word[0].isupper() or not word[0].isalpha():
            return []
        else:
            return [word.capitalize()]

    def main(self):
        # main function of class
        complexity = self.complexity
        total = []
        capital = self.uppercase

        if capital:
            if complexity == 1:
                # only numbers
                for word in self.list:
                    temp = [word]
                    temp += self.capitalStart(word)

                    for option in temp:
                        total.append(option)
                        numbers = self.addNumbers(option)     # add a progress tracker here!!!
                        for num in numbers:
                            total.append(num)

            if complexity == 2:
                # numbers and last special character substitution
                for word in self.list:
                    wordtemp = [word]
                    wordtemp += self.capitalStart(word)
                    for option in wordtemp:
                        temp2 = [option]
                        temp2 += self.onlyLastSpecChar(option)
                        for passwds in temp2:
                            total.append(passwds)
                            numbers = self.addNumbers(passwds)
                            for num in numbers:
                                total.append(num)


            if complexity == 3:
                # numbers and first AND last special character substitution
                for word in self.list:
                    wordtemp = [word]
                    wordtemp += self.capitalStart(word)

                    for option in wordtemp:
                        temp2 = [option]
                        temp2 += self.onlyLastSpecChar(option)
                        temp2 += self.onlyFirstSpecChar(option)
                        temp2 = list(dict.fromkeys(temp2))       #remove duplicates occuring from using both onlyLastSpecChar and onlyFirstSpecChar

                        for passwds in temp2:
                            total.append(passwds)
                            numbers = self.addNumbers(passwds)
                            for num in numbers:
                                total.append(num)
            
            if complexity > 3:
                # numbers and ALL special character substitution
                for word in self.list:
                    wordtemp = [word]
                    wordtemp += self.capitalStart(word)

                    for option in wordtemp:
                        temp2 = [option]
                        temp2 += self.allSpecialCharacterSub(option)
                        for passwds in temp2:
                            total.append(passwds)
                            numbers = self.addNumbers(passwds)
                            for num in numbers:
                                total.append(num)

        else:
            if complexity == 1:
                # only numbers
                for word in self.list:
                    total.append(word)
                    numbers = self.addNumbers(word)     # add a progress tracker here!!!
                    for num in numbers:
                        total.append(num)

            if complexity == 2:
                # numbers and last special character substitution
                for word in self.list:
                    wordtemp = [word]
                    wordtemp += self.onlyLastSpecChar(word)
                    for passwds in wordtemp:
                        total.append(passwds)
                        numbers = self.addNumbers(passwds)
                        for num in numbers:
                            total.append(num)


            if complexity == 3:
                # numbers and first AND last special character substitution
                for word in self.list:
                    wordtemp = [word]
                    wordtemp += self.onlyLastSpecChar(word)
                    wordtemp += self.onlyFirstSpecChar(word)
                    wordtemp = list(dict.fromkeys(wordtemp))       #remove duplicates occuring from using both onlyLastSpecChar and onlyFirstSpecChar

                    for passwds in wordtemp:
                        total.append(passwds)
                        numbers = self.addNumbers(passwds)
                        for num in numbers:
                            total.append(num)
            
            if complexity > 3:
                # numbers and ALL special character substitution
                for word in self.list:
                    wordtemp = [word]
                    wordtemp += self.allSpecialCharacterSub(word)
                    for passwds in wordtemp:
                        total.append(passwds)
                        numbers = self.addNumbers(passwds)
                        for num in numbers:
                            total.append(num)

        self.result = total


def main():
    #
    # Main function. Processes input and creates class instance.
    #
    print()
    print("*** Bruteforce Password Generator by DrHerreman ***")
    print()

    while True: 
        wordListFile = input("Give the wordlist file: ")
        try: 
            with open(wordListFile) as wordlist:
                words = wordlist.read().splitlines()
            
        except FileNotFoundError:
            print("ERROR: No such file found. Try again.")
        
        else:
            break

    print()
    print("--------------------------------------------------------")
    print()
    
    while True:
        complexity = input("Define the complexity of the generator on a scale of 1-4." + "\n" + 
        "1 : Only add numbers \n2 : Numbers + one special character substitution \n3 : Numbers + few special character substitutions \n4 : Numbers + All special characters" 
         + "\n\n" + "Complexity: ")
        try:
            int(complexity)
        except ValueError:
            print()
            print("ERROR: The complexity has to be a number! Try again")
            print()
        else:
            if int(complexity) > 4:
                print()
                print("ERROR: The complexity has to be a number on a scale of 1-4. Try again")
                print()
            else:
                break

    while True:
        numbers = input("Define how many numbers should be added at the end of every password, on a scale of 1-4." + "\n" 
        + "\n" + "Numbers: ")
        try:
            int(numbers)
        except ValueError:
            print()
            print("ERROR: The input has to be a number! Try again")
            print()
        else:
            if int(numbers) > 4:
                print()
                print("ERROR: The input has to be a number on a scale of 1-4. Try again")
                print()
            else:
                break

    while True:
        capital = input("Lastly, do you want to add capital letters to the beginning of every password?" + "\n" 
        + "\n" + "y/n: ")

        if capital == 'y':
            capital = True
            break
        elif capital == 'n':
            capital = False
            break
        else:
            print("ERROR: Input has to be 'y' for yes or 'n' for no")
            print()

       

    generator = passwordgenerator(words, int(complexity), int(numbers), capital)
    passwords = generator.result
    passwordslen = str(len(passwords))
    print()
    print("Done! " + passwordslen + " password were generated.")
    print()

    filename = wordListFile.split('.txt')[0] + '_' + passwordslen + 'generatedPasswds.txt'

    with open(filename, 'w') as f:
        pswdList = map(lambda x:x+'\n', passwords)
        f.writelines(pswdList)
    
    print("The following file has been created:", filename)


main()
