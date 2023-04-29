import ameh as cyk

'''
List of Functions:

Class: CykAlgorithm
    +__init__(fileName)
    +cykParseR(grammar,substring)
    +cykParse(grammar,substring)
    +userInput(grammar)
'''

class CykClassTest():
    def empty_Initialization(self):
        node = cyk.CykAlgorithm()

    def empty_Initialization_Test(self):
        funct = self.empty_Initialization_Test.__name__
        self.empty_Initialization()
        try:
            print(funct)

            print(funct + "... success")
        except:
            print(funct + "... failed")
    def param_Initialization(self):
        node = cyk.CykAlgorithm('grammer.txt')

    def param_Initialization_Test(self):
        funct = self.param_Initialization_Test.__name__
        try:
            print(funct)
            self.param_Initialization()
            print(funct + "... success")
        except:
            print(funct + "... failed")

    def __init__(self):
        print("----------------------------------")
        self.empty_Initialization_Test()
        print("----------------------------------")
        self.param_Initialization_Test()
        print("----------------------------------")
        #self.param_Initialization_Test()
        print("----------------------------------")
        #self.param_Initialization_Test()
        print("----------------------------------")
        #self.param_Initialization_Test()
        print("----------------------------------")
        #self.param_Initialization_Test()
        print("----------------------------------")
        #self.param_Initialization_Test()
        print("----------------------------------")

        print("End CYKClass Test Class\n")