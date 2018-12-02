from pulp import *
from gurobipy import *
import pandas as pd
import os
DATA_DIR = './data'
df = pd.read_pickle(os.path.join(DATA_DIR, 'bugzilla_eclipse_log(comments)_2016meancost.pkl'))


cnt = 0
#print(len(df))
idx = [x for x in range(len(df))]
prob = LpProblem("term_project", LpMaximize)

answer = LpVariable.dicts("answer",idx,0,1,LpInteger)

prob += lpSum([df.values[i][4]*answer[i] for i in idx])

prob += lpSum([df.values[j][3]*answer[j] for j in idx]) <= 50700

status = prob.solve(GUROBI())


print(LpStatus[status])

#for v in prob.variables():
#	print (v.name, " = ", v.varValue)

# for w in prob.variables():
# 	if (w.varValue == 1.0):
# 		print (w.name, " = ", df.values[cnt][0])
# 	cnt += 1
print("Maximum Profit =", value(prob.objective))