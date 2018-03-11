import numpy as np

NUM_CELLS = 1000


class Memory:

    def __init__(self, num_cells=NUM_CELLS):
        self.num_cells = num_cells
        self.memory = np.empty(num_cells, dtype=int)

    def read(self, address):
        return self.memory[address]

    def write(self, address, value):
        self.memory[address] = value

    def print(self):
        for cell in range(7):
            print("{0:2d}".format(self.read(cell)), end=' ')

        print("")
