class Instructions:

    MOV = 1
    ADD = 2
    INP = 3
    OUT = 4
    MUL = 5
    BEGIN = 6
    END = 7
    PUSH = 8
    POP = 9
    JMP = 10
    JMPIF = 11
    SUB = 12
    CALL = 13
    ADDVAL = 14
    SUBVAL = 15
    PRINT = 16
    STOP = 255


class Pointers:

    IP = 0  # Instruction pointer
    STATIC = 2  # Pointer to beginning of static data
    SP = 4  # Stack pointer


class Registry:

    eip = 0
    esp = 1
    eax = 2
    ebx = 3
    ecx = 4
    edx = 5
    esi = 6

    NUM_REGISTERS = 7
