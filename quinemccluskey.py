import math
import pandas as pd


class Data:
    df = pd.DataFrame()

    def __init__(self, decision_table, results) -> None:
        index = 0
        decimal_names = []
        weighted_groups = []
        is_prime = []
        decision_table.reverse()
        for l in decision_table:
            dec_temp = ""
            weighted_groups.append(0)
            for item in l:
                dec_temp += str(item)
                if item == 1:
                    weighted_groups[index] += 1
            index += 1
            decimal_names.append(int(dec_temp, 2))
            is_prime.append(0)
        data = {
            "decimal_names": decimal_names,
            "decision_table": decision_table,
            "weighted_groups": weighted_groups,
            "results": results,
            "is_prime": is_prime,
        }
        self.df = pd.DataFrame(
            data,
            columns=[
                "decimal_names",
                "decision_table",
                "weighted_groups",
                "results",
                "is_prime",
            ],
        )
        self.df = self.df.set_index("decimal_names")


class QuineMcCluskey:
    depth = 0
    steps = []

    def __init__(self, decision_table, results) -> None:
        self.steps.append(Data(decision_table, results))

    def hamming_distance(s1, s2):
        # Calculate the Hamming distance between two bit strings
        assert len(s1) == len(s2)
        return sum(c1 != c2 for c1, c2 in zip(s1, s2))

    def get_monomial(self):
        # get the decision_table with only 1s as output
        step1 = self.steps[0].df
        print(step1)
        return step1[step1.results.gt(0)]

    def summarize_monomials(self):
        # combine monomials from neighboring groups
        pass

    def primeimplicant_table(self):
        # make prime implicant table
        pass


qmc = QuineMcCluskey(
    [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1],
        [1, 0, 0],
        [0, 1, 1],
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 0],
    ],
    [0, 0, 0, 1, 0, 1, 2, 1],
)
print(qmc.get_monomial())