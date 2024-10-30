from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.theme import Theme
from rich.text import Text
from rich.align import Align
from rich.layout import Layout
from utils.getKey import getKey

from rich.console import Console
from rich.layout import Layout

def homescreen_view(selected):
    console = Console()

    layout = Layout()
    layout.split_column(
        Layout(Align.center("[bold]ModuLearn 1.0.0"), size=1),
        Layout(Align.center("[rgb(120,120,120) italic]A smarter approach to memorization."), size=3),
        Layout(Align.left("[#000000 on #ffffff] Study " if selected == 0 else " [bold]Study "), size=2),
        Layout(Align.left("[#000000 on #ffffff] Edit " if selected == 1 else " [bold]Edit "), size=2),
        Layout(Align.left("[#000000 on #ffffff] Settings " if selected == 2 else " [bold]Settings "), size=2),
        Layout(Align.left("[#000000 on #ffffff] Credits " if selected == 3 else " [bold]Credits "), size=4),
        Layout(Align.left("[rgb(120,120,120) italic] ↑↓ move | ⮐  select | 'q' quit "), size=1),
    )
    
    console.height -= 3
    console.clear()
    console.print(Align.center(Align.center(layout, width=40, height=int(console.height/2)), vertical="middle"))


def homescreen():
    selected = 0
    over = False
    while(not over):
        homescreen_view(selected)
        key = getKey()
        if key=="A":
            selected = (selected - 1) % 4
        elif key=="B":
            selected = (selected + 1) % 4
        elif key=="q":
            over = True
        elif key=="\r" or key=="\n":
            over = True
            return selected
    return -1