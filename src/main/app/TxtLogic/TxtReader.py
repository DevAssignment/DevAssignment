import random

class TxtReader:
    def __init__(self, txtFile):
        self.txtFile = txtFile

    def readTxt(self):
        txt = open(self.txtFile, "r")
        print (randomLine(self.txtFile))
        txt.close()

def randomLine(txtFile):
    line = random.choice(open(txtFile).readlines())
    return line
