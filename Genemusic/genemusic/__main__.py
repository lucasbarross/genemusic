from .Population import Population
from .Music import Music
from random import randint
from .config import NOTES
from math import floor

def run(size):
    population = Population(int(size))
    population.calcFitness()
    best = population.getFittest()
    bestSoFar = best
    generations = 0

    while generations < 1000:
        
        matingPool = population.getMatingPool(best)
        population.breed(matingPool)
        population.calcFitness()

        # print("Generation", generations,"FITTEST", best.fitness)
        best = population.getFittest()
        
        if bestSoFar.fitness < best.fitness:
            bestSoFar = best
        
        generations += 1
        print("GENERATIONS: ", generations, "BEST FITNESS:", bestSoFar.fitness)

    bestSoFar.printNotes()
    print("FITNESS", bestSoFar.fitness)

if __name__ == "__main__":
    import sys
    run(sys.argv[1])