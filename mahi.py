import Problems.EightQueenProblem
import Problems.graphpartitioning
import hillCilmbing

a = Problems.EightQueenProblem.EighQueenProblem()
b = Problems.graphpartitioning.GraphPartitioningProblem()


hillc = hillCilmbing.HillClimbing()
hillc.setProblem(a)
hillc.search('rand-start')
