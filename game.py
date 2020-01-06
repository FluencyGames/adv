from actor import Me

class Game:
    TITLE = "pyAdventure Engine"
    DESCRIPTION = "THis is a test of the python adventure game system"
    AUTHOR = "M. Esterman"
    VERSION = "1.0"
    PROMPT = 'Tell me what to do>'
    score = 0

    # starting location
    start = None
    verbose = False

    @staticmethod
    def initialize():
        # handle all startup function here
        Me.location = Game.start
        pass

    @staticmethod
    def add_score(amount: int):
        Game.score += amount
        print('Your score just went up {} points'.format(amount))

    # def report_score(self):




