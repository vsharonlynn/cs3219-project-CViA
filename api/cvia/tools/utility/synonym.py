from nltk.corpus import wordnet

class Synonym():
    def getSynonym(word):
        synonyms = []

        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                synonyms.append(l.name())

        return set(synonyms)

    def determineSynonym(first, second):
        if len(wordnet.synsets(first)) == 0 or len(wordnet.synsets(second)) == 0:
            return 0
        else:
            w1 = wordnet.synset(wordnet.synsets(first)[0].name())
            w2 = wordnet.synset(wordnet.synsets(second)[0].name())
            similarity_ratio = w1.wup_similarity(w2)
            if similarity_ratio != None:
                return similarity_ratio
            else:
                return 0


# print(Synonym.determineSynonym("studies", "education"))
# print(Synonym.determineSynonym("school", "education"))
