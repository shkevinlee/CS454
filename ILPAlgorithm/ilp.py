from pulp import *
import pandas as pd
import os
DATA_DIR = './data'
df = pd.read_pickle(os.path.join(DATA_DIR, 'bugzilla_firefox_2017_random01.pkl'))
cnt = 0
print(df.values[260:300])
print(len(df))
idx = [x for x in range(10)]
prob = LpProblem("term_project", LpMaximize)

answer = LpVariable.dicts("answer",idx,0,1,LpInteger)

prob += lpSum([df.values[i][4]*answer[i] for i in idx])

prob += lpSum([df.values[j][3]*answer[j] for j in idx]) <= 15

status = prob.solve()


print(LpStatus[status])

for v in prob.variables():
	print (v.name, " = ", v.varValue)

for w in prob.variables():
	if (w.varValue == 1.0):
		print (w.name, " = ", df.values[cnt][0])
	cnt += 1
print("Maximum Profit = ", value(prob.objective))