# treemaker

This  python creates a binary decision tree when given the tree depth and a function.

The function has to be written in this style:

> inputs: a - z
  operators:
    -brackets: ()
    -negation: '
    -multiply/and: * or &
    -add/or: + or |
  example: "(a|b')*(c'+a&a)"
