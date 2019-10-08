"""
    Class representing support NPCs. Needed because they have much less methods to be implemented and totally different
    from ordinary NPCs.
"""


class Support(object):
    def __init__(self, name, actions):
        self.name = name
        self.actions = actions
