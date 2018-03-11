from memory import Memory
from vm import VM


def main():
    memory = Memory(100)
    vm = VM(memory)
    print("\n")
    memory.write(0, 1)
    memory.write(1, 6)
    memory.write(2, 5)
    memory.write(3, 0)
    memory.write(4, 2)
    memory.write(5, 8)
    memory.write(6, 0)
    memory.print()
    vm.execute_next()
    memory.print()
    vm.execute_next()
    memory.print()


main()
