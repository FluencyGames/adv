from vocab import Verb

class take(Verb):
    def __init__(self, name, synonyms):
        super().__init__()
        self.name = name
        self.synonyms = list(synonyms)

    def validate(self, directObject = None):
        pass

    def action(self, directObject = None, preposition=None, iobject=None):
        pass

