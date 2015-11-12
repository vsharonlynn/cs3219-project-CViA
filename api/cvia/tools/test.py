from categories import Categories
from skill_tree import SkillTree
from analyser import Analyser
from parser import Parser

parser = Parser(['t.pdf'])
result = parser.parse('t.pdf')
print(result)

#===============================================================================
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
#===============================================================================
