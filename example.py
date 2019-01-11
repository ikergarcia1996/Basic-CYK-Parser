#usage: pyhton3 example.py

from CYK_Paser import Grammar

g = Grammar('example_grammar1.txt')
g.parse('astronomers saw stars with ears')
g.print_parse_table()

print('')
print('')
print('')

g = Grammar('example_grammar2.txt')
g.parse('she eats a fish with a fork')
g.print_parse_table()

print('')
print('')
print('')

g = Grammar('example_grammar2.txt')
g.parse('eats she fork a fish')
g.print_parse_table()
g.get_trees()


