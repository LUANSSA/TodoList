import flet as ft


# Input de tipo texto
def input_texto(pHint_text, pWidth, pIcon=None):
    return ft.TextField(
        hint_text=pHint_text,
        width=pWidth,
        icon=pIcon if pIcon else None
    )
    pass

# Input de tipo numero
def input_numero(pHint_text, pWidth, pIcon=None):
    return ft.TextField(
        hint_text=pHint_text,
        width=pWidth,
        icon=pIcon if pIcon else None,
        keyboard_type=ft.KeyboardType.NUMBER
    )

# Input de tipo senha
def input_senha(pHint_text, pWidth):
    return ft.TextField(
        hint_text=pHint_text,
        width=pWidth,
        password=True,
        can_reveal_password=True
    )

# Caixa de seleção
def checkbox_simples(pLabel):
    return ft.Checkbox(
        label=pLabel
    )

# Dropdow simples
def dropdown_simples(pLabel, pWidth, pOpcoes):
    return ft.Dropdown(
        label=pLabel,
        width=pWidth,
        options=[ft.dropdown.Option(op) for op in pOpcoes]
    )

# Botao simples
def botao_simples(pTexto, pIcon):
    return ft.ElevatedButton(
        pTexto,
        icon=pIcon if pIcon else None
    )
