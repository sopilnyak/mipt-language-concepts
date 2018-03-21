begin 1
mov eax *esp
pop
jmpif eax 5
mov edx eax
mov esi *esp
pop
jmp esi
subval eax 1
jmpif eax 6
addval eax 1
mov edx eax
mov esi *esp
pop
jmp esi
addval eax 1
subval eax 1
mov esi eip
addval esi 20
push eax
push esi
push eax
call 1
mov eax *esp
pop
mov ebx edx
subval eax 1
mov esi eip
addval esi 20
push ebx
push esi
push eax
call 1
mov ebx *esp
pop
add edx ebx
mov esi *esp
pop
jmp esi
end
print eip
print eip
inp eax
mov esi eip
addval esi 16
push esi
push eax
call 1
out edx
stop
add eip eip
jmp ecx
add esp *****************************************************************************************************esp
