from .Music import Music
from .Note import Note
from .config import NOTES
from .config import SCALES
from random import randint
from collections import Counter
from math import floor
import operator

class Population:
    def __init__(self, size):
        self.size = size
        self.individuals = self.generatePopulation(size)

    def generateRandomNotes(self):
        notes = []

        for _ in range(30):
            randomIndex = randint(0, len(NOTES)-1)
            randomTime = randint(1, 5)
            notes.append(Note(NOTES[randomIndex], randomTime))
        return notes

    def generatePopulation(self, size):
        population = []
        for _ in range(size):
            notes = self.generateRandomNotes()
            population.append(Music("CMAJ", notes))
        return population
    
    def calcFitness(self):
        i = 0
        for ind in self.individuals:
            ind.setFitness(self.calcIndFitness(ind))
            i+=1

    def calcIndFitness(self, individual):
        fitness = 0
        count = Counter()
        
        for n in individual.notes:
            if n.note in SCALES[individual.scale]:
                count[n.note] += 1

        scaleNotes = len(count)
        total = sum(count.values())
        fitness = total * scaleNotes
        return fitness

    def getFittest(self):
        
        bestMusicIndex = 0
        
        i = 0
        
        for music in self.individuals:
            
            if music.fitness > self.individuals[bestMusicIndex].fitness:
                bestMusicIndex = i

            i+=1

        # print(bestMusicIndex)
        return self.individuals[bestMusicIndex]

    def breed(self, matingPool):
        newPopulation = []
        # print(len(newPopulation))
        # print(best.fitness)
        for _ in range(self.size):
            indOne, indTwo = self.selection(matingPool)
            child = self.crossover(indOne, indTwo)
            child.mutate()
            # child.setFitness()
            newPopulation.append(child)

        self.individuals = newPopulation
    
    def getMatingPool(self, best):

        matingPool = []
        for individual in self.individuals:
            newFitness = individual.fitness / best.fitness
            for _ in range(floor(newFitness * 10)):
                    matingPool.append(individual)
        
        return matingPool

    def selection(self, matingPool):
            # print(best.fitness)
        indOne = matingPool[randint(0, len(matingPool)-1)]
        indTwo = matingPool[randint(0, len(matingPool)-1)] 

        return indOne, indTwo

    def crossover(self, one, two):
        midpoint = randint(0, len(one.notes))
        newNotes = []
        for i, _ in enumerate(one.notes):
                if i > midpoint:
                    newNotes.append(Note(one.notes[i].note, one.notes[i].time))
                else:
                    newNotes.append(Note(two.notes[i].note, two.notes[i].time))

    #     newNotes = one.notes[slice(0, int(len(one.notes)/2))] + two.notes[slice(int(len(two.notes)/2), int(len(two.notes)))]
        newIndividual = Music(one.scale, newNotes)
        # newIndividual.printNotes()
        return newIndividual