# imports libaries
from os import system
from colorama import Fore, Style

def printIntro():
    # clears system
    system('clear')
    
    # defines title
    title = "Welcome to Typing Test!"
    colors = ["RED", "YELLOW", "GREEN", "BLUE", "MAGENTA", "LIGHTMAGENTA_EX"]
    fore = "Fore."

    # prints title in rainbow
    for i in range(len(title)):
        print(f"{eval(fore + colors[i%6])}{title[i]}", end="")
    
    # resets and new line
    print(Fore.RESET)

    # defines reset of the prompt    
    prompt = ["",
              "In this game, you will be given a prompt, which you will need to type out (accurately).",
              "While taking a test, you can press Tab to regenerate your test and Enter to quit.", 
              "Then, after you finish, you will be given your typing speed! There are various tests to choose from.",
              "",
              "Press enter when you are ready to begin."]
    
    # prints every line
    for line in prompt:
        print(line)

    # waits for enter press to begin
    input()

def getLengthSettings():
    # clears system
    system('clear')

    # defines choice
    option = -1

    # gets option in range
    while 0 < option and option < 200:
        try:
            option = int(input("Enter a word count between 1 and 200: "))
        except:
            print("Please enter an integer!")
            continue

    
    # returns chosen number
    return option
