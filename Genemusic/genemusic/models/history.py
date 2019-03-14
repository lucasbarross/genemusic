from .population import Population

class History:

    def __init__(self, population_size, max_generations, scale):
        self.population_size = int(population_size)
        self.max_generations = max_generations
        self.scale = scale
        self.bestOfEachGeneration = []
        self.bestFitness = 0

    def run(self):
        population = Population(self.population_size, self.scale)
        population.calcFitness()
        best = population.getFittest()
        
        bestOfEachGeneration = [best.getInfo()]
        
        print("GENERATIONS: ", 0, "BEST FITNESS:", best.fitness)

        generations = 1

        while generations < self.max_generations:
            
            matingPool = population.getMatingPool(best)
            population.breed(matingPool)
            population.calcFitness()

            best = population.getFittest()
            
            bestOfEachGeneration.append(best.getInfo())

            generations += 1
            

        print("GENERATIONS: ", generations, "BEST FITNESS:", best.fitness)
        
        self.bestOfEachGeneration = bestOfEachGeneration
        self.bestFitness = best.fitness

        return bestOfEachGeneration

    def getBestFitness(self):
        return self.bestFitness