import flet as ft


def main(page: ft.Page):
    
    # Título da página
    page.title="Rows"
    # Rolagem vertical da página
    page.scroll=True

    # Primeira Linha
    linha1 = ft.Row(
        # Lista elementos da Row
        controls=[
            # Primeiro elemento
            ft.Text("Bem vindo", size=40),
            # Segundo elemento
            ft.Text("What is Lorem Ipsum? Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."),
            # Terceira linha
            ft.Text("Why do we use it? It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).")
        ],
        # Permite que os itens quebrem para uma nova linha
        wrap=True,
        # Define o espaço entre as "linhas" quando os elementos quebram para uma nova linha (quando wrap=True está ativado
        run_spacing=40
    )

    # Segunda Linha
    linha2 = ft.Row(
        # Lista de elementos da Row
        controls=[
            # Primeiro elemento
            ft.Text("Autor:"),
            # Segundo elemento
            ft.Text("Luan Souza")
        ],
        # Permite que os itens quebrem para uma nova linha
        wrap=True
    )

    # Adiciona Rows a página - o page.add() tem um page.update() dentro dele
    page.add(
        linha1,
        linha2
    )

    # Atualiza a página
    page.update()



ft.app(main)