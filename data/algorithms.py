

"""
CREATING AN ALGORITHM:

requirements:
    - has the `self.name` attribute
    - ends when `q` is pressed

After creating a new algorithm, add its class name in the algorithms array

(for more see the github page)

--- example code ---

algorithms = [
    MyNewAlgorithm
]

class MyNewAlgorithm:
    def __init__(self, cards):
        # your code

"""
algorithms = [
    
]

# DO NOT DELETE
class FlashcardsAlgorithm:
    """
    purpose of this algorithm:
        - go through the cards in order
        - can mark a card as known or not known after flipping
        - allowing for looping through the set as many times as the user wants
        - recap after finishing the set each time if user enables card marking
    
    prompt user before start:
        shuffle cards? (boolean)
        card marking? (boolean)
    
    keymap:
        ("A" = up arrow | "B" = down arrow | "C" = right arrow | "D" = left arrow)
        "C" - move to next card
        "D" - go back a card
        "f" - flip the card
        "s" - mark as not known (only when flipped & marking = true)
        "d" - mark as known (only when flipped & marking = true)
        "q" - quit (MANDATORY)
    """
    def __init__(self, cards):
        self.cards = cards # mandatory
        self.name = "Flashcards" # mandatory


# DO NOT DELETE
class LearnAlgorithm:
    def __init__(self, cards):
        self.cards = cards # mandatory
        self.name = "Learn" # mandatory


# DO NOT DELETE
class TestAlgorithm:
    def __init__(self, cards):
        self.cards = cards # mandatory
        self.name = "Flashcards" # mandatory
        
        
# DO NOT DELETE
class MatchAlgorithm:
    def __init__(self, cards):
        self.cards = cards # mandatory
        self.name = "Flashcards" # mandatory