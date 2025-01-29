import flet
from flet import(
    Checkbox,
    Column,
    FloatingActionButton,
    IconButton,
    OutlinedButton,
    Page,
    Row,
    Tab,
    Text,
    TextField,
    UserControl,
    Colors,
    Icons
) # Importação dos componentes que vão ser usados na aplicação


def main(page: Page):
    page.title = "Tarefas"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    page.update()
    
    pass


flet.app(target=main)