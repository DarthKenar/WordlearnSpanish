import flet as ft

word_selected="messi"

class WordApp(ft.UserControl):

    keyboard = "qwertyuiopasdfghjklñzxcvbnm"
    panel_row = 0
    panel_col = 0

    def __init__(self, *args, **kwargs):
        super(WordApp, self).__init__(*args, **kwargs)

    def build(self):
        
        return(ft.Column(controls=[
            self.panel_build(),
            self.enter_build(),
            self.keyboard_build(),
        ]))

    def enter_action(self, ControlEvent):
        print("Btn check pressed")
        self.panel[0].controls[2].content.value
        self.update()

    def enter_build(self):
        btn = [
            ft.Container(
                ft.FilledButton(
                    text="CHECK",
                    width=125,
                    height=50,
                    on_click=self.enter_action
                ),
                padding=ft.padding.only(top=15,bottom=15)
                        
            )
        ]
        return ft.Row(btn,alignment=ft.MainAxisAlignment.CENTER)
    
    def key_word_action(self,ControlEvent):
        print(f"Se presionó la letra {ControlEvent.control.content.value}")
        print(self.panel[0].controls[0].content.value)
        self.panel[0].controls[0].content.value = ControlEvent.control.content.value
        self.page.update()
        
    def key_word(self, letter: str):
        key = ft.Container(
            ft.Text(letter,color="black"),
            on_click=self.key_word_action,
            padding=11,
            margin=0,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.ON_SURFACE_VARIANT,
            border_radius=10
        )
        return key
    
    def keyboard_build(self):

        return ft.Column([
            ft.Row(
                [self.key_word(j) for i, j in enumerate(self.keyboard) if i <= 9],
                alignment="center",
            ),
            ft.Row(
                [self.key_word(j) for i, j in enumerate(self.keyboard) if i > 9 and i < 20],
                alignment="center",
            ),
            ft.Row([
                ft.Container(ft.Row([self.key_word(j) for i, j in enumerate(self.keyboard) if i > 20])),
                ft.Container(self.key_delete())],
                alignment="center",
            ),
        ])
    
    def key_delete_action(self):
        pass
    
    def key_delete(self):
        self.key = ft.Container(
            ft.IconButton(
                icon=ft.icons.ARROW_BACK,
                icon_size=25,
                # on_click=self.key_delete_action
            )
        )
        return self.key
    
    def panel_build(self):
        self.panel = []
        for i in range (6):
            self.panel.append(self.words_display())
        return ft.Column(self.panel)
    
    def words_display(self):
        self.words = []
        for i in range(5):
            self.words.append(
                ft.Container(
                    content=ft.Text(
                        size=28,
                        width=50,
                        height=50,
                        text_align="CENTER",
                    ),
                    width=50,
                    height=50,
                    border_radius=ft.border_radius.all(5),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                )
            )
        return ft.Row(
            controls=self.words, 
            alignment=ft.MainAxisAlignment.CENTER,
            )
    
def main(page: ft.Page):

    def change_view(e):
        if page.navigation_bar.selected_index == 0:
            print("Op 1 NAVBAR")
        elif page.navigation_bar.selected_index == 1:
            print("Op 2 NAVBAR")
        elif page.navigation_bar.selected_index == 2:
            print("Op 3 NAVBAR")
            if page.platform == "windows":
                print("Terminando aplicacion desde pc")
                page.window_close()
            else:
                print("Terminando aplicacion desde celular")
                page.window_destroy()
        else:
            pass
        
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
        on_change=change_view
    )
    page.window_width = 360
    page.window_max_width = 360
    page.window_height = 800
    page.window_max_height = 800
    page.padding = ft.padding.only(top=50)
    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.AMBER,
    )
    wordapp = WordApp()
    page.add(
        wordapp
    )
    
ft.app(main)