import numpy as np
import SIM_ANEAL
import GA
import NSGA2
import pandas as pd

test = pd.read_excel("TestData.xlsx")
test_pkl = pd.read_pickle("bugzilla_eclipse_log(comments)_2016meancost.pkl")

print(test_pkl['Profit'].shape)
print(test_pkl['Cost'].shape)


test_SA = SIM_ANEAL.NRP_SA(profit=test_pkl['Profit'], cost=test_pkl['Cost'], bound=50699.701903571,
                           iteration=100000, init_decision=np.random.randint(0, 2, test_pkl['Profit'].shape))
test_GA = GA.NRP_GA(profit=test_pkl['Profit'], cost=test_pkl['Cost'], bound=50699.701903571, iteration=5000)
test_NSGA2 = NSGA2.NRP_NSGA2(profit=test_pkl['Profit'], cost=test_pkl['Cost'], bound=50699.701903571, iteration=5000)

# result_SA = test_SA.run_SA()
result_GA = test_GA.run_GA()
# result_NSGA2 = test_NSGA2.run_NSGA2()

print(result_SA)
# print(result_NSGA2)




