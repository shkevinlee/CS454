import numpy as np
import pandas as pd
import pickle
import os


class NRP_AHP:
    def __init__(self, profit, cost, bound):
        self.dimension = profit.shape[0]

        self.profit = profit
        self.cost = cost
        self.bound = bound

    def run_AHP(self):
        cost_array = np.zeros((self.dimension, self.dimension))
        profit_array = np.zeros((self.dimension, self.dimension))

        for i in range(self.dimension):
            cost_array[i:(i + 1), :] = self.cost / self.cost[i]
            profit_array[i:(i + 1), :] = self.profit[i] / self.profit

        # 0-1 normalization and sum two pairwise comparison matrix
        AHP_cost_array = ((cost_array / cost_array.sum(axis=0)).sum(axis=1)) / self.dimension
        AHP_profit_array = ((profit_array / profit_array.sum(axis=0)).sum(axis=1)) / self.dimension

        AHP_sum_array = AHP_cost_array + AHP_profit_array

        AHP_result = np.zeros((self.dimension, 4))

        for i in range(self.dimension):
            AHP_result[i, 0] = i  # index
            AHP_result[i, 1] = self.cost[i]  # cost
            AHP_result[i, 2] = self.profit[i]  # profit
            AHP_result[i, 3] = AHP_sum_array[i]  # AHP cost+profit

        # sort to AHP cost+profit
        AHP_result = AHP_result[AHP_result[:, 3].argsort(kind='mergesort')[::-1]]

        # Make select result Tuple
        selected = [0] * self.dimension

        # result of profit with limit cost
        index = 0
        cost_sum = 0
        profit_sum = 0
        while cost_sum + AHP_result[index, 1] <= self.bound:
            selected[int(AHP_result[index, 0])] = 1
            cost_sum += AHP_result[index, 1]
            profit_sum += AHP_result[index, 2]
            index += 1

        return cost_sum, profit_sum, selected






