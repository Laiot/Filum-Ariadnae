from People.Person import Person

"""
    Class representing support NPCs. Needed because they have much less methods to be implemented and totally different
    from ordinary NPCs.
"""


class Support(Person):
    def __init__(self, name, actions):
        super().__init__(name)
        self.actions = actions
