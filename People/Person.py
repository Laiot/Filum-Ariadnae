from abc import ABC


class Person(ABC):
    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_choices(sub_graph):
        choices = []
        for v in sub_graph:
            choices.append(v)
        return choices
