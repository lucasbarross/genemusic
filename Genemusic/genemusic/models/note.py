class Note:
    def __init__(self, note, time):
        self.note = note
        self.time = time

    def setNote(self, note):
        self.note = note

    def setTime(self, time):
        self.time = time
    
    def getNote(self):
        return self.note

    def getTime(self):
        return self.time