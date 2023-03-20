# function for word getting data
import getdata
from readchar import readkey, key
from colorama import Style
from colorama import Fore 
from os import system

class Test:
    def __init__(self, method, count):

        # gets words based on what the prompt is (if its not essay, then its either "easy" or "hard")
        self.prompt = getdata.getRandomEssays(count) if method == "essay" else getdata.getWords(count, method)

        # defines empty answer
        self.answer = ""

        # detects game over
        self.over = False

        # prints game
        system('clear')
        print(self)

    def __str__(self):
        # string output
        output = ""

        # list of letter pairs
        merged = list(zip(self.prompt, self.answer))

        # gets length of merge
        mergeLength = len(merged)

        # prints colors
        for letter, input in merged:
            if letter != input:
                output += f"{Fore.RED}{letter}"
            else:
                output += f"{Fore.GREEN}{letter}"

        # prints remaining
        for index in range(mergeLength, len(self.prompt)):
            output += f"{Style.RESET_ALL}{self.prompt[index]}"

        # detects game ending
        self.over = mergeLength >= len(self.prompt)

        # return colored prompt
        return output

    def run(self):
        while not self.over:
            # gets input
            self.getInput()

            # prints game
            system('clear')
            print(self)

    def getInput(self):
        # gets the key
        inp = readkey()
        
        # checks for backspace to remove letter - otherwise add letter
        if inp == key.BACKSPACE:
            self.answer = self.answer[0:len(self.answer)-1]
        else:
            self.answer += inp