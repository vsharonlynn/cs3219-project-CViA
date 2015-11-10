'''
Calculates the score between two data structures
'''
class Analyser(object):
    def __init__(self, jd):
        self.__score = 0
        self.__jd = jd
        self.__fields = ["education", "skills", "experience", "activities"]
        self.__weightage = [0.25, 0.25, 0.25, 0.25]

    def compare(self, resume):
        # compare jd and resume while updating intemediate score and JD counts
        self.intScore = [0, 0, 0, 0]
        self.jdTotal = [0, 0, 0, 0]
        for i in range(0, 4):
            if ((self.__fields[i] in jd) and (self.__fields[i] in resume)):
                for key in self.__jd.get(self.__fields[i]):
                    self.jdTotal[i] += 1
                    if (resume.get(self.__fields[i]).count(key) != 0):
                        self.intScore[i] += 1

    def changeWeightage(self, edu, skill, exp, act):
        # allow user to update the weigtage for counting of scores
        self.__weightage[0] = edu
        self.__weightage[1] = skill
        self.__weightage[2] = exp
        self.__weightage[3] = act

    def computeScore(self):
        # update the score using the weightage given
        for i in range(0, 4):
            if self.intScore[i] != 0:
                self.__score += self.__weightage[i] * self.intScore[i]/self.jdTotal[i]

    def getScore(self):
        return self.__score

# jd = {"education": ["Singapore", "NUS", "Oxford"],
#      "skills": ["python", "java"],
#      "experience": ["3 years"],
#      "activities": ["ICPC"]}
# cv = {"education": ["Malaysia", "NTU", "Oxford"],
#      "skills": ["python", "javascript"],
#      "EXPERIENCE": [],
#      "activities": ["ACM"]}
# test = Analyser(jd)
# test.compare(cv)
# test.computeScore()
# print(test.getScore())
# test.changeWeightage(0.1, 0.2, 0.3, 0.4)
# test.computeScore()
# print(test.getScore())