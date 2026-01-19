import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model
        self.durata_min = 0



    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""

        self.durata_min = int(self._view.txt_durata.value)
        try:
            if not self.durata_min:
                self._view.show_alert("Inserire un valore")
                return
        except ValueError:
            self._view.show_alert("Inserisci un valore valido")
            return

        self._view.lista_visualizzazione_1.controls.clear()

        self._model.build_grafo(self.durata_min)

        numero_nodi, numero_archi = self._model.get_number_of_nodes_and_edges()
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f"Grafo creato con {numero_nodi} nodi e {numero_archi} archi"))

        self.get_selected_album(e)
        self._view.update()


    def get_selected_album(self, e):
        """ Handler per gestire la selezione dell'album dal dropdown """""
        # TODO
        lista_nodi = self._model.get_nodes()
        for nodo in lista_nodi:
            self._view.dd_album.options.append(ft.dropdown.Option(text = nodo.title, key = nodo.id))

        self._view.update()


    def handle_analisi_comp(self, e):
        """ Handler per gestire l'analisi della componente connessa """""
        # TODO
        self._view.dd_album.options.clear()
        self._view.lista_visualizzazione_2.controls.clear()
        id_a1 = int(self._view.dd_album.value) #è un id
        a1 = self._model.id_map[id_a1]
        dim_componente, durata = self._model.analisi_componente(a1)
        self._view.lista_visualizzazione_2.controls.append(ft.Text(f"Dimensione componente: {dim_componente}"))
        self._view.lista_visualizzazione_2.controls.append(ft.Text(f"Durata totale: {durata} minuti"))

        self._view.update()



    def handle_get_set_album(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del set di album """""
        # TODO