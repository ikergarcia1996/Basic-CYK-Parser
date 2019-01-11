This is a basic CYK Parser implemented in Python. This parser has been implemented for the "Computational Linguistics: Morphology and Syntax" course of the Language Analysis and Processing Master (http://ixa.si.ehu.es/master/?lang=en).

# Files in the repository

1. CYK_Parser.ipyn: Parser in jupyter notebook format
2. CYK_Parser.ipyn: Parser in .py format
3. example.py: Some examples of use (usage: python3 example.py)
4. example_output.txt: output of the example.py script in txt format
5. example_grammar*.txt: Some example grammars


# Author
```
Iker García Ferrero
```
# Example Of Use
 
```
# Initialize the grammar and read the rules from a file
 g = Grammar('example_grammar1.txt')
 # Parse a sentence
 g.parse('astronomers saw stars with ears')
 # Print the table used for parsing the sentence
 g.print_parse_table()
 # Get the trees generated for the sentence
 trees = g.get_trees()
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

RULE applied: VP[2,2] --> V[1,2] NP[1,3]
RULE applied: PP[2,4] --> P[1,4] NP[1,5]
RULE applied: S[3,1] --> NP[1,1] VP[2,2]
RULE applied: NP[3,3] --> NP[1,3] PP[2,4]
RULE applied: VP[4,2] --> V[1,2] NP[3,3]
RULE applied: VP[4,2] --> VP[2,2] PP[2,4]
RULE applied: S[5,1] --> NP[1,1] VP[4,2]
RULE applied: S[5,1] --> NP[1,1] VP[4,2]
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
The program assumes that the grammar is a valid context-free grammar in CNF form. Rules must be separated by lines. 
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




