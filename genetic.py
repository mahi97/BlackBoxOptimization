import Problems.problem
import random
import pprint

class Genetic:
    def __init__(self):
        self.chromosomes = 6
        self.Maxgeneration = 50
        self.currentGen = 0
        self.mutationRate = 1
        self.crossoverRate = 2
        self.chromosomesList = []
        self.fitness = []
        self.prob = []
        self.problem = Problems.problem.Problem()
        self.ans = []

    def generate_chromosome(self):
        for _ in range(self.chromosomes):
            self.chromosomesList.append(random.sample(range(0, 30), 4))

    def evaluation_fitness(self):
        self.currentGen += 1
        fitness = []
        self.fitness.clear()
        for c in self.chromosomesList:
            fitness.append(self.problem.competency(c))
        for f in fitness:
            self.fitness.append(1 / (1 + f))

    def select_chromosome(self):
        total = sum(self.fitness)
        cumulative = []
        for f in self.fitness:
            self.prob.append(f / total)
            cumulative.append(sum(self.prob))
        newChromosomesList = []
        for _ in self.chromosomesList:
            rand = random.random()
            count = 0
            for c in cumulative:
                if rand < c:
                    newChromosomesList.append(self.chromosomesList[count])
                    break
                else:
                    count += 1
        self.chromosomesList = newChromosomesList

    def cross_over(self):
        parent = []
        for i in range(self.chromosomes):
            if random.random() < self.crossoverRate:
                parent.append(self.chromosomesList[i])
        child = []
        for i in parent:
            for j in parent:
                r = random.randint(1, 3)
                c = i[:r] + j[r:]
                child.append(c)
        diff = len(child) - len(parent)
        for p in parent:
            if diff > 0:
                self.chromosomesList.remove(p)
                diff -= 1
        for c in child:
            self.chromosomesList.append(c)

    def mutation(self):
        total_gen = 4 * len(self.chromosomesList)
        number_of_mute = int(total_gen * self.mutationRate)
        for n in range(number_of_mute):
            rand = random.randint(0, total_gen - 1)
            self.chromosomesList[int(rand / 4)][rand % 4] = random.randint(0, 30)

    def end(self):
        for c in self.chromosomesList:
            if self.problem.competency(c) == 0:
                self.ans = c
                return True
        if self.currentGen > self.Maxgeneration:
            return True
        return False

    def answer(self):
        print('ANS is : ', self.ans)
