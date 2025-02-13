import flet as ft



class CheckBox(ft.Row):

    def __init__(self, text):
        super().__init__()
        self.text_view = ft.Text(text)
        self.text_edit = ft.TextField(text, visible=False)
        # Botão editar
        self.edit_button = ft.IconButton(icon=ft.icons.EDIT, on_click=self.edit)
        # Botão salvar
        self.save_button = ft.IconButton(icon=ft.icons.SAVE, icon_color="green", on_click=self.save, visible=False)
        # Botão excluir
        self.delete_button = ft.IconButton(icon=ft.icons.DELETE,icon_color="red", on_click=self.delete)

        self.controls = [
            ft.Checkbox(),
            self.text_view,
            self.text_edit,
            self.edit_button,
            self.save_button,
            self.delete_button
        ]


    def edit(self, event):
        self.edit_button.visible=False
        self.save_button.visible=True
        self.delete_button.visible=False
        self.text_edit.visible=True
        self.text_view.visible=False
        self.update()
        pass
    def save(self, event):
        self.edit_button.visible=True
        self.save_button.visible=False
        self.delete_button.visible=True
        self.text_edit.visible=False
        self.text_view.visible=True
        self.text_view.value = self.text_edit.value
        self.update()
        pass
    def delete(self, event):
        self.visible=False
        self.update()
        pass
        