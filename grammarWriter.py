class CykReader:
    def __init__(self, fileName=""):
        self.fileName = fileName
        print(fileName)
        print(self.fileName)
        self.grammar = self.read(self.fileName)

    def read(self, file):
        grammar = open(file, 'r')
        stmt = grammar.readlines()
        self.grammar : dict
        for line in stmt:
            line = line.replace(" ", "")
            sep = line.find(">")
            key = line[:sep-1]
            values = line[sep+1:]
            values.replace("ε"," ")
            split = values.split("|")
            print(type(split))
            self.grammar[key] = split
        return self.grammar


