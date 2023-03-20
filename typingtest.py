# function for word getting data
import getdata
from readchar import readkey, key
from colorama import Style
from colorama import Fore 
from os import system
from time import time as timer

class Test():
    def __init__(self, method, count):
        # stores settings
        self.settings = {"method": method, "count": count}

        # gets words based on what the prompt is (if its not essay, then its either "easy" or "hard")
        self.prompt = getdata.getRandomEssays(count) if method == "essay" else getdata.getWords(count, method)

        # defines empty answer
        self.answer = ""

        # detects game over
        self.over = False

        # initializes timer
        self.time = -1

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
            output += f"{Fore.RESET}{self.prompt[index]}"

        # detects game ending
        self.over = mergeLength >= len(self.prompt)

        # return colored prompt
        return output

    def run(self):
        # goes until the prompt is done
        while not self.over:

            # gets input
            self.getInput()

            # starts the timer after first input and only first input
            if len(self.answer) <= 1:
                start = timer()
            
            # checks for breaking - if enter was called
            if self.over: 
                return

            # prints game
            system('clear')
            print(self)

        # time at end
        end = timer()
        self.time = round(end-start, 2)        # time in seconds

        # prints the result
        print(self.result())

    def getInput(self):
        # gets the key
        inp = readkey()
        
        # checks for backspace to remove letter - otherwise add letter
        if inp == key.BACKSPACE or inp == key.DELETE:
            self.answer = self.answer[0:len(self.answer)-1]                 # shortens answer by one char
        elif inp == key.TAB:
            self.__init__(self.settings["method"], self.settings["count"])  # restarts game with same settings
        elif inp == key.ENTER:
            self.over = True                                                # ends game
        else:
            self.answer += inp                                              # adds character

    def result(self):

        # merges the answer and the prompt
        merged = list(zip(self.prompt, self.answer))

        # gets total length of the test (in characters) minus spaces count
        length = len(merged) # - self.prompt[0:len(merged)].count(" ")

        # assuming average word length is 5, get word count approximated
        length /= 5

        # get wpm based on time
        wpm = (length / self.time) * 60 if self.time > 0 else 999    # avoids divide by zero errors

        # get accuracy
        correct, total = 0, 0
        for letter, answer in merged:
            if letter == answer:
                correct += 1
            total += 1
        accuracy = correct / total 

        # multiply wpm by the accuracy to get overall wpm
        wpm *= accuracy

        return f"{Fore.RESET}You typed at {Fore.BLUE}{round(wpm, 2)}{Fore.RESET} words per minute, with an accuracy of {Fore.BLUE}{round(accuracy * 100, 2)}%{Fore.RESET}"