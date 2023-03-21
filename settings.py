# imports libaries
from os import system, name as operatingSystem
from colorama import Fore

def printIntro():
    # clears system
    system('clear' if operatingSystem != "nt" else "cls")
    
    # defines title
    title = "Welcome to Typing Test!"
    colors = ["RED", "YELLOW", "GREEN", "BLUE", "MAGENTA"]

    # prints title in rainbow
    for i in range(len(title)):
        print(f"{eval("Fore." + colors[i % len(colors)])}{title[i]}", end="")   # a letter with the color corresponding to the index mod 5
    
    # resets and new line
    print(Fore.RESET)

    # defines reset of the prompt    
    prompt = ["",
              "In this game, you will be given a prompt, which you will need to type out (accurately).",
              "While taking a test, you can press Tab to regenerate your test and Enter to quit.", 
              "Then, after you finish, you will be given your typing speed! There are various tests to choose from.",
              "",
              "If you want to stop running the program, press Crtl+C to quit. Enjoy!",
              ""]
    
    # prints every line
    for line in prompt:
        print(line)

    # waits for enter press to begin
    input("Press enter when you are ready to begin. ")

def getLengthSettings():
    # clears system
    system('clear' if operatingSystem != "nt" else "cls")

    # defines choice
    option = -1

    # prints prompt
    print("How many words would you like to type?")

    # gets option in range
    while not (0 < option and option < 200):
        option = input("Enter a number between 1 and 200: ")
        try:
            option = int(option)
        except:
            print("Please enter an integer!")
            option = -1                             # resets in order to avoid error in while loop
            continue

    
    # returns chosen number
    return option

def getModeSettings():
    # clears system
    system('clear' if operatingSystem != "nt" else "cls")

    # defines choice
    option = ""

    # prints prompt
    prompt = ["What mode would you like to test on?",
              "",
              "  1. Sentences",
              "  2. Easy Words", 
              "  3. Hard Words",
              ""]
    for line in prompt:
        print(line)
    
    # gets the option
    while option not in ["1", "2", "3", "b"]:
        option = input("Enter \"b\" to go back, or a number to choose a mode: ")

    # returns the mode if possible, otherwise returns the exit code
    try:
        return ["essay", "easy", "hard"][int(option)-1]
    except:
        return -1
    
