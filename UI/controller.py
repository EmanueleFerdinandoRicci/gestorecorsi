import flet as ft

from model.model import Model


class Controller:
    def __init__(self, view):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = Model()
        self._ddCodinsValue = None

    def handlePrintCorsiPD(self,e):
        self._view.txt_result.controls.clear()

        pd = self._view._ddPD.value

        if pd is None:
            self._view.create_alert("Attenzione, selezionare un periodo didattico.")
            self._view.update_page()
            return
        if pd == "I":
            pdInt= 1
        else: pdInt = 2

        corsiPD = self._model.getCorsiPD(pdInt)

        if len(corsiPD) == 0:
            self._view.txt_result.controls.append(
                ft.Text(f"Nessun corso trovato per il {pd} periodo didattico")
            )
            self._view.update_page()
            return
        self._view.txt_result.controls.append(
            ft.Text(f"Di seguito i corsi trovati per il {pd} periodo didattico")
        )
        for c in corsiPD:
            self._view.txt_result.controls.append(
                ft.Text(c)
            )
        self._view.update_page()

    def handlePrintIscrittiCorsiPD(self,e):
        self._view.txt_result.controls.clear()

        pd = self._view._ddPD.value

        if pd is None:
            self._view.create_alert("Attenzione, selezionare un periodo didattico.")
            self._view.update_page()
            return
        if pd == "I":
            pdInt = 1
        else:
            pdInt = 2

        corsi = self._model.getCorsiPDwIscritti(pdInt)

        if len(corsi) == 0:
            self._view.txt_result.controls.append(
                ft.Text(f"Nessun corso trovato per il {pd} periodo didattico")
            )
            self._view.update_page()
            return
        self._view.txt_result.controls.append(
            ft.Text(f"Di seguito i corsi trovati per il {pd} periodo didattico con dettaglio iscritti:")
        )
        for c in corsi:
            self._view.txt_result.controls.append(
                ft.Text(f"{c[0]} -- N Iscritti: {c[1]}")
            )
        self._view.update_page()

    def handlePrintIscrittiCodIns(self,e):
        self._view.txt_result.controls.clear()

        if self._ddCodinsValue is None:
            self._view.create_alert("Per favore scegliere un corso.")
            self._view.update_page()
            return

        #se arriviamo qui, posso recuperare gli studenti
        studenti = self._model.getStudentiCorso(self._ddCodinsValue.codins)

        if len(studenti) == 0:
            self._view.txt_result.controls.append(
                ft.Text(f"Nessun studente trovato per il corso {self._ddCodinsValue}")
            )
            self._view.update_page()
            return
        self._view.txt_result.controls.append(
            ft.Text(f"Di seguito gli studenti iscritti al corso {self._ddCodinsValue}:")
        )
        for s in studenti:
            self._view.txt_result.controls.append(
                ft.Text(s)
            )
        self._view.update_page()

    def handlePrintCDSCodIns(self,e):
        self._view.txt_result.controls.clear()

        if self._ddCodinsValue is None:
            self._view.create_alert("Per favore scegliere un corso.")
            self._view.update_page()
            return

        cds = self._model.getCDSofCorso(self._ddCodinsValue.codins)

        if len(cds) == 0: #oppure if not len(cds)
            self._view.txt_result.controls.append(
                ft.Text(f"Nessun CDS afferente al corso {self._ddCodinsValue}")
            )
            self._view.update_page()
            return
        self._view.txt_result.controls.append(
            ft.Text(f"Di seguito i CDS che hanno il corso {self._ddCodinsValue}:")
        )
        for c in cds:
            self._view.txt_result.controls.append(
                ft.Text(f"{c[0]} -- N Iscritti: {c[1]}")
            )
        self._view.update_page()

    def fillddCodIns(self):
        #for cod in self._model.getCodIns():
        #    self._view.ddCodIns.options.append(
        #        ft.dropdown.Option(cod)
        #    )

        for c in self._model.getAllCorsi():
            self._view._ddCodIns.options.append(
                ft.dropdown.Option(
                    key=c.codins,
                    data=c,
                    on_click=self._choiceDDCodIns
                )
            )

    def _choiceDDCodIns(self,e):
        self._ddCodinsValue = e.control.data
        print(self._ddCodinsValue)