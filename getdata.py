import random as rnd

def getRandomEssays(wordCount):
    # opens the file
    with open("essays/ai-essays.txt", "r") as f:

        # gets all the lines
        lines = f.readlines()

        # gets a randomline
        line = lines[rnd.randint(0, len(lines)-1)]

    # returns a random line with a specified word count
    return " ".join(line.split(" ")[0:wordCount])
