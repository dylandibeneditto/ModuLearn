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

def study():
    selected = study_select()
    if selected < 0:
        return selected
            