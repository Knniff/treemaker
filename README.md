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

uses pythons eval()-function, which can be dangerous with unchecked input. There is no sanitation of the input before executed in eval()!
