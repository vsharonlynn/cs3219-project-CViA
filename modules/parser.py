'''
Converts PDF file to data structure
Singleton
'''
from utility.chunk_parser import ChunkParser
from utility.pdf_serializer import PdfSerializer
from utility.synonym import Synonym

cv_base = """
WORK EXPERIENCE
· Research Scholar Jan 2011 – present
Spin and Energy Laboratory, National University of Singapore
 Developed simulations and computational methods for various research projects
 Designed and conducted nanofabrication experiments for spintronic devices
 Mentored junior students and taught undergraduate modules
· Research Assistant Aug 2009 – Oct 2010
Low Temperature Physics Laboratory, Indian Institute of Technology, Kanpur
 Developed Internet based labs
 Researched spin injection into metals
· Summer Internship June 2008 – July 2008
Laboratory of Photonics and Interfaces, Ecole Polytechnique de Lausanne, Switzerland
 Researched electro-catalytic activity of a Ruthenium complex in a PEFC electrode
"""

class Parser(object):
    def __init__(self, filenames):
        self.chunk_parser = ChunkParser(cv_base)
        self.categories = ['experience', 'skills', 'activities', 'education']

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
                print(lines[i].encode('ascii', 'ignore').decode('utf-8'))
                max_score, max_category = 0, ''
                for category in self.categories:
                    synonym_score = 0
                    words = lines[i].lower().split()
                    for word in words:
                        curr_score = Synonym.determineSynonym(word, category)
                        synonym_score += curr_score
                    synonym_score /= len(words)
                    print(synonym_score, category)
                    if synonym_score > 0:
                        if synonym_score > max_score:
                            max_score = synonym_score
                            max_category = category
                if max_score > 0:
                    section_category = max_category
            elif (section_category != ''):
                tokenized_words = ChunkParser.extract(self.chunk_parser.parse(lines[i]))
                for word in tokenized_words:
                    if word != '':
                        data[section_category].append(word)

        return data

parser = Parser('')
result = parser.parse('t.pdf')
print(result)
