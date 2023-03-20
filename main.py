from game import Game
from os import system, name as operatingSystem

def main():
    # create a game and play it
    game = Game()
    game.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        system('clear' if operatingSystem != "nt" else "cls")
        print("Thanks for playing!")