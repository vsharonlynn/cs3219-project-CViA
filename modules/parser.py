'''
Converts PDF file to data structure
'''
class Parser(object):
    def __init__(self, filename):
        self.filename = filename
        self.categories = ['education', 'work experience', 'skills', 'activities']

    def parse(self):
        #extractPDF
        #generateDataStructure
        pass

    def extractPDF(self):
        pass

    def generateDataStructure(self):
        # initilize all categories list to []
        data_structure = {}
        for category in categories:
            data_structure[category] = []

        # for each section, get base category, append members to category
        # to come up with {category: [member, ...], category: [member, ...], ...}
        pass
