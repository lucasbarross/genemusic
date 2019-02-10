from .Music import Music
from .Note import Note
from random import randint

SCALES = { 
  "CMAJ": ["C", "D", "E", "F", "G", "A", "B"]
}

def generateRandomNotes():
    possibleNotes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    notes = []

    for i in range(30):
        randomIndex = randint(0, len(possibleNotes)-1)
        randomTime = randint(1, 5)
        notes.append(Note(possibleNotes[randomIndex], randomTime))

    return notes

def generatePopulation(size):
    population = []
    
    for i in range(size):
        notes = generateRandomNotes()
        population.append(Music("CMAJ", notes))

    return population

def calculatePopulationFitness(individual):
    fitness = 0
    notes = map(lambda x: x.note, individual.notes)
    
    for note in SCALES[individual.scale]:
        if(note in notes):
            fitness+=1

    individual.setFitness(fitness)
    return individual

def run(size):
    population = generatePopulation(int(size))
    population = map(calculatePopulationFitness, population)

    for ind in population:
        print(ind.fitness)

if __name__ == "__main__":
    import sys
    run(sys.argv[1])