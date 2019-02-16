from .Population import Population
from .Music import Music
from random import randint
from .config import NOTES

def run(size):
    population = Population(int(size))
    population.calculateFitness()
    generations = 0
    while population.getFittest().fitness < 197:
        individualOne, individualTwo = selection(population)
        newIndividual = crossover(individualOne, individualTwo)
        
        mutation(newIndividual)

        population.calculateIndividualFitness(newIndividual) 
        
        population.addIndividual(newIndividual)
        
        population.killWeakest()
        
#         # print("Best", population.getFittest().fitness)
        print("Generation:", generations, "Fittest:", population.getFittest().fitness)
        generations += 1
    
    printNotes(population.getFittest().notes)

def selection(population):
    return population.getFittest(), population.getSecondFittest()

def crossover(one, two):
    newNotes = one.notes[slice(0, int(len(one.notes)/2))] + two.notes[slice(int(len(two.notes)/2), int(len(two.notes)))]
    newIndividual = Music(one.scale, newNotes)
    return newIndividual

def mutation(individual):
    for note in individual.notes:
        prob = randint(0, 100)
        if prob <= 10:
           note.note = NOTES[randint(0, len(NOTES)-1)]
           note.time = randint(1, 5)

def printNotes(individual):
        for note in individual:
                print(note.note)

if __name__ == "__main__":
    import sys
    run(sys.argv[1])