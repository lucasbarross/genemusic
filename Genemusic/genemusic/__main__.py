from .Population import Population
from .Music import Music
from random import randint
from .config import NOTES
from math import floor

def run(size):
    population = Population(int(size))
    population.calcFitness()
    best = population.getFittest()
    generations = 0

    while generations < 300:
        
        matingPool = population.getMatingPool(best)
        population.breed(matingPool)
        population.calcFitness()

        best = population.getFittest()
        
        generations += 1
        print("GENERATIONS: ", generations, "BEST FITNESS:", best.fitness)

    best.printNotes()
    print("FITNESS", best.fitness)

if __name__ == "__main__":
    import sys
    run(sys.argv[1])