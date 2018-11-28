import numpy as np
import random


class NRP_SA():
    def __init__(self, profit, cost, bound, init_decision=None, T=-1, beta = 0.00000001, stopping_T=0, iteration=10000):
        self.dimension = profit.shape[0]
        self.T = np.sqrt(self.dimension) if T == -1 else T
        self.beta = beta
        self.stopping_temperature = stopping_T
        self.stopping_iter = iteration
        self.iteration = 0

        self.profit = profit
        self.cost = cost
        self.bound = bound

        if init_decision is None:
            self.cur_decision = self.greedy_initial()
        else:
            self.cur_decision = init_decision
        self.best_decision = list(np.copy(self.cur_decision))

        self.cur_fitness = self.evaluate_fitness(self.cur_decision)
        self.best_fitness = self.cur_fitness

    def greedy_initial(self):
        x = np.zeros(np.shape(self.profit))

        cp_profit = np.copy(self.profit)
        total_cost = 0

        it = 0
        while total_cost < self.bound and it < self.dimension:
            next_req = np.argmax(cp_profit)

            if total_cost + self.cost[next_req] > self.bound:
                it += 1
                cp_profit[next_req] = -1
            else:
                it += 1
                x[next_req] = 1
                total_cost = np.dot(x, self.cost.T)
        return x

    def evaluate_fitness(self, x):
        fitness = np.dot(x, self.profit.T)
        temp = self.bound - np.dot(x, self.cost.T)
        if temp >= 0:
            return fitness
        else:
            return fitness + temp

    def acceptance_ratio(self, new_fitness):
        if new_fitness >= self.cur_fitness:
            return 1
        else:
            return np.exp((new_fitness - self.cur_fitness) / self.T)

    def run_SA(self):
        while self.T >= self.stopping_temperature and self.iteration < self.stopping_iter:
            #if self.iteration % 1000 == 0:
            #    print(self.iteration, self.best_fitness)

            new_decision = np.copy(self.cur_decision)
            for i in range(new_decision.shape[0]):
                prob = np.random.rand()
                if 1/self.dimension < prob:
                    if new_decision[i] == 0:
                        new_decision[i] = 1
                    else:
                        new_decision[i] = 0

            new_fitness = self.evaluate_fitness(new_decision)
            if self.acceptance_ratio(new_fitness) >= random.random():
                self.cur_decision = new_decision
                self.cur_fitness = new_fitness
                if new_fitness > self.best_fitness:
                    self.best_decision = list(np.copy(self.cur_decision))
                    self.best_fitness = new_fitness

            self.T /= 1 + (self.beta * self.T)
            self.iteration += 1

        return self.best_decision, self.best_fitness

