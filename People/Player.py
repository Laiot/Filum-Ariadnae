from People.Person import Person


"""
    Class representing the main character of the game.
"""


class PC(Person):
    def __init__(self, name="Arianna"):
        super().__init__(name)
        self.stress = 0
        self.phys_viol_lv = 0  # Level of physical violence suffered.
        self.psych_viol_lv = 0  # Level of psychological violence suffered.
