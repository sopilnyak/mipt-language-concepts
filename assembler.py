from instructions import Instructions, Registry

import sys
import numpy as np


class Assembler:

    def __init__(self):

        self.bytecode = []

    def init_registers(self):

        for i in range(Registry.NUM_REGISTERS):  # registers
            self.bytecode += [0 for _ in range(4)]
        self.bytecode[0] = Registry.NUM_REGISTERS * 4  # IP value

    def generate(self, filename):

        self.init_registers()

        with open(filename) as file:
            lines = file.readlines()
            for line in lines:
                line = line.split("  ;", 1)[0]  # remove comments
                line = line.strip('\n').split(' ')

                if len(line) < 1:
                    continue

                instruction = line[0]

                try:
                    instruction_code = vars(Instructions)[instruction.upper()]

                except KeyError:
                    print("Instruction not found:", instruction, file=sys.stderr)
                    return

                self.bytecode.append(instruction_code)

                if len(line) > 1:
                    argument, depth = self.parse_argument(line[1])
                    self.bytecode.append(argument)
                else:
                    self.bytecode.append(0)

                if len(line) > 2:
                    argument, depth = self.parse_argument(line[2])
                    self.bytecode.append(argument)
                    self.bytecode.append(depth)
                else:
                    for _ in range(2):
                        self.bytecode.append(0)

                self.bytecode[4] = len(self.bytecode) - 4  # SP value

    def parse_argument(self, argument):

        depth = argument.count("*")
        argument = argument[depth:]

        try:
            argument_code = vars(Registry)[argument.lower()] * 4

        except KeyError:

            try:
                argument_code = int(argument)

            except ValueError:
                print("Wrong argument:", argument, file=sys.stderr)
                return

        return argument_code, depth

    def write_to_file(self, filename):

        np.array(self.bytecode, dtype=int).tofile(filename)
