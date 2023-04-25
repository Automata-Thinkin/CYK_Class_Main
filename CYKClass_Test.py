import CYKClass as cyk

# Unit Tests

''' List of Functions:
Global Parameter:

    Class: User
        +__init__(self)
        +__init__(self,word,set,down,across)
        #Getters/setters not Necessary
        +view_level(): int
        +createStructure():void
        +acrossNNodes(self,n):void
        
        
    
        

'''


class CYKClass_Test():

    def empty_Initialization(self):
        node = cyk.CykNode()

    def empty_Initialization_Test(self):
        funct = self.empty_Initialization_Test.__name__
        try:
            print(funct)
            self.empty_Initialization()
            print(funct + "... success")
        except:
            print(funct + "... failed")

    def param_Initialization(self):
        downNode = cyk.CykNode()
        acrossNode = cyk.CykNode()
        node = cyk.CykNode("abba", {'S','X','Z'}, downNode, acrossNode)

    def param_Initialization_Test(self):
        funct = self.param_Initialization_Test.__name__
        try:
            print(funct)
            self.param_Initialization()
            print(funct + "... success")
        except:
            print(funct + "... failed")

    def node_toString(self):
        node = cyk.CykNode()
        print(node.toString())

    def node_toString_Test(self):
        funct = self.node_toString_Test.__name__
        #self.node_toString()
        try:
            print(funct)
            self.node_toString()
            print(funct + "... success")
        except:
            print(funct + "... failed")
    '''
    Class: CykStructure
    +__init__(self)
    +__init__(self, word)
    +addBranch()
    +createStructure()
    '''

    def cykStruct_empty_Initialization(self):
        structure = cyk.CykStructure()

    def cykStruct_empty_Initialization_Test(self):
        funct = self.cykStruct_empty_Initialization_Test.__name__
        self.cykStruct_empty_Initialization()
        try:
            print(funct)
            self.cykStruct_empty_Initialization()
            print(funct + "... success")
        except:
            print(funct + "... failed")

    def cykStruct_param_Initialization(self):
        structure = cyk.CykStructure("abba")

    def cykStruct_param_Initialization_Test(self):
        funct = self.cykStruct_param_Initialization_Test.__name__
        self.cykStruct_param_Initialization()
        try:
            print(funct)
            self.cykStruct_param_Initialization()
            print(funct + "... success")
        except:
            print(funct + "... failed")

    def cykStruct_param_Display(self):
        struct = cyk.CykStructure("abba")
        root:cyk.CykNode = struct.root
        print('\nZ11:\n' + root.toString())
        print('\nZ12:\n' + root.parent.toString())
        print('\nZ13:\n' + root.parent.parent.toString())
        print('\nZ14:\n', root.parent.parent.parent.toString())
        print('Branches....\n')
        print('\nZ22:\n' + root.parent.across.toString())

        print('\n\nZ23:\n' + root.parent.parent.getAcross().toString())
        print('\nZ33:\n' + root.parent.parent.getAcross().getAcross().toString())

        print('\n\nZ24:\n' + root.parent.parent.parent.getAcross().toString())
        print('\nZ34:\n' + root.parent.parent.parent.getAcross().getAcross().toString())
        print('\nZ44:\n' + root.parent.parent.parent.getAcross().getAcross().getAcross().toString())

    def cykStruct_param_Display_Test(self):
        funct = self.cykStruct_param_Display_Test.__name__
        try:
            print(funct)
            self.cykStruct_param_Display()
            print(funct + "... success")
        except:
            print(funct + "... failed")



    # Upon Initialization, class will run these test functions
    def __init__(self):
        print("----------------------------------")
        self.empty_Initialization_Test()
        print("----------------------------------")
        self.param_Initialization_Test()
        print("----------------------------------")
        self.node_toString_Test()
        print("----------------------------------")
        self.cykStruct_empty_Initialization_Test()
        print("----------------------------------")
        self.cykStruct_param_Initialization_Test()
        print("----------------------------------")
        self.cykStruct_param_Display_Test()
        print("----------------------------------")

        print("End CYKClass Test Class\n")



