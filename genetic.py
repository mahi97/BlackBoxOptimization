import Problems.problem
import random


class Genetic:
    def __init__(self):
        self.chromosomes = 2
        self.Maxgeneration = 3000
        self.currentGen = 0
        self.mutationRate = .2
        self.crossoverRate = .35
        self.chromosomesList = []
        self.fitness = []
        self.prob = []
        self.problem = Problems.problem.Problem()
        self.ans = []
        self.bestG = []
        self.meanG = []
        self.worstG = []

    def generate_chromosome(self):
        for _ in range(self.chromosomes):
            self.chromosomesList.append(random.sample(range(0, 30), 4))

    def evaluation_fitness(self):
        self.currentGen += 1
        fitness = []
        for c in self.chromosomesList:
            fitness.append(self.problem.competency(c))
        self.fitness.clear()
        for f in fitness:
            self.fitness.append(1 / (1 + f))

    def select_chromosome(self):
        print(self.chromosomesList)
        total = sum(self.fitness)
        cumulative = []
        self.prob.clear()
        for f in self.fitness:
            self.prob.append(f / total)
            cumulative.append(sum(self.prob))

        best = 0
        bestid = 0
        for i in range(len(self.prob)):
            if self.prob[i] > best:
                best = self.prob[i]
                bestid = i

        newChromosomesList = [self.chromosomesList[bestid][:]]
        newChromosomesList = []
        for _ in range(self.chromosomes):
            rand = random.uniform(0, 1)
            count = 0
            for c in cumulative:
                if rand < c:
                    newChromosomesList.append(self.chromosomesList[count][:])
                    break
                else:
                    count += 1
        self.chromosomesList = newChromosomesList
        print(self.chromosomesList)

    def cross_over(self):
        parent = []
        for i in range(self.chromosomes):
            if random.random() < self.crossoverRate:
                if self.chromosomesList[i] not in parent:
                    parent.append(self.chromosomesList[i][:])
        child = []
        if len(parent) < 2:
            return
        for i in range(len(parent)):
            for j in range(i, len(parent)):
                if i is not j:
                    r = random.randint(1, 3)
                    c = parent[i][:r] + parent[j][r:]
                    child.append(c)

        for c in child:
            self.chromosomesList.append(c)

    def mutation(self):
        total_gen = 4 * len(self.chromosomesList)
        number_of_mute = int(total_gen * self.mutationRate)
        for n in range(number_of_mute):
            rand = random.randint(0, total_gen - 1)
            self.chromosomesList[int(rand / 4)][rand % 4] = random.randint(0, 30)

    def end(self):
        fitness = []
        ans = False
        for c in self.chromosomesList:
            fitness.append(self.problem.competency(c))
            if self.problem.competency(c) == 0:
                self.ans = c
                ans = True
        if self.currentGen > self.Maxgeneration:
            ans = True
        self.bestG.append(min(fitness))
        self.worstG.append(max(fitness))
        self.meanG.append(sum(fitness) / len(fitness))
        return ans

    def answer(self):
        print('ANS is : ', self.ans)
