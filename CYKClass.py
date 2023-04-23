class cykNode:
    def __init__(self):
        self.level = 0
        self.initialString = ""
        self.parent = None
        self.set = None
        self.down = None
        self.diagonal = None

    def __init_(self, word):
        self.__init__()
        self.initialString = word
        self.createStructure()

    def __init__(self, word, set, down, across):
        self.initialString = word
        self.set = set
        self.down = down
        self.across = across

    # Getters
    def getSet(self):
        return self.set

    def getDown(self):
        return self.down

    def getAcross(self):
        return self.across

    # Setters
    def setSet(self, set):
        self.set = set

    def setDown(self, down):
        self.down = down

    def setAcross(self, across):
        self.across = across

    # Functionalities

    def setLevel(self, current):
        if (self.down() != None):
            self.level += 1
            current.setLevel(self, current)

    def createStructure(self):
        if (len(self.initialString) != 0):
            self.parent = cykNode(self.initialString[1::], None, self, cykNode(self.initialString[1]))




