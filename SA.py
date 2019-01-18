import Problems.problem
import random
import numpy as np


class SA:
    def __init__(self):
        self.problem = Problems.problem.Problem
        self.counter = 0
        self.BS = []
        self.B = 100000
        self.nodeSeen = 0
        self.nodeExpand = 0

    def set_problem(self, _problem):
        self.problem = _problem

    def search(self, mode):
        if mode == '1':
            self.first_search(self.problem.initial_state(), lambda x: 1-(x/200))
        elif mode == '2':
            self.first_search(self.problem.initial_state(), lambda x: 1/np.exp(x/100))
        elif mode == '3':
            self.first_search(self.problem.initial_state(), lambda x: np.cos(x/200*np.pi))

    def first_search(self, state, p):
        self.counter += 1
        best = self.problem.competency(state)

        if best < self.B:
            self.B = best
            self.BS = state

        bestList = []
        for s in self.problem.neighbors(state):
            self.nodeSeen += 1
            if self.problem.competency(s) <= best:
                bestList.append(s)

        print("Temp : " , p(self.counter))
        r =  random.random()
        if r < p(self.counter):
            print("NOT Find Answer or Local : ", state, " with score : ", best)
            self.nodeExpand += 1
            self.first_search(self.problem.neighbors(state)[np.random.randint(0, len(self.problem.neighbors(state)))], p)
        elif len(bestList) != 0:
            print("BEST Find Answer or Local : ", state, " with score : ", best)
            self.nodeExpand += 1
            self.first_search(bestList[np.random.randint(0, len(bestList))], p)

        # for s in self.problem.neighbors(state):
        #     if self.problem.competency(s) < best:
        #         print("BEST Find Answer or Local : ", state, " with score : ", best)
        #         self.first_search(s, p)
        #         break
        #     elif random.random() < p(self.counter+1):
        #         print("NOT Find Answer or Local : ", state, " with score : ", best)
        #         self.first_search(s, p)
        #         break
