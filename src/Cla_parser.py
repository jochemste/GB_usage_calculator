import sys

class Cla_parser():
    printAll: bool
    valid_args: list

    def __init__(self, printAll: bool= False, valid_args: list= []):
        self.printAll= printAll
        self.valid_args= valid_args

    def __del__(self):
        pass

    def checkSyntaxCLA(self):
        syn_correct: bool = False
        if len(sys.argv) > 2:
            syn_correct= False
        else:
            for el in sys.argv:
                if str(el) in self.valid_args:
                    syn_correct= True
                else:
                    syn_correct= False
                    break
        return syn_correct

    def getArgc(self):
        return len(sys.argv)

    def argExists(self, arg):
        return arg in sys.argv

    def getArg(self, index):
        if index < len(sys.argv):
            return sys.argv[index]
        else:
            return -1

    def getArgIndex(self, arg):
        index=1
        while(arg != str(sys.argv[index])):
            index = index+1
            if index > 10:
                return -1
        return index

    def getParsedCLA(self):
        return sys.argv
