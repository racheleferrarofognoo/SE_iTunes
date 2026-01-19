import networkx as nx
from database.dao import DAO


class Model:
    def __init__(self):
        self.G = nx.Graph()
        self.dao = DAO()
        self.nodi = [] #lista di oggetti
        self.edges = []
        self.id_map = {}


    def build_grafo(self, durata):
        #pulisco
        self.G.clear()


        #creo nodi
        self.lista_album = self.dao.get_album_maggiori_di_durata(durata)

        self.G.add_nodes_from(self.lista_album)

        for nodo in self.nodi:
            self.id_map[nodo.id] = nodo

        #creo archi
        lista_connessioni = self.dao.get_connessioni()
        self.G.add_edges_from(lista_connessioni)

        return self.G

    def get_component(self, album):
        if album not in self.G:
            return []
        return list(nx.node_connected_component(self.G, album))











