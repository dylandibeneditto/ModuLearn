from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.theme import Theme
from rich.text import Text
from rich.align import Align
from utils.get_key import get_key
from utils.theme import main_theme
import time
from os import system, name

from homescreen import homescreen
from study import study

console = Console(theme=main_theme)

over = False

while(not over):

    console.clear()

    homescreen_to = homescreen()

    match homescreen_to:
        case -1:
            over = True
        case 0:
            study_to = study()
            if study_to == -2:
                over = True
        case 1:
            print("wip")
        case 2:
            print("wip")
        case 3:
            print("wip")
        case 4:
            print("wip")