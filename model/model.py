import networkx as nx
from database.dao import DAO


class Model:
    def __init__(self):
        self.dao = DAO()
        self.G = nx.Graph()
        self.nodi = []
        self.archi = []
        self.id_map = {}


    def get_album(self, durata):
        album = self.dao.get_album(durata)
        return album


    def build_grafo(self, durata):
        self.G.clear()

        #nodi
        self.nodi = self.get_album(durata)
        for nodo in self.nodi:
            self.G.add_node(nodo)
            self.id_map[nodo.id] = nodo

        connessioni = self.dao.get_connessioni()
        #archi
        for c in connessioni:
            if c[0] in self.id_map and c[1] in self.id_map:
                a1 = self.id_map[c[0]]
                a2 = self.id_map[c[1]]
                self.G.add_edge(a1, a2)

    def get_nodes(self):
        return list(self.G.nodes())

    def get_number_of_nodes_and_edges(self):
        return self.G.number_of_nodes(), self.G.number_of_edges()

    def analisi_componente(self, a1):
        somma_durata = 0
        vicini = nx.node_connected_component(self.G, a1)
        dimensione = len(vicini)
        for vicino in vicini:
            somma_durata += vicino.durata

        return dimensione, somma_durata
























