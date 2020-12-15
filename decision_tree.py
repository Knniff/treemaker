import numpy as np
from binarytree import build
import regex


class DecisionTree:
    function = ""
    depth = 0
    decision_table = []
    result = []

    # constructor which first sets the needed depth and then creates everything need for the tree
    def __init__(self, depth, function):
        self.depth = depth
        self.create_function(function)
        self.decision_table()
        self.calculate()

    # negates the given variable
    def n(self, a):
        if a == 1:
            return 0
        elif a == 0:
            return 1

    # creates tree from the given depth and the calculated result
    # sadly the package used only allows integers as node names
    def create_tree(self):
        base_tree = []
        for x in range(0, self.depth):
            times = 2 ** x
            for _ in range(times):
                base_tree.append(x + 1)
        base_tree.extend(self.result)
        tree = build(base_tree)
        return tree

    # prints the tree to stdout
    def print_tree(self):
        print(self.create_tree())

    # saves tree to specified file and overwrites everything already in it
    def save_tree(self, filename):
        if filename:
            with open(filename, mode="w") as file:
                file.write(str(self.create_tree()))

    # prepares the given function for eval()
    def create_function(self, function):
        # checks function for forbidden combinations or operators
        if (bool(regex.match(r"^[a-z()'+|*&]+$", function))) & (
            not bool(regex.search(r"([a-z]){2,}", function))
        ):
            dic = {x: chr(x + 97) for x in range(0, 26)}
            for item in dic:
                function = function.replace(dic[item], "INPUT[" + str(item) + "]")
            function = regex.sub(r"(INPUT\[[0-9]\]')", "self.n(\\1)", function)
            while regex.findall(r"((\((INPUT\[[0-9]\]|(?2)|(?0))([\*&|+]((INPUT\[[0-9]\])|(?2)|(?0)))*\))')", function):
                function = regex.sub(r"((\((INPUT\[[0-9]\]|(?2)|(?0))([\*&|+]((INPUT\[[0-9]\])|(?2)|(?0)))*\))')", "self.n(\\2)", function)
            function = function.replace("'", "").replace("+", " | ").replace("*", " & ")
            self.function = function
        else:
            raise Exception(
                "You used a blacklisted operator or had 2+ inputs next to each other"
            )

    # returns the calculated row
    # eval is used which is a dangerous function with the wrong input
    def evaluate_function(self, INPUT):
        return eval(self.function)

    # creates the decisiontable with the specified depth as number of inputs
    def decision_table(self):
        arr = []
        x = 1
        p = 2.0 ** self.depth
        for row in range(self.depth):
            for n in range(0, x):
                arr.extend(self.half(p))
            p = p / 2.0
            x *= 2
        array = np.reshape(arr, (self.depth, 2 ** self.depth))
        self.decision_table = array.T

    # helper function for decisiontable
    def half(self, length):
        arr = []
        for i in range(round(length / 2)):
            arr.append(1)
        for i in range(round(length / 2)):
            arr.append(0)
        return arr

    # calls evaluate_function() for every row of the decisiontable
    def calculate(self):
        arr = []
        for row in self.decision_table:
            arr.append(self.evaluate_function(row))
        self.result = arr


# instantiate
t = DecisionTree(3, "((a*b)'*a|b)'*c")
# print the created the decisiontable created while instanciating
print(t.decision_table)
# print the results calculated from the decisiontable and function
print(t.result)
# print tree to stdout
t.print_tree()
# save tree to specified file
t.save_tree("test.txt")