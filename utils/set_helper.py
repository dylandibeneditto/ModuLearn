from datetime import date
import json

def save_json(data):
    with open("./data/sets.json", "w") as f:
        json.dump(data, f, indent=4)

class Card:
    def __init__(self, json, set_index, card_index):
        self.__json = json
        self.__set_index = set_index
        self.__card_index = card_index
        self.__set_json = self.__json["flashcard_sets"][set_index]
        self.__cards = self.__set_json["cards"]
        self.__card = self.__cards[card_index]
        self.term = self.__card["question"]
        self.definition = self.__card["answer"]
        self.views = self.__card["view_count"]
        self.mastery = self.__card["mastery_count"]

    def earn_mastery(self, increment=1):
        self.__json["flashcard_sets"][self.__set_index]["cards"][self.__card_index]["mastery_count"] += increment
        save_json(self.__json)
        
    def view(self, increment=1):
        self.__json["flashcard_sets"][self.__set_index]["cards"][self.__card_index]["view_count"] += increment
        self.__json["flashcard_sets"][self.__set_index]["cards"][self.__card_index]["last_viewed"] = str(date.today())
        save_json(self.__json)

class Set:
    def __init__(self, json, index):
        self.__json = json
        self.__index = index
        self.__set_json = self.__json["flashcard_sets"][index]
        self.name = self.__set_json["set_name"]
        self.description = self.__set_json["description"]
        self.__cards = self.__set_json["cards"]
        self.cards_length = len(self.__cards)
    
    def get_card(self, index, view_increment=1):
        return Card(self.__json, self.__index, index)
    

class SetHelper:
    def __init__(self):
        with open('./data/sets.json') as file:
            self.__json_sets = json.load(file)
        
    def get_sets(self):
        return [s for s in self.__json_sets["flashcard_sets"]]
    
    def get_set(self, index):
        return Set(self.__json_sets, index)
    
    
            