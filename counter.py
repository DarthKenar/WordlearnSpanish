import flet as ft
word_selected="messi"
def main(page: ft.Page):

    def made_panel():
        panel = []
        for i in range (6):
            panel.append(words_display())
        return panel

    def top_spacing_display():
        top_spacing = ft.Container(margin=ft.margin.only(top=10))
        return top_spacing

    def words_display():
        words = []
        for i in range(5):
            words.append(
                ft.Container(
                    content=ft.Text(
                        value="X",
                        size=28,
                        width=50,
                        height=50,
                        text_align="CENTER"
                    ),
                    width=50,
                    height=50,
                    border_radius=ft.border_radius.all(5),
                    bgcolor=ft.colors.BLACK38,
                )
            )
        return ft.Row(
            controls=words, 
            alignment=ft.MainAxisAlignment.CENTER,
            )
    def check(e):
        print("Btn check pressed")
        panel[0].controls[2].content.value = "S"
        page.update()

    def check_display():

            
        btn = [
            ft.Container(
                ft.FilledButton(
                    text="CHECK",
                    width=125,
                    height=50,
                    on_click=check
                ),
                padding=ft.padding.only(top=50)             
            )
        ]
        return ft.Row(btn,alignment=ft.MainAxisAlignment.CENTER)
    
    page.title = "Wordle Game by DK Games"

    top_spacing = top_spacing_display()
    panel = made_panel()
    btn_check = check_display()

    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.AMBER,
    )
    page.add(
        top_spacing,
        ft.Column(panel),
        btn_check,
    )
    
ft.app(main)