"""
    Class representing possible malicious NPCs.
    The list 'actions' will be emptied and refilled through the Markov Chain. //TODO to be changed somehow
"""


class NPC(object):
    def __init__(self, name, actions):
        self.name = name
        self.actions = actions  # List of actions possible for the NPC to choice randomly.  //TODO

