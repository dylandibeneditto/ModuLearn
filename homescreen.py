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

    keep_layout = console.height >= 22

    layout = Layout()
    if not keep_layout:
        layout.split_row()
    else:
        layout.split_column()
    layout.add_split(
        Layout(Align.center("[bold]"+("\n\n\n" if keep_layout else "")+"ModuLearn [a"+rand_color+"]v1.0.0"), size=4 if keep_layout else None),
        Layout(Align.center("[seci]A smarter approach to memorization."), size=3 if keep_layout else 0),
        Layout(Align.left("[a1fill] Study " if selected == 0 else " [bold]Study "), size=2 if keep_layout else None),
        Layout(Align.left("[a2fill] Edit " if selected == 1 else " [bold]Edit "), size=2 if keep_layout else None),
        Layout(Align.left("[a3fill] Stats " if selected == 2 else " [bold]Stats "), size=2 if keep_layout else None),
        Layout(Align.left("[a4fill] Settings " if selected == 3 else " [bold]Settings "), size=2 if keep_layout else None),
        Layout(Align.left("[a5fill] Credits " if selected == 4 else " [bold]Credits "), size=3 if keep_layout else None),
        Layout(Align.left("[seci] [white bold]↑↓[/white bold] move | [white bold]⮐ [/white bold][seci]/[white bold]→[/white bold] select | [white bold]←[/white bold] back | [white bold]q[/white bold] quit"), size=1 if keep_layout else None),
    ) 
    
    console.height -= 3
    console.clear()
    console.print(Align.center(Align.center(layout, width=40 if keep_layout else console.width, height=console.height//2 if keep_layout else console.height), vertical="middle"))


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
        elif key=="\r" or key=="\n" or key=="C":
            over = True
            return selected
    return -1