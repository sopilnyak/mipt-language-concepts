from enumerable import Enumerable


with open('input.txt', 'r') as file:
    lines = file.readlines()
    Enumerable(lines)\
        .select(lambda line: line.split(' '))\
        .flatten()\
        .group_by(lambda x: x)\
        .select(lambda x: (x[0], len(x[1])))\
        .order_by(lambda x: -x[1])\
        .select(lambda x: print("{}: {}".format(x[0], x[1])))\
        .to_list()
