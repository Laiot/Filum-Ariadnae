"""
    Class representing the main character of the game.
"""


class PC(object):
    def __init__(self):
        self.name = "Arianna"
        self.stress = 0
        self.phys_viol_lv = 0  # Level of physical violence suffered.
        self.psych_viol_lv = 0  # Level of psychological violence suffered.

    @staticmethod
    def get_choices(sub_graph):
        choices = []
        for v in sub_graph:
            choices.append(v)
        return choices
