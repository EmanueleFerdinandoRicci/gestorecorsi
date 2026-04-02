import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Gestore Corsi - Edizione 2026"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None

        self._ddPD = None
        self._ddCodIns = None
        self._btnPrintCorsiPD = None
        self._btnPrintIscrittiCorsiPD = None
        self._btnPrintIscrittiCodIns = None
        self._btnPrintCDSCodIns = None

    def load_interface(self):
        # title
        self._title = ft.Text("Gestore Corsi - Edizione 2026", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW1
        self._ddPD = ft.Dropdown(label="Periodo Didattico",
                                 options=[ft.dropdown.Option("I"),ft.dropdown.Option("II")],
                                 width=200)
        self._btnPrintCorsiPD = ft.ElevatedButton(text="Stampa Corsi",
                                                  on_click=self._controller.handlePrintCorsiPD,
                                                  width=300)
        self._btnPrintIscrittiCorsiPD = ft.ElevatedButton(text="Stampa Numero Iscritti",
                                                  on_click=self._controller.handlePrintIscrittiCorsiPD,
                                                          width=300)
        row1 = ft.Row([self._ddPD,self._btnPrintCorsiPD,self._btnPrintIscrittiCorsiPD], alignment=ft.MainAxisAlignment.CENTER)

        #ROW2
        self._ddCodIns = ft.Dropdown(label="Corso",
                                     width=200)
        self._controller.fillddCodIns()
        self._btnPrintIscrittiCodIns = ft.ElevatedButton(text="Stampa Iscritti Al Corso",
                                                         on_click=self._controller.handlePrintIscrittiCodIns,
                                                         width=300)
        self._btnPrintCDSCodIns = ft.ElevatedButton(text="Stampa Corsi Di Studio Afferenti",
                                                    on_click=self._controller.handlePrintCDSCodIns,
                                                    width=300)
        row2 = ft.Row([self._ddCodIns, self._btnPrintIscrittiCodIns, self._btnPrintCDSCodIns],alignment=ft.MainAxisAlignment.CENTER)

        self._page.add(row1,row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.add(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
