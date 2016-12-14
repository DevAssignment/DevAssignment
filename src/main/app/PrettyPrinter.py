class PrettyPrinter:
    def __init__(self):
        #TODO: prints things pretty in the console
        pass

    def print_string(self, string):
        print(string)

    def print_multiple(self, lst):
        [print(s) for s in lst]

    def output(self, to_print):
        if type(to_print) is str:
            self.print_string(to_print)
        elif type(to_print) is list:
            self.print_multiple(to_print)

    def input(self, text=""):
        if text == "":
            return input()
        return input(text)
