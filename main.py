from memory import Memory
from vm import VM
from assembler import Assembler


def main():

    assembler = Assembler()
    assembler.generate("double.asm")
    assembler.write_to_file("double.bin")

    memory = Memory()
    memory.read_file("double.bin")
    vm = VM(memory)

    vm.run()


main()
