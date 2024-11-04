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
from study_select import study_select


def study_set_view(set):
    console = Console(theme=main_theme)
    console.height -= 2
    console.clear()
    console.print(Align.center("[sec]ModuLearn / Set Select / [a1]" + set["set_name"]))

    panel_height = 5 if console.width < 208 else 4

    main_layout = Layout()
    main_layout.split_column(
        Layout(size=console.height - panel_height),
        Layout(name="action_layout", size=panel_height)
    )

    action_layout = Layout()
    action_layout.split_row(
        Layout(Panel("Flashcards\n[seci]Review cards the old fashioned way.", title="[1]")),
        Layout(Panel("Learn\n[seci]Develop an understanding of new terms.", title="[2]")),
        Layout(Panel("Test\n[seci]Quiz your knowledge.", title="[3]")),
        Layout(Panel("Match\n[seci]A fun way to correlate terms.", title="[4]")),
        Layout(Panel("Custom\n[seci]Use a custom algorithm.", title="[5]"))
    )

    main_layout["action_layout"].update(action_layout)

    console.print(main_layout)

def study_set(set):
    over = False
    
    while not over:
        study_set_view(SetHelper().get_sets()[set])
        key = get_key()
        if key == "D":
            return 0
        elif key == "q":
            return -1
        elif key == "1":
            print("flashcard")
        elif key == "2":
            print("learn")
        elif key == "3":
            print("test")
        elif key == "4":
            print("match")
        elif key == "5":
            print("choose custom")

def study():
    over = False
    
    while not over:
        selected = study_select()
        if selected < 0:
            return selected
        else:
            set_res = study_set(selected)    
            if set_res == 0:
                continue
            elif set_res == -1:
                over = True
                return -2
            