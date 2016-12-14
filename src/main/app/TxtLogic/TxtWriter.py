class TxtWriter:

    def __init__(self, txtFile):
        self.txtFile = txtFile

    def writeTxt(self):
        txt = open(self.txtFile, "w")
        txt.write("test")
        txt.close()


txtWriter = TxtWriter("test.txt")
txtWriter.writeTxt()


