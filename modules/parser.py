'''
Converts PDF file to data structure
Singleton
'''
from utility.chunk_parser import ChunkParser
from utility.pdf_serializer import PdfSerializer
from utility.synonym import Synonym

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Parser(object):
    __metaclass__ = Singleton

    def __init__(self, filenames):
        self.categories = ['experience', 'skills', 'activities', 'education']

        learning_text = ""
        for filename in filenames:
            pdf_serializer = PdfSerializer(filename)
            learning_text += pdf_serializer.getString()
        self.chunk_parser = ChunkParser(learning_text)

    def parse(self, filename):
        # initilize all categories list to []
        data = {}
        for category in self.categories:
            data[category] = []

        # for each section, get base category, append members to category
        # to come up with {category: [member, ...], category: [member, ...], ...}
        pdf_serializer = PdfSerializer(filename)
        raw_text = pdf_serializer.getString()
        section_category = ''
        lines = raw_text.split('\n')
        for i in range(len(lines)):
            if lines[i] == '':
                continue

            if (i-11 >= 0 and lines[i-1] == '') and (i+1 < len(lines) and lines[i+1] == ''):
                section_category = self.chooseCategory(section_category, lines[i])
            elif section_category != '':
                tokenized_words = self.chunk_parser.extract(lines[i])
                for word in tokenized_words:
                    if word != '':
                        data[section_category].append(word)
        return data

    def chooseCategory(self, current_category, line):
        max_score, max_category = 0, ''
        for category in self.categories:
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

parser = Parser(['t.pdf'])
result = parser.parse('t.pdf')
print(result)
