from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.theme import Theme
from rich.align import Align
from rich.layout import Layout
from rich.text import Text

from utils.get_key import get_key
from utils.set_helper import SetHelper
from utils.theme import main_theme

def study_select_view(sets, selected, page, items_per_page):
    console = Console(theme=main_theme)
    layout = Layout()
    layout.split_column()
    console.height -= 3
    
    start_index = page * items_per_page
    end_index = min(start_index + items_per_page, len(sets))

    console.print(Align.center("[sec]ModuLearn / [a1]Set Select"))
    if len(sets) > 0:
        for i in range(start_index, end_index):
            s = sets[i]
            set_name = f"[a1fill] {s['set_name']} " if selected == i else f" {s['set_name']} "
            description = f"[seci]  {s['description']}"

            item_layout = Layout(size=3)
            item_layout.split_column(
                Layout(set_name, size=1),
                Layout(description, size=2)
            )
            layout.add_split(item_layout)
        
        console.print(Align.center(Align.left(layout), width=int(console.width * (2 / 3))))

        page_info = f"[a1]{page + 1} [sec]of [a1]{((len(sets) - 1) // items_per_page) + 1}"
        console.print(Align.center(page_info, vertical="bottom"))

        return 0
    else:
        console.print(Align.center("\n[seci]You have no sets. Please go back and go to 'edit' to create a new set.", width=60))
        return -1

def study_select():
    helper = SetHelper()
    sets = helper.get_sets()
    console = Console()
    
    over = False
    selected = 0
    page = 0

    while not over:
        console.clear()
        items_per_page = ((console.height-3) // 3)
        study_select_res = study_select_view(sets, selected, page, items_per_page)
        key = get_key()
        print(key)
        if key == "D":
            return -1
        elif key == "q":
            return -2
        if study_select_res != -1:
            if key == "A":
                if selected > 0:
                    selected -= 1
                else:
                    selected = len(sets) - 1
                page = selected // items_per_page
            elif key == "B":
                if selected < len(sets) - 1:
                    selected += 1
                else:
                    selected = 0
                page = selected // items_per_page
            elif key == "\n" or key == "\r" or key == "C":
                return selected