import numpy as np
import pandas as pd
import pickle
import os

#load CS454/data/bugzilla_eclipse_log(comments)_2016meancost.pkl
parse_data = pd.read_pickle(os.path.join('../data', 'bugzilla_firefox_log(comments)_2016meancost.pkl'))

cost = np.zeros(len(parse_data.values))
profit = np.zeros(len(parse_data.values))

#limited th cost
maximum_cost = 262945.49580958224

#make a parsedata array by numpy
index = 0
for i in parse_data.values:
	cost[index] = i[3]
	profit[index] = i[4]
	index += 1


cost_array = np.zeros((len(cost), len(cost)))
profit_array = np.zeros((len(profit), len(profit)))

#make a pairwise comparison matrix for cost and profit
#low cost is higer point
for i in range(len(cost)):
	cost_array[i:(i+1), :] = cost/cost[i]

for i in range(len(profit)):
	profit_array[i:(i+1), :] = profit[i]/profit


#0-1nomarized and sum two pairwise comparison matrix
AHP_cost_array = ((cost_array/cost_array.sum(axis=0)).sum(axis=1))/len(cost)
AHP_profit_array = ((profit_array/profit_array.sum(axis=0)).sum(axis=1))/len(profit)
AHP_sum_array = AHP_cost_array + AHP_profit_array

AHP_result = np.zeros((len(parse_data.values), 4))
for i in range(len(parse_data.values)):
	AHP_result[i,0] = i                 #index
	AHP_result[i,1] = cost[i]			#cost
	AHP_result[i,2] = profit[i]			#profit
	AHP_result[i,3] = AHP_sum_array[i]  #AHP cost+profit

#sort to AHP cost+profit
AHP_result = AHP_result[AHP_result[:,3].argsort(kind='mergesort')[::-1]]
print(AHP_result)

#Make select result Tuple
selected = [0]*len(parse_data.values)

#result of profit with limit cost
index = 0
cost_sum = 0
profit_sum = 0
while(cost_sum+AHP_result[index,1] <= maximum_cost):
	selected[int(AHP_result[index, 0])] = 1
	cost_sum += AHP_result[index, 1]
	profit_sum += AHP_result[index,2]
	index += 1

print(cost_sum, profit_sum)

f = open('AHP_firefox_log(comments)_2016meancost.pkl', 'wb')
pickle.dump(tuple(selected), f)
f.close()





