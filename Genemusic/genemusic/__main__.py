from .Population import Population

def run(size):
    population = Population(int(size))
    population.calculateFitness()
    print(population.getFittest().fitness)
    while population.getFittest().fitness < 4:
        individualOne, individualTwo = selection(population)
        # newIndividual = crossover(individualOne, individualTwo)
        

def selection(population):
    return population.getFittest(), population.getSecondFittest()

# def crossover(one, two):


if __name__ == "__main__":
    import sys
    run(sys.argv[1])