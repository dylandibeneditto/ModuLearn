from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.theme import Theme
from rich.text import Text
from rich.align import Align
from rich.layout import Layout
from utils.get_key import get_key
from utils.theme import main_theme
import random

from rich.console import Console
from rich.layout import Layout

rand_color = str(random.randrange(1,5))

def homescreen_view(selected):
    console = Console(theme=main_theme)

    layout = Layout()
    layout.split_column(
        Layout(Align.center("[bold]\n\n\nModuLearn [a"+rand_color+"]v1.0.0"), size=4),
        Layout(Align.center("[seci]A smarter approach to memorization."), size=3),
        Layout(Align.left("[a1fill] Study " if selected == 0 else " [bold]Study "), size=2),
        Layout(Align.left("[a2fill] Edit " if selected == 1 else " [bold]Edit "), size=2),
        Layout(Align.left("[a3fill] Stats " if selected == 2 else " [bold]Stats "), size=2),
        Layout(Align.left("[a4fill] Settings " if selected == 3 else " [bold]Settings "), size=2),
        Layout(Align.left("[a5fill] Credits " if selected == 4 else " [bold]Credits "), size=4),
        Layout(Align.left("[seci] ↑↓ move | ⮐  select | 'q' quit "), size=1),
    ) 
    
    console.height -= 3
    console.clear()
    console.print(Align.center(Align.center(layout, width=40, height=int(console.height/2)), vertical="middle"))


def homescreen():
    selected = 0
    over = False
    while(not over):
        homescreen_view(selected)
        key = get_key()
        if key=="A":
            selected = (selected - 1) % 5
        elif key=="B":
            selected = (selected + 1) % 5
        elif key=="q" or key=="Q":
            over = True
        elif key=="\r" or key=="\n":
            over = True
            return selected
    return -1