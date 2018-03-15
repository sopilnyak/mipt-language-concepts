from instructions import Instructions


class VM:

    def __init__(self, memory, instruction_size=4):
        self.memory = memory
        self.instruction_size = instruction_size
        self.is_in_function = False
        self.return_addresses = {}

    def inp(self, dst):
        value = int(input("Input: "))
        self.memory.write(dst, value)

    def out(self, src):
        print(self.memory.read(src))

    def mov(self, dst, src):
        src_value = self.memory.read(src)
        self.memory.write(dst, src_value)

    def inc(self, src):
        src_value = self.memory.read(src)
        self.memory.write(src, src_value + 1)

    def add(self, left, right):
        left_value = self.memory.read(left)
        right_value = self.memory.read(right)
        self.memory.write(left, left_value + right_value)

    def sub(self, left, right):
        left_value = self.memory.read(left)
        right_value = self.memory.read(right)
        self.memory.write(left, left_value - right_value)

    def mul(self, left, right):
        left_value = self.memory.read(left)
        right_value = self.memory.read(right)
        self.memory.write(left, left_value * right_value)

    def jmp(self, dst):
        self.memory.write(self.ip_address(), self.memory[dst])

    def stop(self):
        pass

    def next(self):
        next_instruction = self.ip_value() + self.instruction_size
        self.memory.write(self.ip_address(), next_instruction)

    def ip_address(self):
        return Instructions.IP
    
    def ip_value(self):
        return self.memory.read(self.ip_address())

    def sp_address(self):
        return Instructions.SP

    def sp_value(self):
        return self.memory.read(self.sp_address())

    def print(self, cell):
        return self.memory.read(cell)

    def function_begin(self, name_address):
        self.is_in_function = True
        name = self.memory.read(name_address)
        self.return_addresses[name] = self.ip_value() + 4

    def function_end(self):
        self.is_in_function = False

    def stack_pop(self):
        self.add(self.sp_address(), 1)

    def stack_push(self, address):
        self.sub(self.sp_address(), 1)
        self.memory.write(self.sp_value(), self.memory.read(address))

    def stack_call(self, address):
        self.stack_push(self.ip_value() + 4)
        value = self.memory.read(address)
        self.memory.write(self.ip_address(), self.return_addresses[value])

    def execute_next(self, instruction_code):
        argument1 = self.memory.read(self.ip_value() + 1)
        argument2 = self.memory.read(self.ip_value() + 2)

        if instruction_code == Instructions.MOV:
            self.mov(argument1, argument2)
            self.next()
            return

        if instruction_code == Instructions.ADD:
            self.add(argument1, argument2)
            self.next()
            return

        if instruction_code == Instructions.INP:
            self.inp(argument1)
            self.next()
            return

        if instruction_code == Instructions.OUT:
            self.out(argument1)
            self.next()
            return

        if instruction_code == Instructions.MUL:
            self.mul(argument1, argument2)
            self.next()
            return

        if instruction_code == Instructions.JMP:
            self.jmp(argument1)
            self.next()
            return

        if instruction_code == Instructions.BEGIN:
            self.function_begin(argument1)
            self.next()
            return

        if instruction_code == Instructions.END:
            self.function_end()
            self.next()
            return

        if instruction_code == Instructions.PUSH:
            self.stack_push(argument1)
            self.next()
            return

        if instruction_code == Instructions.POP:
            self.stack_pop()
            self.next()
            return

    def run(self):

        while True:
            instruction_code = self.memory.read(self.ip_value())

            if instruction_code == Instructions.STOP:
                return

            self.execute_next(instruction_code)

    def run_step(self):
        instruction_code = self.memory.read(self.ip_value())

        if instruction_code == Instructions.STOP:
            return

        self.execute_next(instruction_code)
