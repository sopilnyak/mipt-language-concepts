from instructions import Instructions, Registry, Pointers

import numpy as np
import sys


class Disassembler:

    def __init__(self, filename):

        self.instructions = []
        self.arguments_number = {
            1: 2, 2: 2, 3: 1, 4: 1, 5: 2, 6: 1, 7: 0, 8: 1, 9: 0,
            10: 1, 11: 2, 12: 2, 13: 1, 14: 2, 15: 2, 16: 1, 255: 0
        }
        self.instructions_with_nums = {6: 1, 11: 2, 13: 1, 14: 2, 15: 2}
        self.bytecode = np.fromfile(filename, dtype=int)

        self.instructions_dict = dict((value, key)
                                      for key, value in vars(Instructions).items())

        self.registries_dict = dict((value, key)
                                    for key, value in vars(Registry).items())

        self.disassembly()

    def disassembly(self):

        static_begin = self.bytecode[Pointers.STATIC]

        for i in range(Registry.NUM_REGISTERS * 4, static_begin, 4):  # Skip registers

            instruction_code = self.bytecode[i]

            try:
                instruction = self.instructions_dict[instruction_code]

                if instruction.lower() == "print":
                    instruction += " " + self.get_static(self.bytecode[static_begin:],
                                                         self.bytecode[i + 1])
                    self.instructions.append(instruction.lower())
                    continue

            except KeyError:
                print("Instruction not found:", instruction_code, file=sys.stderr)
                continue

            for argument_num in range(1, 3):
                instruction += self.parse_argument(self.bytecode[i + argument_num],
                                                   argument_num, instruction_code,
                                                   self.bytecode[i + 3])

            self.instructions.append(instruction.lower())

    def parse_argument(self, argument, argument_num, instruction_code, depth):

        if self.arguments_number[instruction_code] >= argument_num:

            if instruction_code in self.instructions_with_nums and \
                    self.instructions_with_nums[instruction_code] == argument_num:

                return " " + str(argument)

            else:
                depth_string = "*" * depth if argument_num == 2 else ""
                try:
                    return " " + depth_string + self.registries_dict[argument // 4]

                except KeyError:
                    print("Registry not found:", argument // 4, file=sys.stderr)

        return ""

    def get_static(self, static_data, num):

        static = ""
        for i in range(static_data[static_data[num]]):
            static += chr(static_data[static_data[num] + i + 1])
        return static[:-1]  # remove /n

    def write_to_file(self, filename):

        with open(filename, "w") as file:
            for item in self.instructions[:-1]:
                file.write("%s\n" % item)
            file.write("%s" % self.instructions[-1])
