

class Game:
    TITLE = "pyAdventure Engine"
    DESCRIPTION = "THis is a test of the python adventure game system"
    AUTHOR = "M. Esterman"
    VERSION = "1.0"
    PROMPT = 'Tell me what to do>'
    score = 0

    def startup(self):
        # handle all startup function here
        pass

    @staticmethod
    def add_score(amount: int):
        Game.score += amount
        print('Your score just went up {} points'.format(amount))

    # def report_score(self):




