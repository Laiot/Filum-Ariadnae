"""
    Class representing the main character of the game.
"""


class PC(object):
    def __init__(self):
        self.name = "Arianna"
        self.stress = 0
        self.health = 100
        self.psyche = 100

    @staticmethod
    def get_choices(sub_graph):
        choices = []
        for v in sub_graph:
            choices.append(v)
        return choices
