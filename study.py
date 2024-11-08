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

def set_graph_view(set, height, width):
    graph = Layout()
    graph.split_column(Layout(Align.center("█ - mastery | ░ - views"), size=1))
    
    list_length = min(set.cards_length, height-2)
    list_str_size = len(str(list_length+1))
    
    list_combination_max = max([set.get_card(i).mastery + set.get_card(i).views for i in range(list_length)])
    
    for i in range(0,list_length):
        card = set.get_card(i-1, 0)
        print(i)
        
        data_label = " "+"0"*(list_str_size-len(str(i)))+str(i)
        
        data_density = (width-3-list_str_size)/list_combination_max
        
        mastery_conv = int(card.mastery*data_density)
        views_conv = int(card.views*data_density)
        
        data = " "+"█"*(mastery_conv)+"░"*(views_conv)
        Console().print(data)
        
        graph.add_split(Layout(Text(data_label + data), size=1))
        
    axisAndLegend = Layout()
    axisAndLegend.split_row(
        Layout(" "*(list_str_size+1)+"0", ratio=1),
        Layout(Align.center(str(list_combination_max//2)), ratio=1),
        Layout(Align.right(str(list_combination_max)+" "), ratio=1)
    )
    
    graph.add_split(axisAndLegend)
    
    return graph

def study_set_view(set, index, flip, all_flip):
    console = Console(theme=main_theme)
    console.height -= 2
    console.clear()
    console.print(Align.center("[sec]ModuLearn / Set Select / [a1]" + set.name))


    if set.cards_length > 0:
        panel_height = 5 if console.width < 208 else 4

        main_layout = Layout()
        main_layout.split_column(
            Layout(name="set_data", size=console.height - panel_height),
            Layout(name="action_layout", size=panel_height)
        )

        set_data = Layout()
        set_data.split_row(
            Layout(name="card_review", ratio=2),
            Layout(name="stats", ratio=1)
        )

        card = set.get_card(index)

        card_review = Layout()
        card_review.split_column(
            Layout(Panel(Align.center("[white]"+(card.definition if flip else card.term), vertical="middle"), title="definition" if flip else "term", title_align="left", style="sec"),size=console.height - panel_height - 2),
            Layout(name="card_review_toolbar", size=2)
        )


        card_review_toolbar = Layout()
        card_review_toolbar.split_row(
            Layout("  [sec]\[w] [/sec][sec]show [white bold]"+("definition" if all_flip else "term")+"[/white bold] first", size=30),
            Layout(Align.center("[sec] < [/sec][a1]" + ("0"*(len(str(set.cards_length))-len(str(index+1)))) + str(index + 1) + "[/a1][white] / [/white][sec]" + str(set.cards_length) + " >\n[sec]\[a]   "+(" "*(2*len(str(set.cards_length))))+"\[d]", vertical="middle"), ratio=1),
            Layout(Align.right("[sec]\[s] [/sec][" + ("bold" if flip else "sec") + "]flip card  "), size=30)
        )

        action_layout = Layout()
        action_layout.split_row(
            Layout(Panel("Flashcards\n[seci]Review cards the old fashioned way.", title="[1]")),
            Layout(Panel("Learn\n[seci]Develop an understanding of new terms.", title="[2]")),
            Layout(Panel("Test\n[seci]Quiz your knowledge.", title="[3]")),
            Layout(Panel("Match\n[seci]A fun way to correlate terms.", title="[4]")),
            Layout(Panel("Custom\n[seci]Use a custom algorithm.", title="[5]"))
        )

        card_review["card_review_toolbar"].update(card_review_toolbar)
        set_data["card_review"].update(card_review)
        set_data["stats"].update(set_graph_view(set, console.height-panel_height, console.width // 3))
        main_layout["set_data"].update(set_data)
        main_layout["action_layout"].update(action_layout)

        console.print(main_layout)
    else:
        console.print(Align.center("\n[white bold]You have no cards in this set. Please go back to the 'edit' section to create new cards for this set.", width=60))

def study_set(set):
    over = False
    
    card_review_index = 0
    card_review_all_flip = False
    card_review_flip = card_review_all_flip
    set_ref = SetHelper().get_set(set) # set is the index
    
    set_ref.get_card(card_review_index).view()
    
    while not over:
        study_set_view(set_ref, card_review_index, card_review_flip, card_review_all_flip)
        key = get_key()
        if key == "D":
            return 0
        elif key == "s":
            card_review_flip = not card_review_flip
        elif key == "d":
            card_review_index = (card_review_index+1) % set_ref.cards_length
            card_review_flip = card_review_all_flip
            set_ref.get_card(card_review_index).view()
        elif key == "a":
            card_review_index = (card_review_index-1) % set_ref.cards_length
            card_review_flip = card_review_all_flip
            set_ref.get_card(card_review_index).view()
        elif key == "w":
            card_review_all_flip = not card_review_all_flip
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
            