IP = 0
MOV = 1
ADD = 2


class VM:

    def __init__(self, memory, instruction_size=4):
        self.memory = memory
        self.instruction_size = instruction_size

    def inp(self, value):
        pass

    def out(self, value):
        pass

    def mov(self, dst, src):
        src_value = self.memory.read(src)
        self.memory.write(dst, src_value)
        self.next()

    def inc(self, src):
        src_value = self.memory.read(src)
        self.memory.write(src, src_value + 1)
        self.next()

    def add(self, left, right):
        left_value = self.memory.read(left)
        right_value = self.memory.read(right)
        self.memory.write(left, left_value + right_value)
        self.next()

    def sub(self, left, right):
        left_value = self.memory.read(left)
        right_value = self.memory.read(right)
        self.memory.write(left, left_value - right_value)
        self.next()

    def mul(self, left, right):
        left_value = self.memory.read(left)
        right_value = self.memory.read(right)
        self.memory.write(left, left_value * right_value)
        self.next()

    def stop(self):
        pass

    def next(self):
        next_instruction = self.memory.read(self.ip() + self.instruction_size)
        self.memory.write(self.ip(), next_instruction)

    def ip(self):
        return IP

    def print(self, cell):
        return self.memory.read(cell)

    def execute_next(self):
        instruction_code = self.memory.read(self.ip())
        argument1 = self.memory.read(self.ip() + 1)
        argument2 = self.memory.read(self.ip() + 2)

        if instruction_code == MOV:
            self.mov(argument1, argument2)
            return

        if instruction_code == ADD:
            self.add(argument1, argument2)
            return
