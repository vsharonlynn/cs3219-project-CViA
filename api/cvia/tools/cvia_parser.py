'''
Converts PDF file to data structure
Singleton
'''
from .utility.chunk_parser import ChunkParser
from .utility.pdf_serializer import PdfSerializer
from .utility.synonym import Synonym
from .categories import Categories
from .skill_tree import SkillTree

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class CviaParser(object):
    __metaclass__ = Singleton

    def __init__(self, filenames):
        self.__categories = Categories()

        learning_text = ""
        for filename in filenames:
            pdf_serializer = PdfSerializer(filename)
            learning_text += pdf_serializer.getString()
        self.__chunk_parser = ChunkParser(learning_text)

    def parse(self, filename):
        raw_text = self.__extract(filename)
        data_structure = self.__generateDataStructure(raw_text)
        return data_structure

    def __extract(self, filename):
        pdf_serializer = PdfSerializer(filename)
        return pdf_serializer.getString()

    def __generateDataStructure(self, raw_text):
        skill_tree = SkillTree()

        # construct {category: [member, ...], category: [member, ...], ...}
        section_category = ''
        lines = raw_text.split('\n')
        for i in range(len(lines)):
            if lines[i] == '':
                continue

            if (i-11 >= 0 and lines[i-1] == '') and (i+1 < len(lines) and lines[i+1] == ''):
                section_category = self.__chooseCategory(section_category, lines[i])
            elif section_category != '':
                tokenized_words = self.__chunk_parser.extract(lines[i])
                for word in tokenized_words:
                    if word != '':
                        skill_tree.add(section_category, word)
        return skill_tree

    def __chooseCategory(self, current_category, line):
        max_score, max_category = 0, ''
        for category in self.__categories.all():
            synonym_score = 0
            words = line.lower().split()
            for word in words:
                curr_score = Synonym.determineSynonym(word, category)
                synonym_score += curr_score
            synonym_score /= len(words)
            if synonym_score > max_score:
                max_score = synonym_score
                max_category = category
        if max_score > 0:
            return max_category
        else:
            return current_category
