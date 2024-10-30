from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.theme import Theme
from rich.text import Text
from rich.align import Align
from utils.getKey import getKey
import time
from os import system, name

from homescreen import homescreen

console = Console()

flipped = False
over = True

console.clear()

print(homescreen())

def print_flashcard(text, term):
    print(Align.center(Panel(Align.center(Text(text, justify="center"), vertical="middle"), title=term, height=(int(console.height*(3/8))), width=(int(console.width*(2/3))), title_align="left"), vertical="middle", height=(int(console.height/2))))

while(not over):
    console.rule("Flashcards")
    if not flipped:
        print_flashcard("What is the powerhouse of the cell?", "term")
    else:
        print_flashcard("Mitochondria", "definition")
    
    key = getKey()
    
    if key=="f":
        flipped = not flipped
    elif key=="q":
        over = True
    console.clear()
        
