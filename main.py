import flet as ft

def main(page: ft.Page):
    # Definindo cor de fundo
    page.bgcolor = ft.colors.WHITE

    header = ft.Container(
        content=ft.ResponsiveRow(
            controls=[
                ft.Container(
                    padding=40,
                    content=ft.Image(src='images/logo.png'),
                    bgcolor=ft.colors.BLACK,
                    shape=ft.BoxShape.CIRCLE,
                    height=200,
                ),
                ft.Container(
                    content=ft.ResponsiveRow(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Text(
                                        value='hackingetico',
                                        color=ft.colors.BLACK,
                                        size=24,
                                    ),
                                    ft.icons(
                                        name=ft.icons.VERIFIED,
                                    )
                                ]
                            )
                        ]
                    )
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
    ft.app(target=main, port=8000, assets_dir='assets')