import CYKClass as cyk

# Unit Tests

''' List of Functions:
Global Parameter:

    Class: User
        +__init__(self)
        +__init__(self,word)
        +__init__(self,word,set,down,across)
        #Getters/setters not Necessary
        +view_level(): int
        +createStructure():void
        +acrossNNodes(self,n):void

'''


class CYKClass_Test():

    def empty_Initialization(self):
        node = cyk.cykNode()

    def empty_Initialization_Test(self):
        funct = self.empty_Initialization_Test.__name__
        try:
            print(funct)
            self.empty_Initialization()
            print(funct + "... success")
        except:
            print(funct + "... failed")

    # Upon Initialization, class will run these test functions
    def __init__(self):
        print("----------------------------------")
        self.empty_Initialization_Test()
        print("----------------------------------")

        print("End CYKClass Test Class\n")



