class Instructions:

    IP = 0  # Instruction pointer
    SP = 1  # Stack pointer
    MOV = 1
    ADD = 2
    INP = 3
    OUT = 4
    MUL = 5
    JMP = 10
    BEGIN = 6
    END = 7
    PUSH = 8
    POP = 9
    STOP = 255


class Registry:

    eip = 0
    esp = 1
    eax = 2
    ebx = 3
    ecx = 4
    edx = 5
    esi = 6

    NUM_REGISTERS = 7