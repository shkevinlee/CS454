import numpy as np
import SIM_ANEAL
import GA
import pandas as pd

test = pd.read_excel("TestData.xlsx")
test_pkl = pd.read_pickle("bugzilla_firefox_2017_random01.pkl")

print(test_pkl['Profit'].shape)
print(test_pkl['Cost'].shape)

test_SA = SIM_ANEAL.NRP_SA(profit=test_pkl['Profit'], cost=test_pkl['Cost'], bound=100)
test_GA = GA.NRP_GA(profit=test_pkl['Profit'], cost=test_pkl['Cost'], bound=100)

result1 = test_SA.run_SA()
result2 = test_GA.run_GA()

print(result1)
print(result2)




