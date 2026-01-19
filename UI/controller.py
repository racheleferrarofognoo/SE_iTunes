import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""
        dur = self._view.txt_durata.value
        try:
            durata = int(dur)
        except (ValueError, TypeError):
            self._view.show_alert("Inserisci una durata valida nel campo durata.")
            return

        self._model.build_grafo(durata)

        for album in self._model.lista_album:
            self._view.dd_album.options.append(ft.dropdown.Option(album.title))

        self._view.update()

        self._view.lista_visualizzazione_1.controls.clear()
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f"Grafo creato: {self._model.G.number_of_nodes()} nodi e {self._model.G.number_of_edges()} archi"))


        self._view.update()

    def get_selected_album(self, e):
        """ Handler per gestire la selezione dell'album dal dropdown """""
        # TODO
        #
        title = e.control.value
        self._selected_album = next((a for a in self._model.nodi if a.title == title), None)


    def handle_analisi_comp(self, e):
        """ Handler per gestire l'analisi della componente connessa """""
        # TODO
        if not self._selected_album:
            self._view.show_alert("Selezionare un album")
            return

        componente=self._model.get_component(self._selected_album)
        total_duration=sum(a.duration for a in componente)
        self._view.lista_visualizzazione_2.controls.clear()
        self._view.lista_visualizzazione_2.controls.append(ft.Text(f"Dimensione componente: {len(componente)}"))
        self._view.lista_visualizzazione_2.controls.append(ft.Text(f"Durata totale: {total_duration:.2f} minuti"))
        self._view.page.update()

    def handle_get_set_album(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del set di album """""
        # TODO