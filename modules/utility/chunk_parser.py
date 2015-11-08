import nltk
from nltk.corpus import conll2000

cv1 = """
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
cv2 = """
Research Intern Genome Institute of Singapore. A*STAR, Singapore Aug – Oct 2012
    Worked on bioinformatics related to cancer genetics.
    Data base mining for cancers and drugs that could be used to treat them
    Created a genome data base for few types of cancersResearch Intern Genome Institute of Singapore. A*STAR, Singapore Aug – Oct 2012
    Worked on bioinformatics related to cancer genetics.
    Data base mining for cancers and drugs that could be used to treat them
    Created a genome data base for few types of cancers
"""

class ChunkParser(nltk.ChunkParserI):
    def __init__(self, train_sents):
         train_data = ChunkParser.tag(train_sents)
         self.tagger = nltk.UnigramTagger(train_data)

    def parse(self, test_sents):
         test_data = ChunkParser.tokenize(test_sents)
         tagged = [self.tagger.tag(sent) for sent in test_data]
         return tagged

    def tag(document):
        sentences = ChunkParser.tokenize(document)
        sentences = [nltk.pos_tag(sent) for sent in sentences]
        return sentences

    def tokenize(document):
        sentences = nltk.sent_tokenize(document)
        sentences = [nltk.word_tokenize(sent) for sent in sentences]
        return sentences

    def extract(tagged):
        list = []
        for sent in tagged:
            for (pos, chunktag) in sent:
                if chunktag == 'NNP':
                    list.append(pos.encode('ascii', 'ignore').decode('utf-8'))
        return list

# unigram_tagger = ChunkParser(cv1)
# tagged_data = unigram_tagger.parse(cv2);
# print(ChunkParser.extract(tagged_data))
