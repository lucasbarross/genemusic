from .population import Population

class History:

    def __init__(self, population_size, max_generations, scale):
        self.population_size = int(population_size)
        self.max_generations = max_generations
        self.scale = scale
        self.bestOfEachGeneration = []

    def run(self):
        population = Population(self.population_size, self.scale)
        population.calcFitness()
        best = population.getFittest()
        
        bestOfEachGeneration = [best.getNotes()]
        
        print("GENERATIONS: ", 0, "BEST FITNESS:", best.fitness)

        generations = 1

        while generations < self.max_generations and best.fitness < 210:
            
            matingPool = population.getMatingPool(best)
            population.breed(matingPool)
            population.calcFitness()

            best = population.getFittest()
            
            bestOfEachGeneration.append(best.getNotes())

            generations += 1
            
            print("GENERATIONS: ", generations, "BEST FITNESS:", best.fitness)

        self.bestOfEachGeneration = bestOfEachGeneration

        return bestOfEachGeneration