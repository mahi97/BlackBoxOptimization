import Problems.EightQueenProblem
import Problems.graphpartitioning
import Problems.SimpleMathEquationProblem
import hillCilmbing
import SA
import genetic
import random
import matplotlib.pyplot as plt
from matplotlib.pyplot import setp
from time import clock
import os
import numpy as np
a = Problems.EightQueenProblem.EighQueenProblem()
b = Problems.graphpartitioning.GraphPartitioningProblem()
c = Problems.SimpleMathEquationProblem.SimpleMathEquationProblem()

# hillc = hillCilmbing.HillClimbing()
# hillc.setProblem(a)
# hillc.search('rand-start')
# print(hillc.nodeExpand)
# print(hillc.nodeSeen)

# sa = SA.SA()
# sa.set_problem(b)
# sa.search('3')
# sa.counter = 0
# print('Best :' , sa.BS, ' Score : ', sa.B)
# sa.B = 10000
# print(sa.nodeSeen)
# print(sa.nodeExpand)
#
# print('--------')
# sa.search('2')
# sa.counter = 0
# print('Best :' , sa.BS, ' Score : ', sa.B)
# sa.B = 100000
#
# print('--------')
# sa.search('3')
# print('Best :' , sa.BS, ' Score : ', sa.B)

genetic = genetic.Genetic()
genetic.problem = c
genetic.generate_chromosome()
while not genetic.end():
    print('Spin : ', genetic.currentGen)
    genetic.evaluation_fitness()
    genetic.select_chromosome()
    genetic.cross_over()
    genetic.mutation()
genetic.answer()

c_time = genetic.bestG

python_time = genetic.meanG
new_time = genetic.worstG

plt.savefig('result.pdf')
fig = plt.figure(1)
ax = plt.axes([0.1, 0.1, 0.8, 0.8])
setp(ax, 'frame_on', False)
# Plot here

##############################################
degree = np.arange(0, len(c_time))
# python_time = degree  # replace with f(degree)
# c_time = degree + 1 # replace with f(degree)
##############################################

ax.plot(degree, genetic.bestG, label='Best', marker='o')
ax.plot(degree, genetic.worstG, label='Worst', marker='o')
ax.plot(degree, genetic.meanG, label='Mean', marker='o')
# End Plot
ax.set_xlabel(r'Iteration (n)')
ax.set_ylabel(r'Competency')
handle, label = ax.get_legend_handles_labels()
ax.legend(handle, label, loc='upper left', bbox_to_anchor=(0.01, 0.99), ncol=1, labelspacing=0.3, fancybox=True,
          shadow=True,
          columnspacing=1, borderpad=0.2, title='', handletextpad=0.1,
          numpoints=1, handlelength=1.5, markerscale=1)
plt.savefig(os.path.join(os.getcwd(), 'result.png'))
