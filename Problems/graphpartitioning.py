from Problems.problem import Problem
import numpy as np


class GraphPartitioningProblem(Problem):
    def __init__(self):
        super().__init__()
        self.graph = {
            0: [1, 2],
            1: [0, 2, 3, 11],
            2: [0, 1, 4],
            3: [1, 4, 6],
            4: [2, 3, 5],
            5: [4, 6],
            6: [3, 5, 7, 10],
            7: [6, 8],
            8: [7, 9, 10],
            9: [8, 10],
            10: [6, 8, 9, 11],
            11: [1, 10]
        }

    def initial_state(self):
        return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    def neighbors(self, state):
        l = []
        for i in range(len(state)):
            temp = [t for t in state if t is not state[i]]
            if temp is not state:
                l.append(temp)
        for i in range(12):
            temp = state[:]
            if i not in state:
                temp.append(i)
                l.append(temp)

        return l

    def competency(self, state):
        cost = np.abs(6 - len(state)) * 2
        for i in range(len(state)):
            for v in self.graph[state[i]]:
                if v not in state:
                    cost += 1
        return cost
