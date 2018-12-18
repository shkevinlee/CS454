import numpy as np
import pandas as pd

from AHP import AHP
from SA_GA_NSGAII import GA, NSGA2, SIM_ANEAL


# The Datasets we used in projects
file1 = pd.read_pickle("Dataset/bugzilla_eclipse_log(comments)_2016meancost.pkl")
file2 = pd.read_pickle("Dataset/bugzilla_firefox_log(comments)_2016meancost.pkl")
file3 = pd.read_pickle("Dataset/bugzilla_firefox_priority_2016meancost.pkl")
file4 = pd.read_pickle("Dataset/bugzilla_firefox_comments+priority_2016meancost.pkl")

file_list = [file1, file2, file3, file4]
bound_list = [50699.701903571, 262945.49580958224, 262945.49580958224, 262945.49580958224]


# AHP
# If you want to test the AHP, then please remove quotation marks
"""
index = 1      # Which dataset do you want to test in the file_list?

test_pkl = file_list[index]
test_AHP = AHP.NRP_AHP(profit=test_pkl['Profit'], cost=test_pkl['Cost'], bound=bound_list[index])

result = test_AHP.run_AHP()
print(result)
"""

# Simulated Annealing
# If you want to test the SA, then please remove quotation marks
"""
index = 1      # Which dataset do you want to test in the file_list?

test_pkl = file_list[index]
test_SA = SIM_ANEAL.NRP_SA(profit=test_pkl['Profit'], cost=test_pkl['Cost'], bound=bound_list[index], iteration=500000)

result = test_SA.run_SA()
print(result)
"""

# Genetic Algorithm
# If you want to test the GA, then please remove quotation marks
"""
index = 1      # Which dataset do you want to test in the file_list?

test_pkl = file_list[index]
test_GA = GA.NRP_GA(profit=test_pkl['Profit'], cost=test_pkl['Cost'], bound=bound_list[index], iteration=2500)

result = test_GA.run_GA()
print(result)
"""


# NSGA-II
# If you want to test the NSGA-II, then please remove quotation marks
"""
index = 1      # Which dataset do you want to test in the file_list?

test_pkl = file_list[index]
test_NSGA2 = NSGA2.NRP_NSGA2(profit=test_pkl['Profit'], cost=test_pkl['Cost'], bound=bound_list[index], iteration=2500)

result = test_NSGA2.run_NSGA2()
print(result)
"""

# the NSGA-II result is population. So if you want to get the maximum profit among them, you have to run following code
"""
best_profit = None
bound = bound_list[index]
for i in range(len(result)):
    if best_profit is None and result[i]['cost'] >= -bound:
        best_profit = result[i]['profit']
        x = result[i]['chrm']
    elif result[i]['cost'] >= -bound and result[i]['profit'] > best_profit:
        best_profit = result[i][j]['profit']
        x = result[i]['chrm']

print(best_profit, x)
"""

