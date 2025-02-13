import flet as ft
from custom_checkbox import CheckBox


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title="Acervo Digital"
    page.window.width=450
    page.window.height=650
    page.padding = ft.padding.only(top=20, left=20, right=20, bottom=20)
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    WIDTH: int = page.width
    HEIGHT: int = page.height

    print(WIDTH)
    print(HEIGHT)

    def adicionar_tarefa(e):
        print(nova_tarefa.value)

        if nova_tarefa.value != "":
            lista_de_tarefas.controls.append(CheckBox(nova_tarefa.value))

        nova_tarefa.value=""
        page.update()
        nova_tarefa.focus()

    nova_tarefa = ft.TextField(hint_text="Escreva a tarefa", expand=True, on_submit=adicionar_tarefa)
    novo_botao= ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=adicionar_tarefa)
    
    # Coluna - Lista de tarefas
    lista_de_tarefas = ft.Column(height=HEIGHT-170, scroll=ft.ScrollMode.ADAPTIVE)

    card = ft.Column(
        width=450,
        controls=[
            ft.Row(
                controls=[
                    nova_tarefa,
                    novo_botao
                ]
            ),
            lista_de_tarefas
        ]
    )

    page.add(
        card
    )


ft.app(target=main)