begin 1
mov eax *esp  ; pop function argument
pop
jmpif eax 5  ; if n == 0
mov edx eax  ; save n to result
mov esi *esp  ; pop return address
pop
jmp esi  ; go to return address
subval eax 1  ; if n == 1
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
push eax  ; push local variable to save for f(n - 2) call
push esi  ; push return address
push eax  ; push argument
call 1  ; call f(n - 1)
mov eax *esp  ; pop local variable for f(n - 2) call
pop
mov ebx edx  ; save return from f(n - 1)
subval eax 1
mov esi eip
addval esi 20
push ebx  ; push return from f(n - 1)
push esi
push eax
call 1  ; call f(n - 2)
mov ebx *esp  ; pop return from f(n - 1)
pop
add edx ebx  ; f(n - 1) + f(n - 2)
mov esi *esp
pop
jmp esi
end
inp eax
mov esi eip
addval esi 16
push esi
push eax
call 1
out edx
stop