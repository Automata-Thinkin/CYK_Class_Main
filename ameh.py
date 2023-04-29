class CykAlgorithm:
    def __init__(self, fileName=""):
        self.grammar = {}
        self.grammar = self.readGrammar(fileName)

    def readGrammar(self, fileName):
        try:
            f = open(fileName, "r")
            for i in f.read().strip().split('\n'):
                self.grammar[i.split(':')[0]] = i.split(':')[1].strip().split('/')
            return self.grammar
        except:
            print("Could not open File")
            return {}
    def cykParseR(self,grammar, substring):
        s = set()
        if (len(substring) == 1):
            for i in grammar.keys():
                for j in grammar[i]:
                    if (j == substring[0]): s.add(i)

        else:
            for g in range(1, len(substring)):
                # print("---",substring[:i],substring[i:])
                l = self.cykParseR(grammar, substring[:g])
                r = self.cykParseR(grammar, substring[g:])

                if (len(substring) == 2):
                    for i in grammar.keys():
                        for j in grammar[i]:
                            if (j == list(l)[0] + list(r)[0]): s.add(i)
                else:
                    for i in range(len(l)):
                        for j in range(len(r)):
                            for y in grammar.keys():
                                for z in grammar[y]:
                                    if (z == list(l)[i] + list(r)[j]): s.add(y)
                                    # print(substring[:g],substring[g:],list(l)[i]+list(r)[j])
        # if(len(substring)==3):print(substring,s)
        return s

    def cykParse(self,grammar, substring):
        if (substring == "" and '' in grammar['S']): return True
        substring = [i for i in substring]
        out = self.cykParseR(grammar, substring)
        if ('S' in out): return True
        return False

    def userInput(self, fileName):
        self.grammar = self.readGrammar(fileName)
        Tstr = input("Input the string? ")
        print(Tstr, " -> ", self.cykParse(self.grammar, Tstr))

