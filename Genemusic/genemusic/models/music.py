from ..config import NOTES
from random import randint

class Music:
    def __init__(self, notes):
        self.notes = notes
        self.fitness = 0

    def setFitness(self, fitness):
        self.fitness = fitness

    def mutate(self):
        for note in self.notes:
            prob = randint(0, 100)
            if prob <= 10:
                note.setNote(NOTES[randint(0, len(NOTES)-1)])
                note.setTime(randint(1, 5))

    def printNotes(self):
        for note in self.notes:
            print(note.note, end=" ")

    def getInfo(self):
        notesCharacters = []
        for note in self.notes:
            notesCharacters.append({"note": note.getNote(), "time": note.getTime()})
        return notesCharacters