from .Music import Music
from .Note import Note
from random import randint
from collections import Counter
import operator

class Population:
    def __init__(self, size):
        print("size", size)
        self.individuals = self.generatePopulation(size)
        self.SCALES = { 
            "CMAJ": ["C", "D", "E", "F", "G", "A", "B"]
        }

    def generateRandomNotes(self):
        possibleNotes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        notes = []

        for i in range(30):
            randomIndex = randint(0, len(possibleNotes)-1)
            randomTime = randint(1, 5)
            notes.append(Note(possibleNotes[randomIndex], randomTime))
        return notes

    def generatePopulation(self, size):
        population = []
        for i in range(size):
            notes = self.generateRandomNotes()
            population.append(Music("CMAJ", notes))
        return population

    def calculateFitness(self): 
        self.individuals = list(map(self.calculateIndividualFitness, self.individuals))

    def calculateIndividualFitness(self, individual):
        fitness = 0
        notes = map(lambda x: x.note, individual.notes)
        count = Counter()
        
        for n in individual.notes:
            if n.note in self.SCALES[individual.scale]:
                count[n.note] += 1

        scaleNotes = len(count)
        
        mostCommonNote = list(dict(count.most_common(1)).keys())[0]
        mostCommonNoteCount = list(dict(count.most_common(1)).values())[0]

        fitness = (1.0/mostCommonNoteCount) * scaleNotes  

        individual.setFitness(fitness)
        return individual

    def getFittest(self):
        
        bestMusic = self.individuals[0]

        for music in self.individuals:
            if music.fitness > bestMusic.fitness:
                bestMusic = music

        return bestMusic
    
    def getSecondFittest(self):
        
        bestMusic = self.individuals[0]
        secondBest = self.individuals[1]

        for music in self.individuals:
            if music.fitness > bestMusic.fitness:
                secondBest = bestMusic
                bestMusic = music
            elif music.fitness > secondBest.fitness:
                secondBest = music

        return secondBest