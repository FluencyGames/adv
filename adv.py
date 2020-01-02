import types

from game import Game

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

    return Verbs.index(strverb)


def get_property(obj, prop):
    p = getattr(obj, prop, None)
    if p is None:
        return None

    if type(p) == types.MethodType:
        return p()
    else:
        return p


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
    newverb = parse_verb(parts[0])
    if newverb is None:
        return -1

    #   debugging
    #   for part in parts:
    #       print(part)
    return 0


#
# Start it up
#
header()
newline()


# main game loop
while True:
    command = prompt()
    err = handle_command(command)

    # -99 means quit
    if err == -99:
        break

    newline()
