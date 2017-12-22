import Problems.EightQueenProblem

a = Problems.EightQueenProblem.EighQueenProblem()


for i in a.neighbors(a.initial_state()):
    print(a.competency(i))