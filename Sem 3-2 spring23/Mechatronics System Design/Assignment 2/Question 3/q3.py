import itertools
import pandas as pd

L = int(input("Number of links: "))
O = int(input("Maximum order of links: "))
DoF = int(input("Enter number of degrees of freedom: "))

def do_problem(n_links, max_order, rhs):
    solutions = []
    for combination in itertools.combinations_with_replacement(range(max_order), n_links):
        if sum(combination) == rhs:
            solution = {"Order{}".format(i): combination.count(i) for i in range(4)}
            solutions.append(solution)
    return solutions

solutions = []
for n_links in range(2, L+1, 2 if DoF % 2 == 1 else 1):
    rhs = n_links - 3 - DoF
    if rhs < 0:
        continue
    max_order = min(O, rhs // (n_links - 2) + 2)
    solutions += do_problem(n_links, max_order, rhs)

df = pd.DataFrame(solutions)
df["Number of Links"] = range(2, L+1, 2 if DoF % 2 == 1 else 1)
df.set_index("Number of Links", inplace=True)

print("All possible combinations with {} links, {} degrees of freedom and maximum order of link {}:".format(L, DoF, O))
pd.set_option('display.max_colwidth', None)
print(df)