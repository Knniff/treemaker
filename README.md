# treemaker

This python program creates a binary decision tree when given the tree-depth and a function.

> example:

```
t = DecisionTree(3, "a|b'*c")
t.print_tree()
        ______1______
       /             \
    __2__           __2__
   /     \         /     \
  3       3       3       3
 / \     / \     / \     / \
1   1   1   1   0   0   1   0
```

The function has to be written in this style:

> ## operators
>
> - inputs: a - z
> - brackets: ()
> - negation: '
> - add/or: + or |
> - multiply/and: \* or &
>
> > example: "(a|b')\*(c'+a&a)"

uses pythons eval()-function, which can be dangerous with unchecked input. The input is checked before execution in eval() and throws an Exception if check fails.

## roadmap

- implement a table maker for any function
- implement implication and aquivalency conversion
- implement quine-mccluskey algorithm

## used packages

- numpy, binarytree, regex

## codestyle
- formatted with black
