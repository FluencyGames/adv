from dictionary import Vocabulary


class PyAdvBaseClass(object):
    # this is the base class for all pyAdv classes

    # this is the long description of whatever
    ldesc = None

    # this is the short description of whatever
    sdesc = None


class Location(PyAdvBaseClass):
    is_dark = False
    has_visited = False
    pass


class Verb(PyAdvBaseClass):
    # the name and
    verb = ''

    # these are the valid prepositions to work with this verb
    Preps = []

    def __init__(self, preps=None):
        Vocabulary.Dictionary.add_verb(self.verb, self)
        if preps is not None:
            self.Preps.extend(preps)
            Vocabulary.Dictionary.add_words(preps, 'Preposition', self)

    # this method verifies that we can do the verb with the thing, prep and
    # indirect object
    @staticmethod
    def verify(thing=None, prep=None, io=None) -> bool:
        thing = thing
        prep = prep
        io = io
        return False

    @staticmethod
    def do(thing=None, prep=None, io=None):
        pass


class Thing(PyAdvBaseClass):
    location = None
    weight = 0
    bulk = 0


class Actor(PyAdvBaseClass):
    location = None
    inventory = []

    @staticmethod
    def verify_travel(direction):
        return True

    @staticmethod
    def travel(locale: object):
        print('Actor travel to {}'.format(locale.sdesc))
        Actor.location = locale
