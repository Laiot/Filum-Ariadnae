from People.Person import Person

"""
    Class representing possible malicious NPCs.
    The list 'actions' will be emptied and refilled through the Markov Chain. //TODO to be changed somehow
"""


class NPC(Person):
    def __init__(self, name, actions):
        super().__init__(name)
        self.actions = actions  # List of actions possible for the NPC to choice randomly.  //TODO

