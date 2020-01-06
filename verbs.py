from base import Verb


class Take(Verb):
    verb = 'take, ta'

    def __init__(self):
        super(Take, self).__init__()


class Drop(Verb):
    verb = 'Drop, dr'

    def __init__(self):
        super(Drop, self).__init__()
