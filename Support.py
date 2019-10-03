"""
    Class representing support NPCs. Needed because they have much less methods to be implemented and totally different
    from ordinary NPCs.
"""


class Support(object):
    def __init__(self, name):
        self.name = name