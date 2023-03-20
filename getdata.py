import random as rand

def getRandomEssays(wordCount):
    # opens the file
    with open("essays/ai-essays.txt", "r") as f:

        # gets all the lines
        lines = f.readlines()

        # gets a randomline
        line = lines[rand.randint(0, len(lines)-1)]

    # returns a random line with a specified word count
    return " ".join(line.split(" ")[0:wordCount])

def getWords(wordCount, difficulty):

    # defines filename based on difficulty
    filename = "1-1000" if difficulty == "easy" else "engmix"

    # defines output
    output = ""

    # opens the file
    with open(f"words/{filename}.txt", "r") as f:

        # gets all the lines
        lines = f.readlines()

        # gets random lines
        for _ in range(wordCount):
            output += rand.randint(0, len(lines)-1)
    
    # return
    return output