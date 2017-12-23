import Problems.EightQueenProblem
import Problems.graphpartitioning
import hillCilmbing
import SA
import random

a = Problems.EightQueenProblem.EighQueenProblem()
b = Problems.graphpartitioning.GraphPartitioningProblem()

# hillc = hillCilmbing.HillClimbing()
# hillc.setProblem(a)
# hillc.search('rand-start')

sa = SA.SA()
sa.set_problem(b)
sa.search('1')
sa.counter = 0
print('Best :' , sa.BS, ' Score : ', sa.B)
sa.B = 10000

print('--------')
sa.search('2')
sa.counter = 0
print('Best :' , sa.BS, ' Score : ', sa.B)
sa.B = 100000

print('--------')
sa.search('3')
print('Best :' , sa.BS, ' Score : ', sa.B)
