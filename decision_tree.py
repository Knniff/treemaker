import numpy as np
from binarytree import build
import re

""" def convert(table):
    for row in range(len(table)):
        if table[row] == 1:
            table[row] = True
        elif table[row] == 0:
            table[row] = False
        elif table[row] == True:
            table[row] = 1
        elif table[row] == False:
            table[row] = 0
    return table """


class DecisionTree:
    function = ""
    depth = 0
    decision_table = []
    result = []

    def __init__(self, depth, function):
        self.depth = depth
        self.create_function(function)
        self.decisionTable()
        self.calculate()

    def n(self, a):
        if a == True:
            return False
        elif a == False:
            return True
        if a == 1:
            return 0
        elif a == 0:
            return 1

    def create_tree(self):
        base_tree = []
        for x in range(0, self.depth):
            times = 2 ** x
            for _ in range(times):
                base_tree.append(x + 1)
        base_tree.extend(self.result)
        tree = build(base_tree)
        print(tree)

    def create_function(self, function):
        dic = {x: chr(x + 97) for x in range(0, 26)}
        print(function)
        for item in dic:
            function = function.replace(dic[item], "INPUT[" + str(item) + "]")
        function = re.sub("(INPUT\[[0-9]\]')", "self.n(\\1)", function)
        function = function.replace("'", "").replace("+", " | ").replace("*", " & ")
        print(function)
        self.function = function

    def evaluate_function(self, INPUT):
        return eval(self.function)

    def half(self, length):
        arr = []
        for i in range(round(length / 2)):
            arr.append(1)
        for i in range(round(length / 2)):
            arr.append(0)
        return arr

    def decisionTable(self):
        arr = []
        x = 1
        p = 2.0 ** self.depth
        for row in range(self.depth):
            for n in range(0, x):
                arr.extend(self.half(p))
            p = p / 2.0
            x *= 2
        # arr.reverse()
        array = np.reshape(arr, (self.depth, 2 ** self.depth))
        print(array.T)
        self.decision_table = array.T

    def calculate(self):
        arr = []
        for row in self.decision_table:
            arr.append(self.evaluate_function(row))
        print(arr)
        self.result = arr


t = DecisionTree(2, "a+b'")
t.create_tree()