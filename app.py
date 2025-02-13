import flet as ft


# Classe para criar tarefas
class Tarefa(ft.Column):
    def __init__(self, tarefa_nome, tarefa_estado, tarefa_delete):
        super().__init__()
        # Completa
        self.completa=False
        # Nome
        self.tarefa_nome=tarefa_nome
        # Estado da tarefa
        self.tarefa_estado=tarefa_estado
        # Excluir tarefa
        self.tarefa_delete=tarefa_delete

        def build(self):
            self.tarefa_display=ft.Checkbox(
                value=False,
                label=self.tarefa_nome,
                on_change=self.tarefa_estado
            )

        # Editar tarefa
        self.editar_nome=ft.TextField(expand=True, on_submit=self.salvar)

        # View tarefa - Linha da tarefa
        self.tarefa_view=ft.Row(
            controls=[
                # Tarefa checkbox
                self.tarefa_display,
                # Tarefa ações
                ft.Row(
                    controls=[
                        # Botão de editar tarefa
                        ft.IconButton(
                            icon=ft.Icons.CREATE_OUTLINED,
                            icon_color=ft.Colors.GREEN,
                            tooltip="Editar tarefa",
                            on_click=self.editar
                        ),
                        # Botão de excluir tarefa
                        ft.IconButton(
                            icon=ft.Icons.DELETE_OUTLINED,
                            icon_color=ft.Colors.RED,
                            tooltip="Deletar tarefa",
                            on_click=self.deletar
                        )
                    ]
                )
            ]
        )

        self.editar_view = ft.Row(
            visible=False,
            controls=[
                self.editar_nome,
                ft.IconButton(
                    icon=ft.Icons.DONE_OUTLINE_OUTLINED,
                    icon_colors=ft.Colors.GREEN,
                    tooltip="Atualizar tarefa",
                    on_click=self.salvar
                )
            ]
        )

        return ft.Column(
            controls=[
                self.tarefa_view,
                self.editar_view

            ]
        )

    # Salvar tarefa
    def salvar(self, event):
        self.tarefa_display.label = self.editar_nome.value
        self.tarefa_view.visible=False
        self.editar_view.visible=False
        self.update()

    # Editar tarefa
    def editar(self, event):
        self.editar_nome.value = self.tarefa_display.label
        self.editar_nome.focus()
        self.tarefa_view.visible=False
        self.editar_view.visible=True
        self.update()

    # Deletar tarefa
    def deletar(self, event):
        self.tarefa_delete(self)

    # Estado da tarefa
    def tarefa_status(self):
        self.completa = self.mudanca_de_guia.value
        self.tarefa_estado(self)
        self.update()

    
    

# Classe para criar o aplicativo
class TodoApp(ft.Column):

    def build(self):
        self.nova_tarefa = ft.TextField(
            hint_text="Qual tarefa precisa ser feita?",
            expand=True,
            on_submit=self.adicionar_tarefa,
        )


        # Tarefa
        self.tarefas = ft.Column()

        # Filtro de tarefas - Navegação
        self.filtro = ft.Tabs(
            scrollable=False,
            selected_index=0,
            on_change=self.mudanca_de_guia,
            tabs=[
                ft.Tab(text="Todas"),
                ft.Tab(text="Ativas"),
                ft.Tab(text="Concluídas"),
            ]
        )

        self.itens_esquerda = ft.Text("0 tarefas adicionadas")

        # Retorno
        return ft.Column(
            controls=[
                # Título da aplicação
                ft.Row(
                    controls=[
                        ft.Text(value="Tarefas", size=50, weight="bold", color=ft.Colors.with_opacity(0.7, "black"))
                    ],
                    alignment="center",
                ),
                # Inserção de tarefas
                ft.Row(
                    controls=[
                        self.nova_tarefa,
                        ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=self.adicionar_tarefa)
                    ]
                ),
                # Lista de Tarefas
                ft.Column(
                    controls=[
                        # Filtro de tarefas
                        self.filtro,
                        # Lista de tarefas
                        self.tarefas,
                        ft.Row(
                            controls=[
                                # Mensagem de 0 tarefas concluídas
                                self.itens_esquerda,
                                # Botão que apaga tarefas concluídas
                                ft.OutlinedButton(
                                    text="Apagar todas as tarefas concluídas".upper(),
                                    on_click=self.apagar_tarefas_concluidas
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER
                        )
                    ]
                ),
            ]
        )


    # Mudança de guia
    def mudanca_de_guia(self, event):
        self.update()
        pass

    # Adicionar tarefa
    def adicionar_tarefa(self, event):
        if self.nova_tarefa.value:
            tarefa=Tarefa(self.nova_tarefa.value, self.tarefa_estado, self.tarefa_delete)
            self.tarefas.controls.append(tarefa)
            self.nova_tarefa.value=""
            self.nova_tarefa.focus()
            self.update()
        pass

    # Apagar todas as taredas concluídas
    def apagar_tarefas_concluidas(self, event):
        pass

    def tarefa_estado(self, tarefa):
        self.update()

    def tarefa_delete(self, tarefa):
        self.tarefas.controls.remove(tarefa)
        self.update()

# Função principal
def main(page: ft.Page):
    # Titulo
    page.title="Minhas Tarefas"
    # Largunta da tela
    page.window.width=500
    # Altura da tela
    page.window.height=650
    # Tema da página
    page.theme_mode = ft.ThemeMode.LIGHT
    # Alinhamento dos itens na tela
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Atualizar página
    page.update()

    # Todo List
    app = TodoApp()

    page.add(
        app
    )


ft.app(target=main)