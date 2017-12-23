import Problems.problem
import numpy as np
import random


class HillClimbing:
    def __init__(self):
        self.problem = Problems.problem.Problem()
        self.counter = 0
        self.Best = 0
        self.BestState = []

    def setProblem(self, _problem):
        self.problem = _problem

    def search(self, mode):
        if mode == 'simple':
            self.simple_search(self.problem.initial_state())
        elif mode == 'rand':
            self.rand_search(self.problem.initial_state())
        elif mode == 'first':
            self.first_search(self.problem.initial_state())
        elif mode == 'rand-start':
            self.rand_start_search(self.problem.initial_state(), False)

    def rand_start_search(self, state, rand):
        self.counter += 1
        best = self.Best
        bestState = self.BestState
        if not rand:
            best = self.problem.competency(state)
            bestState = state
            self.Best = best
            self.BestState = bestState
        find = False
        for s in self.problem.neighbors(state):
            if self.problem.competency(s) < best:
                best = self.problem.competency(s)
                bestState = s
                find = True

        if best == 0 or self.counter > 200:
            print("LAST : Find Answer or Local : ", bestState, " with score : ", best)
            return

        if find:
            print("Find Answer or Local : ", bestState, " with score : ", best)
            self.rand_start_search(bestState, False)
        else:
            self.rand_start_search(random.sample(range(0, 8), 8), True)
            print("RAND : Find Answer or Local : ", bestState, " with score : ", best)

    def first_search(self, state):
        self.counter += 1
        best = self.problem.competency(state)

        if best == 0 or self.counter > 200:
            print("Find Answer or Local : ", state, " with score : ", best)
            return
        else:
            print("Find Answer or Local : ", state, " with score : ", best)

        for s in self.problem.neighbors(state):
            if self.problem.competency(s) < best:
                self.first_search(s)
                break

    def rand_search(self, state):
        self.counter += 1
        best = self.problem.competency(state)
        bestList = []
        for s in self.problem.neighbors(state):
            if self.problem.competency(s) <= best:
                bestList.append(s)
        if best == 0 or self.counter > 200 or len(bestList) is 0:
            print("Find Answer or Local : ", state, " with score : ", best)
        else:
            print("Find Answer or Local : ", state, " with score : ", best)
            self.rand_search(bestList[np.random.randint(0, len(bestList))])

    def simple_search(self, state):
        best = self.problem.competency(state)
        bestState = state
        find = False
        for s in self.problem.neighbors(state):
            if self.problem.competency(s) < best:
                best = self.problem.competency(s)
                bestState = s
                find = True
        if find:
            self.simple_search(bestState)
        else:
            print("Find Answer or Local : ", bestState, " with score : ", best)
