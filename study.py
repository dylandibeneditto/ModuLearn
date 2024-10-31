from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.theme import Theme
from rich.align import Align
from rich.layout import Layout
from rich.text import Text

from utils.get_key import getKey
from utils.set_helper import SetHelper
from utils.theme import main_theme

console = Console(theme=main_theme)
console.height -=1

def study_select_view(sets, selected):
    layout = Layout()
    layout.split_column()
    
    if len(sets) > 0:
        for i, s in enumerate(sets):
            set_name = f"[a1fill] {s['set_name']} " if selected == i else f" {s['set_name']} "
            description = f"[seci]  {s['description']}"
            
            item_layout = Layout(size=4)
            item_layout.split_column(
                Layout(set_name, size=1),
                Layout(description, size=3)
            )
            layout.add_split(item_layout)
            
        console.print(Align.center(Align.left(layout), width=int(console.width*(2/3))))
        return 0
    else:
        console.print(Align.center("[seci]You have no sets. Press 'q' to quit and go to 'edit' to create a new set."))
        return -1

def study():
    helper = SetHelper()
    sets = helper.get_sets()
    
    over = False
    selected = 0
    
    while not over:
        console.clear()
        study_select_res = study_select_view(sets, selected)
        key = getKey()
        if key == "q":
            return 0
        elif key == "Q":
            return -1
        if study_select_res != -1:
            if key == "A":
                selected = (selected - 1) % len(sets)
            elif key == "B":
                selected = (selected + 1) % len(sets)