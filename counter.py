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
                    ft.TextField(
                        text_size=28,
                        max_length=1,
                        focused_border_width=2, 
                        width=50,
                        height=50,
                        filled=True
                        
                    ),
                    width=50,
                    height=75,
                    border_radius=ft.border_radius.all(5),
                )
            )
        return ft.Row(
            words, 
            alignment=ft.MainAxisAlignment.CENTER,
            )
    def check():
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