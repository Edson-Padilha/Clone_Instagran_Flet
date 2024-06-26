import flet as ft

def main(page: ft.Page):
    # Definindo cor de fundo
    page.bgcolor = ft.colors.WHITE

    header = ft.Container(
        content=ft.ResponsiveRow(
            controls=[
                ft.Container(
                    padding=40,
                    content=ft.Image(src='images/Logo.png'),
                    bgcolor=ft.colors.BLACK,
                    shape=ft.BoxShape.CIRCLE,
                    height=200,
                )
            ]
        )
    )

    layout = ft.Container(
        width=900,
        content=ft.Column(
            controls=[
                header,
            ]
        )
    )
    page.add(layout)

if __name__=='main':
    ft.app(target=main, assets_dir='assets')