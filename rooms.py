from base import Location


class AtHillInRoad(Location):
    sdesc = 'At Hill In Road'
    ldesc = 'You have walked up a hill, still in the forest. The road slopes back down the other side of the \
hill.  There is a building in the distance.'

    def __init__(self):
        super(AtHillInRoad,self).__init__()

    @staticmethod
    def east():
        return AtEndOfRoad



class InsideBuilding(Location):
    sdesc = 'Inside Building'
    ldesc = 'You are inside a building, a well house for a large spring. On the north side, through an \
open doorway, is a small pantry.'

    @staticmethod
    def west():
        return AtEndOfRoad


class InAValley(Location):
    sdesc = 'In a Valley'
    ldesc =  'You are in a valley in the forest beside a stream tumbling along a rocky bed.'

    @staticmethod
    def north():
        return AtEndOfRoad


class InForest1(Location):
    sdesc = 'In Forest'
    ldesc = 'You are in open forest, with a deep valley to one side. Not far is a large billboard.'

    east = InAValley
    down = InAValley

    @staticmethod
    def north():
        return InForest1

    @staticmethod
    def south():
        return InForest1

    @staticmethod
    def west():
        return InForest1


class AtEndOfRoad(Location):
    sdesc = 'At End of Road'
    ldesc = 'You are standing at the end of a road before a small brick building. Around %you% is a forest. A \
small stream flows out of the building and down a gully.'

    north = InForest1
    east = InsideBuilding
    west = AtHillInRoad
    south = InAValley

    def __init__(self):
        super(AtEndOfRoad, self).__init__()
