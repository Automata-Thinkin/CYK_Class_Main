import ameh as cyk
import UnitTest_CykClass as cykTest
def HelloWorld():
    print("Hello CYK!")
def main():
    #Just to ensure Interpreter Works
    #HelloWorld()

    #init will run and start test class
    #testClass = cykTest.CykClassTest()

    #If you want to test your own file and String: Uncomment the line below!
    cyk.CykAlgorithm().userInput("grammer.txt")

    print("Main Terminated")

main()
