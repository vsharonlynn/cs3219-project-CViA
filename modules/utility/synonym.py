from nltk.corpus import wordnet

class Synonym():
    def getSynonym(word):

        synonyms = []

        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                synonyms.append(l.name())

        return set(synonyms)

    def determineSynonym(first, second):
        w1 = wordnet.synset(wordnet.synsets(first)[0].name())
        w2 = wordnet.synset(wordnet.synsets(second)[0].name())

        return w1.wup_similarity(w2)
    

#print(Synonym.determineSynonym("studies", "education"))

