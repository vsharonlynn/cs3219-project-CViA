from categories import Categories
from skill_tree import SkillTree
from analyser import Analyser
from cvia_parser import CviaParser

parser = CviaParser(['t.pdf', 'Resume_DesmondLim_2015.pdf'])
cv1 = parser.parse('t.pdf')
print(str(cv1))
cv2 = parser.parse('Resume_DesmondLim_2015.pdf')
print(str(cv2))

test = Analyser(cv1)
test.compare(cv2)
test.computeScore()
print(test.getScore())
test.changeWeightage(0.1, 0.2, 0.3, 0.4)
test.computeScore()
print(test.getScore())
