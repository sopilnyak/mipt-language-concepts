from instructions import Instructions


class VM:

    def __init__(self, memory, instruction_size=4):
        self.memory = memory
        self.instruction_size = instruction_size
        self.is_in_function = False
        self.function_ips = {}

    def get(self, src, depth=0):
        while depth >= 0:
            src = self.memory.read(src)
            depth -= 1
        return src

    def inp(self, dst):
        value = int(input())
        self.memory.write(dst, value)

    def out(self, src):
        print(self.memory.read(src))

    def print_static(self, value):
        address = self.memory.read(self.static_begin() + value)
        length = self.memory.read(self.static_begin() + address)
        output = ""
        for i in range(length):
            output += chr(self.memory.read(self.static_begin() + address + i + 1))
        print(output, end="")

    def mov(self, dst, src, depth=0):
        src_value = self.get(src, depth)
        self.memory.write(dst, src_value)

    def inc(self, src):
        src_value = self.memory.read(src)
        self.memory.write(src, src_value + 1)

    def add(self, left, right):
        left_value = self.memory.read(left)
        right_value = self.memory.read(right)
        self.memory.write(left, left_value + right_value)

    def add_val(self, left, right_value):
        left_value = self.memory.read(left)
        self.memory.write(left, left_value + right_value)

    def sub(self, left, right):
        left_value = self.memory.read(left)
        right_value = self.memory.read(right)
        self.memory.write(left, left_value - right_value)

    def sub_val(self, left, right_value):
        left_value = self.memory.read(left)
        self.memory.write(left, left_value - right_value)

    def mul(self, left, right):
        left_value = self.memory.read(left)
        right_value = self.memory.read(right)
        self.memory.write(left, left_value * right_value)

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

    def static_begin(self):
        return self.memory.read(Instructions.STATIC)

    def print(self, cell):
        return self.memory.read(cell)

    def function_begin(self, name):
        self.is_in_function = True
        self.function_ips[name] = self.ip_value()

    def function_end(self):
        self.is_in_function = False

    def stack_pop(self):
        self.sub_val(self.sp_address(), 4)

    def stack_push(self, address):
        self.add_val(self.sp_address(), 4)
        self.memory.write(self.sp_value(), self.memory.read(address))

    def call(self, name):
        self.memory.write(self.ip_address(), self.function_ips[name])

    def jmp(self, dst):
        self.memory.write(self.ip_address(), self.memory.read(dst))

    def jump_if(self, src, diff):
        value = self.memory.read(src)
        if value > 0:
            self.add_val(self.ip_address(), diff * 4)
        else:
            self.next()

    def execute_next(self, instruction_code):

        if instruction_code == Instructions.END:
            self.function_end()
            self.next()
            return

        if self.is_in_function:  # function declaration
            self.next()
            return

        argument1 = self.memory.read(self.ip_value() + 1)
        argument2 = self.memory.read(self.ip_value() + 2)
        depth = self.memory.read(self.ip_value() + 3)

        if instruction_code == Instructions.MOV:
            self.mov(argument1, argument2, depth)
            self.next()
            return

        if instruction_code == Instructions.ADD:
            self.add(argument1, argument2)
            self.next()
            return

        if instruction_code == Instructions.SUB:
            self.sub(argument1, argument2)
            self.next()
            return

        if instruction_code == Instructions.ADDVAL:
            self.add_val(argument1, argument2)
            self.next()
            return

        if instruction_code == Instructions.SUBVAL:
            self.sub_val(argument1, argument2)
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

        if instruction_code == Instructions.PRINT:
            self.print_static(argument1)
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

        if instruction_code == Instructions.PUSH:
            self.stack_push(argument1)
            self.next()
            return

        if instruction_code == Instructions.POP:
            self.stack_pop()
            self.next()
            return

        if instruction_code == Instructions.CALL:
            self.call(argument1)
            self.next()
            return

        if instruction_code == Instructions.JMPIF:
            self.jump_if(argument1, argument2)
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
