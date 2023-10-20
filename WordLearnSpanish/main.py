import flet as ft
import random as rdm
words_table = ["pasar","comer","baile","ronca","cazar","manco","tasar","tigre","tieso","casas","palta"]
word_selected = rdm.choice(words_table)

class WordApp(ft.UserControl):

    keyboard = "qwertyuiopasdfghjklñzxcvbnm"
    panel_row = 0
    panel_col = 0

    def panel_help(self):
        print(f"""

        Columna: {self.panel_col}
        Fila: {self.panel_row}

        """)
        
    def __init__(self, *args, **kwargs):
        self.popup_win = ft.AlertDialog(
                        modal=True,
                        title=ft.Text(value="WIN!"),
                        content=ft.Text(value="Thanks for play!"),
                        actions=[
                            ft.TextButton("New Game", on_click=self.close_popup_win),
                        ],
                        actions_alignment=ft.MainAxisAlignment.END,
                        on_dismiss=lambda e: print("Reiniciar Juego"),
                    )
        self.popup_lose = ft.AlertDialog(
                        modal=True,
                        title=ft.Text(value="You are a Loser!"),
                        content=ft.Text(value=f"The word was {word_selected}"),
                        actions=[
                            ft.TextButton(":)", on_click=self.close_popup_lose),
                        ],
                        actions_alignment=ft.MainAxisAlignment.END,
                        on_dismiss=lambda e: print("Reiniciar Juego"),
                    )
        super(WordApp, self).__init__(*args, **kwargs)

    def build(self):
        template = ft.Column(controls=[
            self.panel_build(),
            self.enter_build(),
            self.keyboard_build(),
        ])
        self.select()
        return(template)
    
    def enter_update(self):
        if self.panel_col == 5:
            self.btn[0].content.opacity = 1
        else:
            self.btn[0].content.opacity = 0.5

    def keyboard_update(self, word, color):
        for i, keyboard_row in enumerate(self.keyboard.controls):
            controls = keyboard_row.controls
            if i == 2: #Second row contains a row (whit keys) and a delete key.
                controls = controls[0].content.controls
            for key_container in controls:
                if type(key_container.content) is type(ft.Text()):
                    if key_container.content.value == word:
                        print(key_container.bgcolor)
                        if key_container.bgcolor == ft.colors.ON_SURFACE_VARIANT or key_container.bgcolor == ft.colors.BLACK12:
                            key_container.bgcolor = color
                            key_container.content.color = ft.colors.WHITE
                        elif key_container.bgcolor == ft.colors.ORANGE and color == ft.colors.GREEN:
                            key_container.bgcolor = color
                            key_container.content.color = ft.colors.WHITE
                        else:
                            pass

    def clean_keyboard(self):
        for i, keyboard_row in enumerate(self.keyboard.controls):
            controls = keyboard_row.controls
            if i == 2: #Second row contains a row (whit keys) and a delete key.
                controls = controls[0].content.controls
            for key_container in controls:
                if type(key_container.content) is type(ft.Text()):
                    key_container.bgcolor = ft.colors.ON_SURFACE_VARIANT
                    key_container.content.color = ft.colors.BACKGROUND

    def clean_panel(self):
        print("CLEAN PANEL")
        for i in range(6):
            for j in range(5):
                self.panel_row = i
                self.panel_col = j
                self.deselect()
                self.panel[i].controls[j].content.value = ""
        self.panel_col = 0
        self.panel_row = 0
        self.select()

    def close_popup_win(self, ControlEvent):
        self.popup_win.open = False
        self.clean_panel()
        self.clean_keyboard()
        self.page.update()
        self.update()

    def close_popup_lose(self, ControlEvent):
        self.popup_lose.open = False
        self.clean_panel()
        self.clean_keyboard()
        self.page.update()
        self.update()

    def open_popup_win(self, ControlEvent):
        # popup win
        self.page.dialog = self.popup_win
        self.popup_win.open = True
        self.page.update()

    def open_popup_lose(self, ControlEvent):
        # popup lose
        self.page.dialog = self.popup_lose
        self.popup_lose.open = True
        self.page.update()

    def check_word(self):
        word = ""
        for i in range(5):
            word += self.panel[self.panel_row].controls[i].content.value
        if word == word_selected:
            self.open_popup_win(self)
            print(word,"---",word_selected)
            print("SON IGUALES")
        else:
            if self.panel_row == 5:
                print("POPUP LOSE")
                self.open_popup_lose(self)
            word_selected_copy = word_selected
            for i,j in enumerate(word_selected):
                print(f"{i}-->{j}")
                if word[i] == j:
                    word_selected_copy = word_selected_copy[:i] + "-" + word_selected_copy[i+1:]
                    color = ft.colors.GREEN
                    border_color = ft.border.all(3,color)
                    self.keyboard_update(word[i], color)
                    self.panel[self.panel_row].controls[i].border = border_color
            for i,j in enumerate(word_selected):
                if word[i] != j:
                    if word[i] in word_selected_copy:
                        word_selected_copy = word_selected_copy.replace(word[i],"-",1)
                        color = ft.colors.ORANGE
                        border_color = ft.border.all(3,color)
                        self.keyboard_update(word[i], color)
                        self.panel[self.panel_row].controls[i].border = border_color
                    else:
                        color = ft.colors.BACKGROUND
                        border_color = ft.border.all(3,ft.colors.BLACK)
                        self.keyboard_update(word[i], color)
                        self.panel[self.panel_row].controls[i].border = border_color

    def deselect(self):
        if self.panel_col >= 0 and self.panel_col <= 4:
            self.panel[self.panel_row].controls[self.panel_col].border = ft.border.all(0,)

    def select(self):
        if self.panel_col >= 0 and self.panel_col <= 4:
            if self.panel_row >= 0 and self.panel_row <= 5:
                self.panel[self.panel_row].controls[self.panel_col].border = ft.border.all(0,)
                self.panel[self.panel_row].controls[self.panel_col].border = ft.border.all(2,ft.colors.AMBER_300)

    #! ACTIONS
    def enter_action(self, ControlEvent):
        print("enter_action")
        self.deselect()
        
        if self.panel_col == 5:
            self.check_word()
            self.panel_row += 1
            self.panel_col = 0
            self.select()
            self.enter_update()
            self.update()
        else:
            print("Se debe completar la linea para enviar el check")

        self.panel_help()

    def key_word_action(self, ControlEvent):
        print(f"Se presionó la letra {ControlEvent.control.content.value}")
        if self.panel_col < 5:
            self.panel[self.panel_row].controls[self.panel_col].content.value = ControlEvent.control.content.value
            self.deselect()
            self.panel_col += 1
            self.select()
            self.enter_update()
            self.update()
        self.panel_help()

    def key_delete_action(self, ControlEvent):
        print("key_delete_action")
        if self.panel_col >= 0:
            if self.panel_col != 0:
                self.deselect()
                self.panel_col -= 1
                self.panel[self.panel_row].controls[self.panel_col].content.value = ""
                self.select()
            self.enter_update()
            self.update()
        self.panel_help()

    #! BUILDS
    def enter_build(self):
        self.btn = [
            ft.Container(
                ft.FilledButton(
                    text="ENTER",
                    width=125,
                    height=50,
                    on_click=self.enter_action,
                    opacity=0.5
                    
                ),
                padding=ft.padding.only(top=15,bottom=15)
            )
        ]
        return ft.Row(self.btn,alignment=ft.MainAxisAlignment.CENTER)
        
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

        self.keyboard = ft.Column(controls=[
            ft.Row(
                controls=[self.key_word(j) for i, j in enumerate(self.keyboard) if i <= 9],
                alignment="center",
            ),
            ft.Row(
                controls=[self.key_word(j) for i, j in enumerate(self.keyboard) if i > 9 and i < 20],
                alignment="center",
            ),
            ft.Row(controls=[
                ft.Container(ft.Row([self.key_word(j) for i, j in enumerate(self.keyboard) if i > 20])),
                ft.Container(self.key_delete())],
                alignment="center",
            ),
        ])

        return self.keyboard
    
    def key_delete(self):
        self.key = ft.Container(
            ft.IconButton(
                icon=ft.icons.ARROW_BACK,
                icon_size=25,
                on_click=self.key_delete_action
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
            # ft.NavigationDestination(icon=ft.icons.FEATURED_PLAY_LIST_OUTLINED,
            #                         label="Statistics",
            #                         selected_icon=ft.icons.FEATURED_PLAY_LIST
            #                         ),
            ft.NavigationDestination(icon=ft.icons.PLAY_CIRCLE_OUTLINE,
                                    label="Play",
                                    selected_icon=ft.icons.PLAY_CIRCLE_FILLED_ROUNDED
                                    ),
            ft.NavigationDestination(
                icon=ft.icons.OUTPUT,
                label="Exit",
                
            ),
        ],
        on_change=change_view
    )
    page.window_width = 460
    page.window_max_width = 460
    page.window_height = 800
    page.window_max_height = 800
    page.padding = ft.padding.only(top=50)
    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.AMBER,
    )
    wordapp = WordApp()
    page.add(
        wordapp,
    )
    
    
ft.app(main)