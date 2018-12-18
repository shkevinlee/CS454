import numpy as np
import SIM_ANEAL
import GA
import NSGA2
import pandas as pd

# test_pkl = pd.read_pickle("bugzilla_eclipse_log(comments)_2016meancost.pkl")
test_pkl = pd.read_pickle("bugzilla_firefox_priority_2016meancost.pkl")

print(test_pkl['Profit'].shape)
print(test_pkl['Cost'].shape)


# test_SA = SIM_ANEAL.NRP_SA(profit=test_pkl['Profit'], cost=test_pkl['Cost'], bound=262945.49580958224, iteration=1000000)
# test_GA = GA.NRP_GA(profit=test_pkl['Profit'], cost=test_pkl['Cost'], bound=50600, iteration=5000)
# test_NSGA2 = NSGA2.NRP_NSGA2(profit=test_pkl['Profit'], cost=test_pkl['Cost'], bound=262945.49580958224, iteration=2500)
test_MNSGA2 = modified_NSGA2.NRP_MNSGA2(profit=test_pkl['Profit'], cost=test_pkl['Cost'], bound=262945.49580958224, iteration=2500)


# result_SA = test_SA.run_SA()
# result_GA = test_GA.run_GA()
# result_NSGA2 = test_NSGA2.run_NSGA2()

result_MNSGA2 = test_MNSGA2.run_MNSGA2()

# print(len(result_NSGA2))
# print(result_NSGA2)




