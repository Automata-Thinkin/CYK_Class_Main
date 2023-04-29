# Function to perform the CYK Algorithm
def cykParseR(grammar,substring):
    s= set()
    if(len(substring)==1):
        for i in grammar.keys():
            for j in grammar[i]:
                if(j == substring[0]): s.add(i)

    else:
        for g in range(1,len(substring)):
            #print("---",substring[:i],substring[i:])
            l= cykParseR(grammar,substring[:g])
            r= cykParseR(grammar,substring[g:])

            if(len(substring)==2):
                for i in grammar.keys():
                    for j in grammar[i]:
                        if(j == list(l)[0]+list(r)[0]): s.add(i)
            else:
                for i in range(len(l)):
                    for j in range(len(r)):
                        for y in grammar.keys():
                            for z in grammar[y]:
                                if(z == list(l)[i]+list(r)[j]):s.add(y)
                                #print(substring[:g],substring[g:],list(l)[i]+list(r)[j])
    #if(len(substring)==3):print(substring,s)
    return s

def cykParse(grammar,substring):
    if(substring == "" and '' in grammar['S']):return True
    substring = [i for i in substring]
    out= cykParseR(grammar,substring)
    if('S' in out):return True
    return False

print("--Grammer--")
grammar={}
f = open("grammer.txt", "r")
for i in f.read().strip().split('\n'):
   grammar[i.split(':')[0]] = i.split(':')[1].strip().split('/')
print(grammar)

# Given string
Tstr= input("Input the string? ")
print(Tstr," -> ",cykParse(grammar,Tstr))