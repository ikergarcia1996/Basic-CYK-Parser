This is a basic CYK Parser implemented in Python. This parser has been implemented for the "Computational Linguistics: Morphology and Syntax" course of the Language Analysis and Processing Master (http://ixa.si.ehu.es/master/?lang=en).

# Files in the repository

1. CYK_Parser.ipyn: Parser in jupyter notebook format
2. CYK_Parser.ipyn: Parser in .py format
3. example.py: Some examples of use (usage: python3 example.py)
4. example_output.txt: output of the example.py script in txt format
5. example_grammar*.txt: Some example grammars


# Author
```
Iker García Ferrero - ikergarcia1996
```
# Example Of Use
 
```
# Initialize the grammar and read the rules from a file
g = Grammar('example_grammar1.txt')

# Parse a sentence
g.parse('astronomers saw stars with ears')

# Print the table used for parsing the sentence
g.print_parse_table()

# Get the list of trees generated for the sentence
trees = g.get_trees()

# Get the result of the production rule, VP, S, NP... 
p = trees[0].get_type

# Get the left child of the production rule
l = trees[0].get_left

# Get the right child of the production rule
d = trees[0].get_right
```

 ## Expected output

 
```
Grammar file readed succesfully. Rules readed:
S --> NP VP
PP --> P NP
VP --> V NP
VP --> VP PP
NP --> NP PP
NP --> astronomers
NP --> ears
NP --> saw
V --> saw
NP --> telescope
NP --> stars
P --> with

Applied Rule: VP[2,2] --> V[1,2] NP[1,3]
Applied Rule: PP[2,4] --> P[1,4] NP[1,5]
Applied Rule: S[3,1] --> NP[1,1] VP[2,2]
Applied Rule: NP[3,3] --> NP[1,3] PP[2,4]
Applied Rule: VP[4,2] --> V[1,2] NP[3,3]
Applied Rule: VP[4,2] --> VP[2,2] PP[2,4]
Applied Rule: S[5,1] --> NP[1,1] VP[4,2]
Applied Rule: S[5,1] --> NP[1,1] VP[4,2]
----------------------------------------
The sentence IS accepted in the language
Number of possible trees: 2
----------------------------------------

-----------  ------------  ------  ------  ------
['S', 'S']
[]           ['VP', 'VP']
['S']        []            ['NP']
[]           ['VP']        []      ['PP']
['NP']       ['NP', 'V']   ['NP']  ['P']   ['NP']
astronomers  saw           stars   with    ears
-----------  ------------  ------  ------  ------
```

# Example of grammar file
The program assumes that the grammar is a valid context-free grammar in CNF form (https://www.tutorialspoint.com/automata_theory/chomsky_normal_form.htm). Rules must be separated by lines. 
```
S -> NP VP
PP -> P NP
VP -> V NP
VP -> VP PP
NP-> NP PP
NP -> astronomers
NP -> ears
NP -> saw
NP-> telescope
NP -> stars
P -> with
V -> saw
```




