import flet as ft
word_selected="messi"
def main(page: ft.Page):

    def word_display():
        words = []
        for i in range(5):
            words.append(
                ft.Container(
                    ft.TextField(color="black",max_length=1,text_size=28, focused_border_width=2, width=50,height=50),
                    width=50,
                    height=50,
                    padding=
                    bgcolor=ft.colors.BLUE_50,
                    border_radius=ft.border_radius.all(5),
                )
            )
        return words
    

    def check_display():
        btn = [ft.FilledButton(text="Check")]
        return btn
    
    page.title = "Wordle Game by DK Games"
    page.add(ft.Row(word_display(), alignment=ft.MainAxisAlignment.CENTER), ft.Row(check_display(), alignment=ft.MainAxisAlignment.END,height=100,width=100))
    
ft.app(main)