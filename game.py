# imports setting getter methods
import settings
from typingtest import Test

class Game():
    def __init__(self):

        # "empty" settings
        self.settings = {"method": -1, "count": -1}

        # prints the state of the thing
        self.state = "home"

    def run(self):
        while True:
            if self.state == "home":            # home menu page
                self.intro()
            elif self.state == "count":         # settings for word count
                self.countSettings()
            elif self.state == "mode":          # settings for mode
                self.modeSettings()
            elif self.state == "play":          # playing the test
                self.play()
    
    def intro(self):

        # prints introduction sequence
        settings.printIntro()

        # switches state
        self.state = "count"

    def countSettings(self):

        # gets count
        self.settings["count"] = settings.getLengthSettings()

        # switches state
        self.state = "mode"

    def modeSettings(self):

        # gets mode
        mode = settings.getModeSettings()

        # switches state
        self.state = "count" if mode == -1 else "play"

        # sets settings
        self.settings["method"] = mode

    def play(self):

        # runs the typingtest
        test = Test(self.settings["method"], self.settings["count"])
        test.run()

        # asks if the player wants to continue
        cont = input("Would you like to test again? (y/n): ") in ["y", "Y"]

        # switches mode if player wants to quit
        self.state = "mode" if not cont else self.state