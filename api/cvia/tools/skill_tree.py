from .categories import Categories

class SkillTree(object):
    def __init__(self):
        self.__categories = Categories()

        # initilize all categories list to []
        self.__data = {}
        for category in self.__categories.all():
            self.__data[category] = []

    def keys(self):
        return self.__data.keys()

    def get(self, key):
        return self.__data[key]

    def add(self, key, value):
        self.__data[key].append(value)

    def __str__(self):
        return str(self.__data)
