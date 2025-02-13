# import flet
# from flet import (
#     Checkbox,
#     Column,
#     FloatingActionButton,
#     IconButton,
#     OutlinedButton,
#     Page,
#     Row,
#     Tab,
#     Tabs,
#     Text,
#     TextField,
#     UserControl,
#     colors,
#     icons
# )  # Importação dos componentes que vão ser usados na aplicação


# # Classe de tarefas
# class Tarefas(UserControl):
#     def __init__(self, tarefa_nome, tarefa_estado, tarefa_excluir):
#         super().__init__()
#         self.completa = False
#         self.tarefa_nome = tarefa_nome
#         self.tarefa_estado = tarefa_estado
#         self.tarefa_excluir = tarefa_excluir

#     def build(self):
#         self.tarefa_display = Checkbox(
#             value=False,
#             label=self.tarefa_nome,
#             on_change=self.tarefa_estado
#         )

#         # Entrada de texto para edição de tarefa
#         self.editar_nome = TextField(expand=1)

#         self.display_view = Row(
#             alignment="spaceBetween",
#             vertical_alignment="center",
#             controls=[
#                 self.tarefa_display,
#                 Row(
#                     spacing=0,
#                     controls=[
#                         IconButton(
#                             icon=icons.CREATE_OUTLINED,
#                             tooltip="Editar tarefa",
#                             on_click=self.editar_tarefa,
#                             icon_color=colors.GREEN,
#                         ),
#                         IconButton(
#                             icon=icons.DELETE_OUTLINED,
#                             tooltip="Deletar tarefa",
#                             on_click=self.tarefa_excluir,
#                             icon_color=colors.RED,
#                         ),
#                     ],
#                 ),
#             ],
#         )

#         self.edit_view = Row(
#             visible=False,
#             alignment="spaceBetween",
#             vertical_alignment="center",
#             controls=[
#                 self.editar_nome,
#                 IconButton(
#                     icon=icons.DONE_OUTLINED,
#                     icon_color=colors.GREEN,
#                     tooltip="Atualizar tarefa",
#                     on_click=self.salvar_tarefa,
#                 )
#             ]
#         )

#         return Column(controls=[self.display_view, self.edit_view])

#     # Função editar tarefa
#     def editar_tarefa(self, e):
#         self.editar_nome.value = self.tarefa_display.label
#         self.display_view.visible = False
#         self.edit_view.visible = True
#         self.update()
    
#     # Função salvar tarefa
#     def salvar_tarefa(self, e):
#         self.tarefa_display.label = self.editar_nome.value
#         self.display_view.visible = True
#         self.edit_view.visible = False
#         self.update()
    
#     # Função apagar tarefa
#     def apagar_tarefa(self, e):
#         self.tarefa_excluir()
    
#     # Função alterar status da tarefa
#     def alterar_status_tarefa(self, e):
#         self.completa = self.tarefa_display.value


# class Aplicacao(UserControl):
#     def build(self):
#         self.nova_tarefa = TextField(
#             hint_text="Escreva a tarefa que deseja adicionar",
#             expand=True,
#             on_submit=self.adicionar_tarefa
#         )

#         self.tarefas = Column()

#         self.filtro = Tabs(
#             selected_index=0,
#             tabs=[Tab(text="Todas as tarefas"), Tab(text="Tarefas ativas"), Tab(text="Tarefas completadas")]
#         )

#         return Column(
#             width=600,
#             controls=[
#                 Row([Text(value="Tarefas", style="headlineMedium")], alignment="center"),
#                 Row(
#                     controls=[
#                         self.nova_tarefa,
#                         FloatingActionButton(icon=icons.ADD, on_click=self.adicionar_tarefa)
#                     ]
#                 ),
#                 Column(
#                     spacing=20,
#                     controls=[
#                         self.filtro,
#                         self.tarefas,
#                         Row(
#                             alignment="spaceBetween",
#                             vertical_alignment="center",
#                             controls=[
#                                 Text("0 itens"),
#                                 OutlinedButton(
#                                     text="Limpar as tarefas completadas".upper(),
#                                     on_click=self.limpar_tarefa
#                                 ),
#                             ],
#                         ),
#                     ],
#                 )
#             ],
#         )
    
#     def adicionar_tarefa(self, e):
#         pass
    
#     def limpar_tarefa(self, e):
#         pass


# # Função principal
# def main(page: Page):
#     page.title = "Tarefas"
#     page.horizontal_alignment = "center"
#     page.scroll = "adaptive"
    
#     app = Aplicacao()
#     page.add(app)
#     page.update()


# flet.app(target=main)

import flet as ft
from utils.formulario import (
    input_texto,
    input_numero,
    input_senha,
    checkbox_simples,
    dropdown_simples,
    botao_simples
)

def main(page: ft.Page):

    page.theme_mode = ft.ThemeMode.LIGHT
    page.title="Acervo Digital"

    # INFORMAÇÕES INCIAIS
    # Título
    entrada_titulo=input_texto("Título", 300)
    # Sub título
    entrada_subtitulo=input_texto("Subtítulo", 300)
    # Coleção
    entrada_colecao=input_texto("Coleção", 300)
    # Edição
    entrada_endicao=input_texto("Edição", 300)
    # Local
    entrada_local=input_texto("Local", 300)
    # Editora
    entrada_editora=dropdown_simples("Editora", 300, ["Editora Sextante", "Buzz Editora", "Editora Livre"])
    # Quantidade de páginas
    entrada_quantidade_de_paginas=input_numero("Páginas", 300)
    # Volume
    entrada_volume=input_numero("Volume", 300)
    # Tipologia
    entrada_tipologia=dropdown_simples("Tipologia", 300, ["Livro", "Periódico", "Editora Livre"])

    # IDENTIFICAÇÃO
    # Chamada
    entrada_chamada=input_texto("Chamada", 300)
    # № de tombamento
    entrada_n_tombamento=input_texto("№ de tombamento", 300)
    # Assunto
    entrada_assunto=input_texto("Assunto", 300)
    # Área do acerto
    entrada_area_do_acervo=dropdown_simples("Área do acervo", 300, ["Referência", "Corrente", "Obras Raras", "Coleção 1", "Coleção 2", "Novo"])

    # Botão de enviar
    botao_salvar=botao_simples("Salvar", ft.icons.SAVE)

    # Adicionando na página
    page.scroll="auto"
     # Organizando os campos em linhas (Row)
    linha_1 = ft.Row([entrada_titulo, entrada_subtitulo], spacing=20)
    linha_2 = ft.Row([entrada_colecao, entrada_endicao, entrada_editora], spacing=20)
    linha_3 = ft.Row([entrada_quantidade_de_paginas, entrada_volume, entrada_local], spacing=20)
    linha_4 = ft.Row([entrada_tipologia, entrada_chamada], spacing=20)
    linha_5 = ft.Row([entrada_n_tombamento, entrada_assunto], spacing=20)
    linha_6 = ft.Row([entrada_area_do_acervo], spacing=20)
    
    # Criando um layout responsivo
    conteudo = ft.Column(
        [
            linha_1,
            linha_2,
            linha_3,
            linha_4,
            linha_5,
            linha_6,
            botao_salvar
        ],
        spacing=20,  # Espaçamento entre as linhas
        alignment=ft.MainAxisAlignment.CENTER  # Centraliza os elementos
    )

    # Adiciona um Container para estilizar a página
    page.add(
        ft.Container(
            conteudo,
            padding=20,
            margin=20,
            alignment=ft.alignment.center
        )
    )

ft.app(target=main)