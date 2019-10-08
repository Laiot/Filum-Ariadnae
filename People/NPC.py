"""
    Class representing possible malicious NPCs.
    The list 'actions' will be emptied and refilled through the Markov Chain. //TODO to be changed somehow
"""


class NPC(object):
    def __init__(self, name, actions):
        self.name = name
        self.actions = actions  # List of actions possible for the NPC to choice randomly.  //TODO
        self.phys_viol_lv = 0   # Level of physical violence of the NPC.
        self.psych_viol_lv = 0  # Level of psychological violence of the NPC.
