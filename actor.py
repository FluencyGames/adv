from base import Actor


class Me(Actor):
    start_things = []

    def __init__(self):
        Actor.inventory = [t for t in Me.start_things]

    @staticmethod
    def travel(locale: object):
        Me.location = locale
