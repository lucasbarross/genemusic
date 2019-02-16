from .Music import Music
from .Note import Note
from .config import SCALES
from .config import NOTES
from random import randint
from collections import Counter
import operator

class Population:
    def __init__(self, size):
        print("size", size)
        self.individuals = self.generatePopulation(size)

    def generateRandomNotes(self):
        notes = []

        for i in range(30):
            randomIndex = randint(0, len(NOTES)-1)
            randomTime = randint(1, 5)
            notes.append(Note(NOTES[randomIndex], randomTime))
        return notes

    def generatePopulation(self, size):
        population = []
        for i in range(size):
            notes = self.generateRandomNotes()
            population.append(Music("CMAJ", notes))
        return population

    def calculateFitness(self): 
        for individual in self.individuals:
            self.calculateIndividualFitness(individual)

    def calculateIndividualFitness(self, individual):
        fitness = 0
        count = Counter()
        
        for n in individual.notes:
            if n.note in SCALES[individual.scale]:
                count[n.note] += 1

        scaleNotes = len(count)
        
        mostCommonNote = list(dict(count.most_common(1)).keys())[0]
        mostCommonNoteCount = list(dict(count.most_common(1)).values())[0]
        total = sum(count.values())
        # print("SCN", scaleNotes)
        # fitness = (2.0/mostCommonNoteCount) * scaleNotes  
        # print("total", total)
        fitness = total * scaleNotes  
        # print("FIT", fitness)

        individual.setFitness(fitness)
        # print(fitness)

    def getFittest(self):
        
        bestMusicIndex = 0
        i = 0
        
        for music in self.individuals:
            # print("A", self.individuals[bestMusicIndex].fitness, "B", music.fitness)
            if music.fitness > self.individuals[bestMusicIndex].fitness:
                bestMusicIndex = i
            i+=1
        # print(bestMusicIndex)
        return self.individuals[bestMusicIndex]
    
    def getSecondFittest(self):
        
        bestMusicIndex = 0
        secondBestIndex = 1
        i = 0
        for music in self.individuals:
            
            if music.fitness > self.individuals[bestMusicIndex].fitness:
                secondBestIndex = bestMusicIndex
                bestMusicIndex = i
            elif music.fitness > self.individuals[secondBestIndex].fitness:
                secondBestIndex = i

            i+=1

        return self.individuals[secondBestIndex]

    def killWeakest(self):
        worstMusicIndex = 0
        i = 0
        for i in range(len(self.individuals)):
            # print("Music", self.individuals[i].fitness, "Worst", self.individuals[worstMusicIndex].fitness)
            if self.individuals[i].fitness < self.individuals[worstMusicIndex].fitness:
                worstMusicIndex = i
            
            i+=1
        # print("killed", worstMusicIndex)
        # print("Weak", self.individuals[worstMusicIndex].fitness)
        del self.individuals[worstMusicIndex]
        # print("size", len(self.individuals))
        
    def addIndividual(self, individual):
        self.individuals.append(individual)

    def setIndividuals(self, individuals):
        self.individuals = individuals