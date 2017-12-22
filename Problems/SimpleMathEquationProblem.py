from Problems.problem import Problem

class SimpleMathEquationProblem(Problem):

    def __init__(self):
        super().__init__()

    def initial_state(self):
        return [0, 0, 0, 0]

    def neighbors(self, state):
        pass