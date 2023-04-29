CykParser

How to Run:

Run the interpreter on the Main File called: Ahmed.py

Amed.py - By initialization, Outputs into console the results of tests from grammars made from
a text file. The Grammar producded by reading the file is put in a
dictionary datatype, using a set of key/valued pairs to check if the cardesian product
like the two nonterminals "AB" is a value in one of the keys from the dictionary called grammar.

grammar.txt -

List of Functions:
+cykParse(grammar,substring)
+cykParseR(grammar,substring)

Using Python for this assignment was an exceptional language to use for it's array-based string manipulation.
Other languages, like Javascript, does not allow strings to be mutable as contents in a string are immutable, but lists and sets are mutable themselves.
Python gives us the flexibility to easily iterate through elements of an array by iteratively calling the elements by its keys.

cykParse(grammar,substring) - This function is the initial function that's called after being given a CFG, represented as a dictionary datatype. We call it grammar in the code.
It deals with the first case, dealing with empty strings. If the start Symbol contains an epsilon, or empty string, and the given string is empty, we return true as it is the
simplist case to deal with. After that it will move on to the next function to deal with the cases of one or many string lengths in cykParseR(grammar,substring)

cykParseR(grammar,substring) - Recursive function with a Base Case, and a recursive Part. For the base case, we want to add Symbols that contain terminals to the set.
This will occur last as we start the parsing in a top-down fashion.
