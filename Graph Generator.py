"""
    Class supported to create the Markov Chain and retrain information in a faster and cleaner way.
"""


class Graph(object):
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def __get_vertices(self):
        return list(self.__graph_dict.keys())

    def __get_edges(self):
        edges = []
        for v in self.__graph_dict:
            for neigh in self.__graph_dict[v]:
                if {neigh, v} not in edges:
                    edges.append({v, neigh})
        return edges

    def merge_graph(self, graph):
        for v in graph.__get_vertices():
            if v not in self.__graph_dict:
                self.__graph_dict[v] = []

        for edge in graph.__get_edges():
            edge = set(edge)
            (v1, v2) = tuple(edge)
            if v1 in self.__graph_dict:
                self.__graph_dict[v1].append(v2)
            else:
                self.__graph_dict[v1] = [v2]    # Multiple edges
