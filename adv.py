import types

from game import Game
import rooms as Rooms
from actor import Me

# vocabulary
Verbs = ['go', 'north', 'south', 'east', 'west', 'up', 'down', 'take']
Articles = ['the', 'a' 'an']
Prepositions = ['on', 'in', 'under']


def newline(count=1):
    print('\n' * count)


def header():
    print('{} version {}'.format(Game.TITLE, Game.VERSION))
    print('Written by {}'.format(Game.AUTHOR))
    print('{}'.format(Game.DESCRIPTION))
    newline()


def prompt(promptstr=Game.PROMPT):
    return input(promptstr)


def parse_verb(strverb):
    if strverb not in Verbs:
        print('I dont know how to {}'.format(strverb))
        return None

    # Verbs.index(strverb)
    return strverb


def get_property(obj, prop, args=[]):
    p = getattr(obj, prop, None)
    if p is None:
        return None

    if type(p) == types.FunctionType or type(p) == types.MethodType:
        if len(args) == 0:
            return p()
        elif len(args) == 1:
            return p(args[0])
        elif len(args) == 2:
            return p(args[0], args[1])
        elif len(args) == 3:
            return p(args[0], args[1], args[2])
        else:
            return None
    else:
        return p


def move_into(direction):
    can_travel = get_property(Me, 'verify_travel', [direction])
    if can_travel is None or can_travel == False:
        print('You are unable to move.')
        return

    new_loc = get_property(Me.location, direction)
    if new_loc is None:
        print('You cannot go that way.')
    else:
        Me.travel(new_loc)


def handle_command(text):
    # command syntax
    #
    #  verb
    #  verb <art> <adj>DirectObject
    #  verb <art> <adj>DirectObject <prep> <art> <adj>IObject

    parts = text.split()
    # nothing entered
    if len(parts) == 0:
        return 0

    # system command is q or quit
    if parts[0] == 'q' or parts[0] == 'quit':
        return -99

    # parse out the verb
    verb = parse_verb(parts[0])
    if verb is None:
        return -1

    if verb == 'north' or verb == 'n':
        move_into('north')
    elif verb == 'south' or verb == 's':
        move_into('south')
    elif verb == 'east' or verb == 'e':
        move_into('east')
    elif verb == 'west' or verb == 'w':
        move_into('west')
    else:
        print('I didn\'t understand that.')

    #   debugging
    #   for part in parts:
    #       print(part)
    return 0


def report_location():
    room_name = get_property(Me.location, 'sdesc')
    has_seen = get_property(Me.location, 'has_seen')
    long_desc = get_property(Me.location, 'ldesc')

    print(room_name)
    if not has_seen or Game.verbose:
        print(long_desc)
    newline()


def report_things():
    pass


#
# Start it up
#
header()
newline()

Game.start = Rooms.AtHillInRoad
Game.initialize()

# main game loop
while True:
    report_location()
    report_things()

    command = prompt()
    err = handle_command(command)

    # -99 means quit
    if err == -99:
        break
