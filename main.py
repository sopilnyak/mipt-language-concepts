from memory import Memory
from vm import VM


def main():
    memory = Memory(100)
    memory.read_file("double.bin")
    vm = VM(memory)

    vm.run()


main()
