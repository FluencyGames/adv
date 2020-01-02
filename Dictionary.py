
class Vocabulary(object):
    Dictionary = {
        'Nouns': [],
        'Verbs': [],
        'Articles': [],
        'Prep': [],
        'Adjectives': [],
        'Number': []
    }

    # this is the map of verbs to verbObjects
    Verbs = {}

    # this is the map of nouns to item objects
    Items = {}

    # add a new vocabulary word to our dictionary
    # we define what the type of word is (ie, verb, noun, etc)
    @staticmethod
    def add_to_dictionary(section, word):
        sect = Vocabulary.Dictionary[section]
        if word not in section:
            section.append(word)

    # get the section that the word is in
    @staticmethod
    def find_section(word):
        return [section for section in Vocabulary.Dictionary if word in section]

    @staticmethod
    def is_vocabulary_word(word):
        return Vocabulary.find_section(word) != []

    @staticmethod
    def is_word_type(word, section):
        return word in Vocabulary.Dictionary[section]

    @staticmethod
    def add_verb(verb, obj):
        if verb not in Vocabulary.Verbs:
            Vocabulary.Verbs[verb] = obj

    @staticmethod
    def add_noun(noun, obj):
        if noun not in Vocabulary.Items:
            Vocabulary.Items[noun] = obj

    @staticmethod
    def parse_item_description(desc):
        # this parses an item descriptor and adds to the dictionary
        # format a//small green round//box*es
        pass



