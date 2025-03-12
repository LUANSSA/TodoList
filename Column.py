import flet as ft

def main(page: ft.Page):

    # Título da página
    page.title="Columns"


    # Primeira Coluna
    coluna1 = ft.Column(
        # Lista de elementos dentro da coluna
        controls=[
            # Primeiro elemento da coluna
            ft.Text("Bem Vindos", size=40),
            # Segundo elemento da coluna
            ft.Text("What is Lorem Ipsum?\nLorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."),
            # Terceiro elemento da coluna
            ft.Text("What is Lorem Ipsum?\nLorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."),
            # Quarto elemento da coluna
            ft.Text("What is Lorem Ipsum?\nLorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."),
        ],
        # Define o espaço vertical entre os elementos da coluna
        spacing=40
    )

    # Segunda coluna
    coluna2 = ft.Column(
        # Lista de elementos dentro da coluna
        controls=[
            # Primeiro elemento da coluna
            ft.Row(
                # Lista de elementos da linha
                controls=[
                    # Primeiro elemento
                    ft.Text("Autor:"),
                    # Segundo elemento
                    ft.Text("Luan Souza")
                ]
            ),
            # Segundo elemento da coluna
            ft.Text("copyright Luan Souza"),
        ],
        # Define o espaço vertical entre os elementos da coluna
        spacing=60
    )

    # Adiciona Column a página - o page.add() tem um page.update() dentro dele
    page.add(
        coluna1,
        coluna2
    )


ft.app(main)