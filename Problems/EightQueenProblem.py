from Problems.problem import Problem


class EighQueenProblem(Problem):
    def __init__(self):
        super().__init__()

    def initial_state(self):
        table = [0, 0, 0, 0, 0, 0, 0, 0]
        return table

    def competency(self, state):
        return self.number_of_conflicts(state)

    def neighbors(self, state):
        l = []
        for i in range(len(state)):
            if state[i] > 0:
                tempS = state[:]
                tempS[i] -= 1
                l.append(tempS)
            if state[i] < 7:
                tempS = state[:]
                tempS[i] += 1
                l.append(tempS)
        return l

    @staticmethod
    def number_of_conflicts(table):
        total = 0
        for i in range(len(table)):
            for j in range(len(table)):
                if i is not j:
                    if table[i] == table[j] or table[i] - i == table[j] - j:
                        total += 1
        return total / 2
