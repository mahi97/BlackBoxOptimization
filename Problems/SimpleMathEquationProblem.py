from Problems.problem import Problem
import numpy as np

class SimpleMathEquationProblem(Problem):
    def __init__(self):
        super().__init__()

    def initial_state(self):
        return [0, 0, 0, 0]

    def neighbors(self, state):
        pass

    def competency(self, state):
        ans = state[0] + 2 * state[1] + 3 * state[2] + 4 * state[3] - 40
        return np.abs(ans)
