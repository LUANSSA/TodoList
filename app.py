import flet as ft

# Classe para criar tarefas
class Task(ft.Column):
    def __init__(self, task_name,task_status_change, task_delete):
        super().__init__()
        self.completed=False
        self.task_name=task_name
        self.task_stattus_change=task_status_change
        self.task_delete=task_delete

    def build(self):
        self.display_task=ft.Checkbox(
            value=False,
            label=self.task_name,
            on_change=self.status_change,
        )

        self.edit_name=ft.TextField(expand=1,on_submit=self.save_clicked)

        self.display_view=ft.Row(
            controls=[
                self.display_task,
                ft.Row(
                    controls=[
                        # Editar tarefa
                        ft.IconButton(
                            icon=ft.Icons.CREATE_OUTLINED,
                            icon_color=ft.Colors.GREEN,
                            tooltip="Editar tarefa",
                            on_click=self.edit_clicked,
                        ),
                        # Deletar tarefa
                        ft.IconButton(
                            icon=ft.Icons.DELETE_OUTLINED,
                            icon_color=ft.Colors.RED,
                            tooltip="Deletar tarefa",
                            on_click=self.delete_clicked,
                        )
                    ],
                    alignment="right"
                )
            ]
        )

        self.edit_view=ft.Row(
            visible=False,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.Icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.Colors.GREEN,
                    tooltip="Atualizar tarefa",
                    on_click=self.save_clicked
                )
            ]
        )

        return ft.Column(
            controls=[
                self.display_view, self.edit_view,
            ]
        )


    def save_clicked(self, event):
        self.display_task.label=self.edit_name.value
        self.display_view.visible=True
        self.edit_view.visible=False
        self.update()
        pass
    def edit_clicked(self, event):
        self.edit_name.value=self.display_task.label
        self.display_view.visible=False
        self.edit_view.visible=True
        self.update()
        pass
    def delete_clicked(self, event):
        self.task_delete(self)
        pass
    def status_change(self, event):
        self.completed=self.display_task.value
        self.task_stattus_change(self)
        pass
    pass

# Classe para criar aplicativo
class TodoApp(ft.Column):
    def build(self):
        self.new_task=ft.TextField(
            hint_text="Qual tarefa precisa ser feita?",
            expand=True,
            on_submit=self.add_task
        )

        self.tasks=ft.Column()

        self.filter=ft.Tabs(
            scrollable=False,
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[
                ft.Tab(text="Todas"),
                ft.Tab(text="A Fazer"),
                ft.Tab(text="Concluídas"),
            ]
        )

        self.itens_left=ft.Text("0 tarefas adicionadas")

        self.button_clear = ft.OutlinedButton(
            text="Apagar todas a tarefas concluídas".upper(),
            on_click=self.clear_completed_tasks,
            disabled = True
        )

        return ft.Column(
            controls=[
                # Titulo da Aplicação
                ft.Row(
                    controls=[
                        ft.Text(value="Tarefas", size=40, weight="bold",color=ft.Colors.with_opacity(0.7, "black"))
                    ],
                    alignment="center"
                ),
                # Adicionar tarefa
                ft.Row(
                    controls=[
                        self.new_task,
                        ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=self.add_task)
                    ]
                ),
                # Filtro de tarefas
                ft.Column(
                    controls=[
                        self.filter,
                        self.tasks,
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                self.itens_left,
                                self.button_clear,
                            ]
                        )
                    ]
                )
            ]
        )

    # Navegação de tarefas
    def tabs_changed(self, event):
        self.update()

    # Adiconar tarefa
    def add_task(self, event):
        if self.new_task.value:
            task=Task(self.new_task.value, self.task_status_chage, self.task_delete)
            self.tasks.controls.append(task)
            self.new_task.value=""
            self.new_task.focus()
            self.update()
        pass

    # Apagar tarefas concluídas
    def clear_completed_tasks(self, event):
        for task in self.tasks.controls[:]:
            if task.completed:
                self.task_delete(task)
        pass

    def task_status_chage(self, task):
        self.update()
        pass

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()
        pass

    def before_update(self):
        
        status = self.filter.tabs[self.filter.selected_index].text
        count=0
        task_complete = 0

        for task in self.tasks.controls[:]:

            task.visible = (
                status == "Todas"
                or (status == "A Fazer" and task.completed == False)
                or (status == "Concluídas" and task.completed == True)
            )
            
            if not task.completed:
                count+=1

            print(task_complete)

            if task.completed:
                task_complete += 1
                print(task_complete)
                print(self.tasks.controls)
                print(len(self.tasks.controls))

                if task_complete == len(self.tasks.controls):
                    self.button_clear.disabled = False
                elif task_complete != len(self.tasks.controls):
                    self.button_clear.disabled = False
                else:
                    self.button_clear.disabled = False
            else:
                self.button_clear.disabled = True

        self.itens_left.value=f"{count} tarefa(s) não concluídas"
        
        super().before_update()



def main(page: ft.Page):
    page.title="Minhas Tarefas"
    page.window.width=550
    page.window.height=650
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.padding=ft.padding.only(top=20,bottom=20,left=20,right=20)
    page.theme_mode=ft.ThemeMode.LIGHT
    page.scroll=ft.ScrollMode.ADAPTIVE
    page.update()

    app = TodoApp()

    page.add(app)


ft.app(target=main)