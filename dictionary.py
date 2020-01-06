
class Vocabulary(object):
    Dictionary = {}
    Parts_of_speech = ['Article', 'Thing', 'Adjective', 'Verb', 'Preposition', 'Number', 'Text']

    @staticmethod
    def dump():
        print(Vocabulary.Dictionary)

    # add a new vocabulary word to our dictionary
    # we define what the type of word is (ie, verb, noun, etc)
    @staticmethod
    def add_word(word: str, part_of_speech: str, obj: object) -> bool:
        if len(word) == 0 or len(part_of_speech)==0 or object is None:
            # todo: Error(invalid word added to dictionary)
            return False

        if Vocabulary.Dictionary.get(word) is None:
            Vocabulary.Dictionary[word] = {part_of_speech: obj}
        else:
            word_map = Vocabulary.Dictionary[word]
            if part_of_speech in Vocabulary.Parts_of_speech:
                if Vocabulary.Dictionary.get(part_of_speech) is None:
                    word_map[part_of_speech] = obj
                    return True
            else:
                # Todo: Error('Vocabulary Word not part of speech!')
                pass

        return False

    @staticmethod
    # adds a list of new vocabulary words to our dictionary
    def add_words(words: list, part_of_speech: str, obj: object) -> bool:
        added = False
        if not words:
            return False

        for w in words:
            if Vocabulary.add_word(w, part_of_speech, obj):
                added = True

        return True

    # returns a list of all parts of speech that the word is a part of
    @staticmethod
    def get_parts_of_speech(word) -> list:
        word_map = Vocabulary.Dictionary[word]
        if word_map is not None:
            return [p for k, p in word_map]
        return []

    # returns a list of words that belong to a particular part of speech
    @staticmethod
    def get_words(part_of_speech:str) -> list:
        return [w for w, m in Vocabulary.Dictionary.items() if m[part_of_speech] is not None]

    # returns True if the word is part of our vocabulary
    @staticmethod
    def is_vocabulary_word(word: str) -> bool:
        return not Vocabulary.Dictionary.get(word) is None

    # returns True if the word is in the given part of speech
    @staticmethod
    def is_word_type(word: str, part_of_speech: str) -> bool:
        return Vocabulary.Dictionary[word] is not None and Vocabulary.Dictionary[word].get(part_of_speech) is not None

    # adds a verb to our vocabulary, and attaches the object
    # parse the verb and for each common-delimted alias/shorthand, add to our dictionary
    # format: longname, alias, alias
    @staticmethod
    def add_verb(verb: str, obj: object) -> bool:
        verbs = verb.split(',')
        if Vocabulary.Dictionary.get(verbs[0]) is not None:
            # Todo: Error('verb already in dictionary')
            return False
        else:
            for v in verbs:
                Vocabulary.add_word(v.strip(), 'Verb', obj)
        return True

    # adds a thing name to our vocabulary, and attaches the object
    # parse the thing for articles, adjectives, and nouns
    # format: longname, alias, alias
    @staticmethod
    def add_thing(thing: str, obj: object) -> bool:
        return False




