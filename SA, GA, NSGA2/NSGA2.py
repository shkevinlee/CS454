import random
import numpy as np


class NRP_NSGA2:
    def __init__(self, profit, cost, bound, init_decision=None, pop_size=200, prob_co=0.8, iteration=10000, tournament_size=5):
        self.dimension = profit.shape[0]
        self.iteration = iteration

        self.profit = profit
        self.cost = cost
        self.bound = -bound

        self.pop = []
        for i in range(pop_size):
            tmp = np.random.randint(0, 2, (self.dimension,))
            self.pop.append({'profit': 0, 'cost': 0, 'chrm': tmp, 'Domt_set': [], 'Domt_num': 0, 'rank': 0, 'dist': 0})

        if init_decision is None:
            self.pop[0]['chrm'] = self.greedy_initial()
        else:
            self.pop[0]['chrm'] = init_decision

        self.pop_size = pop_size
        self.sel_list = []
        self.sel_size = int(pop_size * (1 - prob_co))
        self.tournament_size = tournament_size
        self.mutant_rate = 1/self.dimension
        self.fittest = None

    def greedy_initial(self):
        x = np.zeros(np.shape(self.profit))

        cp_profit = np.copy(self.profit)
        total_cost = 0

        it = 0
        while total_cost > self.bound and it < self.dimension:
            next_req = np.argmax(cp_profit)

            if total_cost + self.cost[next_req] >= self.bound:
                x[next_req] = 1
                total_cost = -np.dot(x, self.cost.T)

            it += 1
            cp_profit[next_req] = -1
        return x

    def evaluate_fitness(self):
        self.fittest = self.pop[0]

        for i in range(self.pop_size):
            chrm = self.pop[i]['chrm']
            profit = np.dot(chrm, self.profit.T)
            cost = -np.dot(chrm, self.cost.T)
            self.pop[i]['profit'] = profit
            self.pop[i]['cost'] = cost

            if self.bound < cost and self.fittest['profit'] < profit:
                self.fittest = self.pop[i]

    def fast_NS(self):
        F = []
        F_1 = []
        for p in self.pop:
            p['Domt_set'] = []
            p['Domt_num'] = 0
            for q in self.pop:
                if q['profit'] < p['profit'] and q['cost'] < p['cost']:   # if p dominate q
                    p['Domt_set'].append(q)
                elif q['profit'] > p['profit'] and q['cost'] > p['cost']:
                    p['Domt_num'] += 1

            if p['Domt_num'] == 0:
                p['rank'] = 1
                F_1.append(p)

        i = 1
        F_i = F_1
        while F_i:
            F.append(F_i)
            Q = []
            for p in F_i:
                for q in p['Domt_set']:
                    q['Domt_num'] -= 1
                    if q['Domt_num'] == 0:
                        q['rank'] = i+1
                        Q.append(q)
            i += 1
            F_i = Q
        return F

    def crowding_distance(self, F_i):
        # initialize #
        for p in F_i:
            p['dist'] = 0

        for obj in ['profit', 'cost']:
            F_i = sorted(F_i, key=lambda elm: elm[obj])
            F_i[0]['dist'], F_i[len(F_i)-1]['dist'] = 100000000, 100000000
            diff = F_i[len(F_i)-1][obj] - F_i[0][obj]
            for i in range(2, len(F_i)-1):
                F_i[i]['dist'] += (F_i[i+1][obj] - F_i[i-1][obj]) / diff
        return F_i

    def dominate(self, p, q):
        if p['rank'] < q['rank']:
            return True
        elif p['rank'] == q['rank'] and p['dist'] > q['dist']:
            return True
        return False

    def tour_selection(self):
        self.sel_list = []
        self.sel_list.append(self.fittest)

        index_list = []
        for i in range(self.sel_size-1):
            winner = -1
            tour_num = 0

            while tour_num < self.tournament_size:
                index = np.random.randint(len(self.pop))

                if index not in index_list:
                    if winner == -1:
                        winner = index
                    elif self.dominate(self.pop[index], self.pop[winner]):
                        winner = index
                    tour_num += 1
            self.sel_list.append(self.pop[winner])
            index_list.append(winner)

    def cross_over(self):
        parents = self.sel_list
        children = []
        children_size = self.pop_size/2

        while len(children) < children_size:
            random.shuffle(parents)
            start = np.random.randint(self.dimension - 1)
            child1 = np.zeros((self.dimension,))
            child2 = np.zeros((self.dimension,))

            for j in range(self.dimension):
                if j <= start:
                    child1[j] = parents[0]['chrm'][j]
                    child2[j] = parents[1]['chrm'][j]
                else:
                    child1[j] = parents[1]['chrm'][j]
                    child2[j] = parents[0]['chrm'][j]

            children.append({'profit': 0, 'cost': 0, 'chrm': child1, 'Domt_set': [], 'Domt_num': 0, 'rank': 0, 'dist': 0})
            if len(children) != children_size:
                children.append({'profit': 0, 'cost': 0, 'chrm': child2, 'Domt_set': [], 'Domt_num': 0, 'rank': 0, 'dist': 0})
        self.pop = self.pop + children
        assert len(self.pop) == self.pop_size, "cross_over, size of population is different"

    def mutation(self):
        for i in range(int(self.pop_size/2), self.pop_size):
            for j in range(self.dimension):
                w = np.random.uniform()
                if w < self.mutant_rate:
                    if self.pop[i]['chrm'][j] == 0:
                        self.pop[i]['chrm'][j] = 1
                    else:
                        self.pop[i]['chrm'][j] = 0

    def run_NSGA2(self):
        it = 0
        self.evaluate_fitness()
        while it < self.iteration:
            if it % 10 == 0:
                print(it, self.fittest['profit'])
            F = self.fast_NS()
            self.pop = []
            i = 0
            while len(self.pop) + len(F[i]) <= self.pop_size/2:
                self.crowding_distance(F[i])
                self.pop = self.pop + F[i]
                i += 1
            F[i] = sorted(F[i], key= lambda elm: elm['dist'])
            self.pop = self.pop + F[i][int(len(F[i]) - (self.pop_size/2) + len(self.pop)):]

            self.tour_selection()
            self.cross_over()
            self.mutation()

            self.evaluate_fitness()
            it += 1

        return self.fittest


