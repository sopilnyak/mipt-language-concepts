IP = 0
MOV = 1
ADD = 2
INP = 3
OUT = 4
MUL = 5
STOP = 255


class VM:

    def __init__(self, memory, instruction_size=4):
        self.memory = memory
        self.instruction_size = instruction_size

    def inp(self, dst):
        value = int(input())
        self.memory.write(dst, value)
        self.next()

    def out(self, src):
        print(self.memory.read(src))
        self.next()

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
        next_instruction = self.ip_value() + self.instruction_size
        self.memory.write(self.ip_address(), next_instruction)

    def ip_address(self):
        return IP
    
    def ip_value(self):
        return self.memory.read(self.ip_address())

    def print(self, cell):
        return self.memory.read(cell)

    def execute_next(self, instruction_code):
        argument1 = self.memory.read(self.ip_value() + 1)
        argument2 = self.memory.read(self.ip_value() + 2)

        if instruction_code == MOV:
            self.mov(argument1, argument2)
            return

        if instruction_code == ADD:
            self.add(argument1, argument2)
            return

        if instruction_code == INP:
            self.inp(argument1)
            return

        if instruction_code == OUT:
            self.out(argument1)
            return

        if instruction_code == MUL:
            self.mul(argument1, argument2)
            return

    def run(self):

        while True:
            instruction_code = self.memory.read(self.ip_value())

            if instruction_code == STOP:
                return

            self.execute_next(instruction_code)

    def run_step(self):
        instruction_code = self.memory.read(self.ip_value())

        if instruction_code == STOP:
            return

        self.execute_next(instruction_code)
