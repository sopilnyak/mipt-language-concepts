from memory import Memory
from vm import VM
from assembler import Assembler
from disassembler import Disassembler

import sys


def main(is_assembly_mode):

    memory = Memory()

    if is_assembly_mode:  # assembly mode

        assembler = Assembler("fibonacci.asm")
        assembler.write_to_file("fibonacci.bin")

        memory.read_file("fibonacci.bin")

        vm = VM(memory)
        vm.run()

        return

    disassembler = Disassembler("fibonacci.bin")
    disassembler.write_to_file("fibonacci_disassembled.asm")

    assembler = Assembler("fibonacci_disassembled.asm")
    assembler.write_to_file("fibonacci_disassembled.bin")

    memory.read_file("fibonacci_disassembled.bin")

    vm = VM(memory)
    vm.run()


main(True if len(sys.argv) < 2 or sys.argv[1] != '1' else False)
