import random
import numpy as np


class NRP_GA:
    def __init__(self, profit, cost, bound, init_decision=None, pop_size=200, prob_co=0.8, iteration=10000, tournament_size=5, sp=1.5):
        self.dimension = profit.shape[0]
        self.iteration = iteration

        self.profit = profit
        self.cost = cost
        self.bound = bound

        self.pop = []
        for i in range(pop_size):
            tmp = np.random.randint(0, 2, (self.dimension,))
            self.pop.append([0, tmp])

        if init_decision is None:
            self.pop[0][1] = self.greedy_initial()
        else:
            self.pop[0][1] = init_decision

        self.pop_size = pop_size
        self.sel_list = []
        self.sel_size = int(pop_size * (1 - prob_co))
        self.tournament_size = tournament_size
        self.mutant_rate = 1/self.dimension
        self.sp = sp
        self.fittest = None
        self.worst = None

    def greedy_initial(self):
        x = np.zeros(np.shape(self.profit))

        cp_profit = np.copy(self.profit)
        total_cost = 0

        it = 0
        while it < self.dimension:
            next_req = np.argmax(cp_profit)

            if total_cost + self.cost[next_req] <= self.bound:
                x[next_req] = 1
                total_cost = np.dot(x, self.cost.T)

            it += 1
            cp_profit[next_req] = -1
        return x

    def evaluate_fitness(self):
        self.fittest = self.pop[0]
        self.worst = self.pop[0]

        for i in range(self.pop_size):
            chrm = self.pop[i][1]
            fitness = np.dot(chrm, self.profit.T)
            temp = self.bound - np.dot(chrm, self.cost.T)
            if temp < 0:
                fitness = fitness + temp
            self.pop[i][0] = fitness

            if self.fittest[0] < self.pop[i][0]:
                self.fittest = self.pop[i]
            if self.worst[0] > self.pop[i][0]:
                self.worst = self.pop[i]

    def converge_check(self):
        self.evaluate_fitness()
        # self.fittest = self.pop[0]
        # self.worst = self.pop[-1]

        error = (self.worst[0] - self.fittest[0]) / self.fittest[0]
        if error < 0.0001:
            return False
        else:
            return True

    def rank_base1(self):
        cmp = 0
        for i in range(1, self.pop_size + 1):
            scaled_rank = 2 - self.sp + (2 * (self.sp - 1) * (self.pop_size - i) / (self.pop_size - 1))
            scaled_rank /= self.pop_size
            cmp += scaled_rank
            self.pop[i-1][0] = cmp

    def rank_selection(self):
        self.sel_list = []

        self.pop.sort()
        self.rank_base1()
        self.sel_list.append(self.pop[0])
        step = 1/self.sel_size

        r = np.random.uniform(0, step)
        r += step

        current_member = 0
        i = 1
        while current_member < self.sel_size-1:
            while r < self.pop[i][0]:
                self.sel_list.append(self.pop[i])
                r += step
                current_member += 1
            i += 1

    def tour_selection(self):
        self.sel_list = []
        self.sel_list.append(self.fittest)

        index_list = []
        for i in range(self.sel_size-1):
            winner = -1
            tour_num = 0

            while tour_num < self.tournament_size:
                index = np.random.randint(self.pop_size)

                if index not in index_list:
                    if winner == -1:
                        winner = index
                    elif self.pop[index][0] > self.pop[winner][0]:
                        winner = index
                    tour_num += 1
            self.sel_list.append(self.pop[winner])
            index_list.append(winner)

    def cross_over(self):
        parents = self.sel_list
        children = []
        children_size = self.pop_size-len(parents)

        while len(children) < children_size:
            random.shuffle(parents)
            start = np.random.randint(self.dimension - 1)
            child1 = np.zeros((self.dimension,))
            child2 = np.zeros((self.dimension,))

            for j in range(self.dimension):
                if j <= start:
                    child1[j] = parents[0][1][j]
                    child2[j] = parents[1][1][j]
                else:
                    child1[j] = parents[1][1][j]
                    child2[j] = parents[0][1][j]
            children.append([0, child1])
            if len(children) != children_size:
                children.append([0, child2])
        self.pop = parents + children
        assert len(self.pop) == self.pop_size, "cross_over, size of population is different"

    def mutation(self):
        for i in range(self.sel_size, self.pop_size):
            for j in range(self.dimension):
                w = np.random.uniform()
                if w < self.mutant_rate:
                    if self.pop[i][1][j] == 0:
                        self.pop[i][1][j] = 1
                    else:
                        self.pop[i][1][j] = 0

    def run_GA(self):
        it = 0
        self.evaluate_fitness()
        while it < self.iteration:
            if it % 10 == 0:
                print(it, self.fittest[0])
            it += 1
            self.tour_selection()
            self.cross_over()
            self.mutation()

            self.evaluate_fitness()

        #print("total iteration is ", it)
        return self.fittest

    def run_GA_rank(self):
        it = 0
        self.evaluate_fitness()
        while self.converge_check() and it < self.iteration:
            #if it % 1000 == 0:
            #    print(it, self.fittest[0])
            it += 1
            self.rank_selection()
            self.cross_over()
            self.mutation()

        #print("total iteration is ", it)
        return self.fittest



