from instructions import Instructions, Registry

import sys
import numpy as np


class Assembler:

    def __init__(self):

        self.bytecode = []
        self.static_variables = []

    def init_registers(self):

        for i in range(Registry.NUM_REGISTERS):  # registers
            self.bytecode += [0 for _ in range(4)]
        self.bytecode[Instructions.IP] = Registry.NUM_REGISTERS * 4  # IP value

    def generate(self, filename):

        self.init_registers()

        with open(filename) as file:
            lines = file.readlines()
            for line_string in lines:
                line_string = line_string.split("  ;", 1)[0]  # remove comments
                line = line_string.strip('\n').split(' ')

                if len(line) < 1:
                    continue

                instruction = line[0]

                try:
                    instruction_code = vars(Instructions)[instruction.upper()]

                except KeyError:
                    print("Instruction not found:", instruction, file=sys.stderr)
                    return

                if instruction_code == Instructions.PRINT:  # static print
                    self.static_variables.append(line_string.split(instruction + " ")[1])
                    line = [line_string.split(instruction + " ")[1], str(len(self.static_variables) - 1)]

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

        self.bytecode[Instructions.STATIC] = len(self.bytecode)  # static begin

        static_data = self.init_static_variables()
        self.bytecode[Instructions.SP] = len(self.bytecode) + len(static_data) - 4  # SP value
        self.bytecode += static_data

    def init_static_variables(self):
        size = len(self.static_variables)

        for variable in self.static_variables:
            size += len(variable) + 1

        data = np.zeros(size, dtype=int)
        offset = len(self.static_variables)

        for i in range(len(self.static_variables)):
            data[i] = offset
            variable = self.static_variables[i]
            data[offset] = len(variable)
            offset += 1

            for char in variable:
                data[offset] = ord(char)
                offset += 1

        return data.tolist()

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
