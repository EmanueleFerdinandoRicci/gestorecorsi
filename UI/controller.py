import flet as ft

from model.model import Model


class Controller:
    def __init__(self, view):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = Model()

    def handlePrintCorsiPD(self,e):
        pass

    def handlePrintIscrittiCorsiPD(self,e):
        pass

    def handlePrintIscrittiCodIns(self,e):
        pass

    def handlePrintCDSCodIns(self,e):
        pass

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
        self._ddCodInsValue = e.control.data
        print(self._ddCodInsValue)