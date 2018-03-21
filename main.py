from memory import Memory
from vm import VM
from assembler import Assembler


def main():

    assembler = Assembler()
    assembler.generate("fib.asm")
    assembler.write_to_file("fib.bin")

    memory = Memory()
    memory.read_file("fib.bin")
    vm = VM(memory)

    vm.run()


main()
