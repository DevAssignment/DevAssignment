class TxtWriter:

    def __init__(self, txtFile):
        self.txtFile = txtFile

    def writeTxt(self, txtToWrite):
        txt = open(self.txtFile, "w")
        txt.write(txtToWrite)
        txt.close()




