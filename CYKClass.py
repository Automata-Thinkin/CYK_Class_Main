class CykNode:

    #Constructors
    def __init_(self, word):
        self.__init__()
        self.initialString = word
        self.createStructure()

    def __init__(self, word="", set=None, down=None, across=None):
        self.level = 0
        self.initialString = word
        self.set = set
        self.parent:CykNode = None
        self.down = down
        self.across = across

    # Getters
    def getInitialString(self):
        return self.initialString
    def getSet(self):
        return self.set
    def getParent(self):
        return self.parent
    def getDown(self):
        return self.down

    def getAcross(self):
        return self.across

    # Setters
    def setInitialString(self, word):
        self.initialString = word
    def setSet(self, set):
        self.set = set
    def setParent(self, parent):
        self.parent = parent
    def setDown(self, down):
        self.down = down

    def setAcross(self, across):
        self.across = across

    # Functionalities

    def setLevel(self, current):
        if (self.down() != None):
            self.level += 1
            current.setLevel(self, current)

    def toString(self):
        content = "Node: "
        content += "initialString: 0" if self.initialString == "" else self.initialString
        content += "\nParent: Taken" if self.parent is not None else "\nParent: "
        content += "\nDown: Taken" if self.down is not None else "\nDown: "
        content += "\nAcross: Taken" if self.across is not None else "\nAcross: "
        return content


class CykStructure:

    def __init__(self):
        self.root = None
        self.level = 0
        self.word = ""
    def __init__(self, word=""):
        self.root = None
        self.word = word
        self.level = 0
        if(word!=""):
            self.createStructure()


    def createStructure(self):
        if (self.root == None):
            self.root = CykNode(word=self.word[self.level]) #Take the first letter of the string and place here.
            #print('createStructure() - n: ', len(self.word)-1)
            self.addLevel((len(self.word) - 1), self.root)


    def addLevel(self,n, child: CykNode):
        if(n > 0):
            child.parent = CykNode("", None, child, None)
            self.level += 1
            self.addBranch(self.level-1, child.parent)
            n -= 1
            self.addLevel(n, child.parent)

    def addBranch(self, n, current:CykNode):
        current.across = CykNode()
        current.across.setParent(current)
        #--n
        if n == 0:
            current.across.setInitialString(self.word[self.level])
        elif n > 0:
            n -= 1
            self.addBranch(n, current.across)

    def toString(self):
        content = ("{}",self.root.toString)






