import flet as ft

word_selected="messi"
class KeyBoard(ft.UserControl):

    keyboard = "qwertyuiopasdfghjklñzxcvbnm"

    def __init__(self, *args, **kwargs):
        super(KeyBoard, self).__init__(*args, **kwargs)
    
    def build(self):
        
        return ft.Column([
            ft.Row(
                [self.key_word(j) for i, j in enumerate(self.keyboard) if i <= 9],
                alignment="center",
                
            ),
            ft.Row([self.key_delete(), self.key_word("s")])
        ])
    
    def key_word_action(self,ControlEvent):
        print(f"Se presionó la letra {ControlEvent.control}")
        # panel[fila].controls[columna].content.value = ControlEvent
        ft.Page.update

    def key_delete(self):
        key = ft.Container(
            ft.IconButton(
                icon=ft.icons.ARROW_BACK,
                icon_size=25,
                # on_click=self.key_delete_action
            ),
            padding=ft.padding.only(top=10)
        )
        return key
    def key_word(self, letter: str):
        key = ft.Container(
            ft.Text(letter,color="black"),
            on_click=self.key_word_action,
            padding=7,
            margin=0,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.ON_SURFACE_VARIANT
        )

        return key
class WordsPanel(ft.UserControl):
    panel_row = 0
    panel_col = 0
    def __init__(self, *args, **kwargs,):
        super(WordsPanel, self).__init__(*args, **kwargs)

    def build(self):
        return ft.Column(self.made_panel())
    
    def made_panel(self):
        panel = []
        for i in range (6):
            panel.append(self.words_display())
        return panel
    
    def words_display(self):
        words = []
        for i in range(5):
            words.append(
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
            controls=words, 
            alignment=ft.MainAxisAlignment.CENTER,
            )
    

def manage(page:ft.Page):
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
    wp = WordsPanel()
    kb = KeyBoard()
    page.add(
        wp,
        kb
    )
ft.app(manage)