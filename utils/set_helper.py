import json

class SetHelper:
    def __init__(self):
        with open('./data/sets.json') as file:
            self.json_sets = json.load(file)
        
    def get_sets(self):
        return [s for s in self.json_sets["flashcard_sets"]]
    
    
            