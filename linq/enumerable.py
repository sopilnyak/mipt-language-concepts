import collections


class Enumerable:
    def __init__(self, collection):
        self.collection = collection

    def __select__(self, func):
        for element in self.collection:
            yield func(element)

    def select(self, func):
        return Enumerable(self.__select__(func))

    def __flatten__(self):
        for subcollection in self.collection:
            for element in subcollection:
                yield element

    def flatten(self):
        return Enumerable(self.__flatten__())

    def __where__(self, predicate):
        for element in self.collection:
            if predicate(element):
                yield element

    def where(self, predicate):
        return Enumerable(self.__where__(predicate))

    def __take__(self, k):
        for i, element in enumerate(self.collection):
            if i == k:
                break
            yield element

    def take(self, k):
        return Enumerable(self.__take__(k))

    def __group_by__(self, func):
        dictionary = collections.defaultdict(list)
        for element in self.collection:
            dictionary[func(element)].append(element)

        return dictionary.items()

    def group_by(self, func):
        return Enumerable(self.__group_by__(func))

    def order_by(self, func):
        return Enumerable(sorted(self.collection, key=func))

    def to_list(self):
        return list(self.collection)
