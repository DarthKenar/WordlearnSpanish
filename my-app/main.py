import flet as ft
word_selected="messi"
keyboard = "qwertyuiopasdfghjklñzxcvbnm"
def main(page: ft.Page):

    def made_panel():
        panel = []
        for i in range (6):
            panel.append(words_display())
        return panel

    def top_spacing_display():
        top_spacing = ft.Container(margin=ft.margin.only(top=50))
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
                    bgcolor=ft.colors.SURFACE_VARIANT
                )
            )
        return ft.Row(
            controls=words, 
            alignment=ft.MainAxisAlignment.CENTER,
            )
    
    def check(self):
        print("Btn check pressed")
        panel[0].controls[2].content.value = "S"
        page.update()
        print(len(keyboard))

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
    
    def navigation(self):
        print("Nav change page")
        if page.navigation_bar.selected_index == 0:
            print("Op 1 de la barra de navegacion seleccionada")
        elif page.navigation_bar.selected_index == 1:
            print("Op 2 de la barra de navegacion seleccionada")
        elif page.navigation_bar.selected_index == 2:
            print("Op 3 de la barra de navegacion seleccionada")
            if page.platform == "windows":
                print("Terminando aplicacion desde pc")
                page.window_close()
            else:
                print("Terminando aplicacion desde celular")
                page.window_destroy()
        else:
            pass

    def key(letter):
        key = ft.Container(
            ft.TextButton(
                text=letter,
            ),
            expand=True,
            padding=ft.padding.only(top=10)
        )
        return key

    
    page.title = "Wordle Game by DK Games"

    top_spacing = top_spacing_display()
    panel = made_panel()
    btn_check = check_display()

    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.AMBER,
    )

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.FEATURED_PLAY_LIST_OUTLINED,
                                     label="Estadísticas",
                                     selected_icon=ft.icons.FEATURED_PLAY_LIST
                                     ),
            ft.NavigationDestination(icon=ft.icons.PLAY_CIRCLE_OUTLINE,
                                      label="Jugar",
                                      selected_icon=ft.icons.PLAY_CIRCLE_FILLED_ROUNDED
                                      ),
            ft.NavigationDestination(
                icon=ft.icons.OUTPUT,
                label="Salir",
                
            ),
        ],
        on_change=navigation
    )
    page.add(
        top_spacing,
        ft.Column(panel),
        ft.Row(controls=[key("q"),key("w"),key("e"),key("r"),key("t"),key("y"),key("u"),key("i"),key("o"),key("p")]),
        ft.Row(controls=[key("a"),key("s"),key("d"),key("f"),key("g"),key("h"),key("j"),key("k"),key("l")]),
        ft.Row(controls=[key("z"),key("x"),key("c"),key("v"),key("b"),key("n"),key("m")]),
        btn_check
    )

ft.app(main)