class TxtReader:
    def __init__(self, txtFile):
        self.txtFile = txtFile

    def readTxt(self):
        txt = open(self.txtFile, "r")
        print (txt.read())
        txt.close()

txtReader = TxtReader("test.txt")
txtReader.readTxt()