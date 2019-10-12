from People.Support import Support

"""
    Class representing the single scene.
"""


class Scene(object):
    def __init__(self, public_flag, person):
        self.public = public_flag
        self.person = person
        if isinstance(person, Support):
            self.isSupport = True
        # TODO define Markov Chain supported by actions database with probability Matrix
