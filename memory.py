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

    def print(self, size):
        for cell in range(size):
            print("{0:2d}".format(self.read(cell)), end=' ')
            if (cell + 1) % 4 == 0:
                print("")

        print("")

    def read_file(self, filename):

        bin_data = np.fromfile(filename, dtype=np.int32)

        for i in range(len(bin_data)):
            self.memory[i] = bin_data[i]
