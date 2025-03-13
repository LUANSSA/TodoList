# import flet as ft

# def main(page: ft.Page):
#     page.title = "Flet counter example"
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER

#     txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

#     def minus_click(e):
#         txt_number.value = str(int(txt_number.value) - 1)
#         page.update()

#     def plus_click(e):
#         txt_number.value = str(int(txt_number.value) + 1)
#         page.update()

#     page.add(
#         ft.Row(
#             [
#                 ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
#                 txt_number,
#                 ft.IconButton(ft.Icons.ADD, on_click=plus_click),
#             ],
#             alignment=ft.MainAxisAlignment.CENTER,
#         )
#     )

# ft.app(main)


import flet as ft

def main(page: ft.Page):
    page.title="Números"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    numero = ft.TextField(value=0, text_align="right", width=100)

    def diminuir_numero(e):
        numero.value = str(int(numero.value)-1)
        page.update()

    def aumentar_numero(e):
        numero.value = str(int(numero.value)+1)
        page.update()
    
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.Icons.REMOVE, on_click=diminuir_numero),
                numero,
                ft.IconButton(ft.Icons.ADD, on_click=aumentar_numero)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


    pass

ft.app(main)