class Verb:
    def __init__(self):
        self.name = ''
        self.synonyms = []
        self.properties = {}    # dictionary of properties for this verb
        self.objects = []       # list of objects we can act on

    def validate(self, directobject=None):
        return True

    def action(self, directobject=None, preposition=None, iobject=None):
        return True


class Location:
    def __init__(self):
        self.name = ''
        self.synonyms = []
        self.directions = {}
        self.properties = {}

    def validate(self, direction):
        return self.directions.get(direction) is not None

    def action(self, direction):
        return self.directions.get(direction)

    def get_valid_directions(self):
        return self.directions.keys()
