#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[])
{
    int n, r;
    if (argc < 2) {
        printf("Usage: %s number(<40)\n", argv[0]);
        return -1;
    }
    n = atoi(argv[1]);
    __asm {
        mov ebx, [n]
        mov ecx, 1
        call fib
        jmp end
    fib:
        cmp ecx, ebx
        jns setvalue
        dec ebx
        push ebx
        call fib
        pop ebx
        push edx
        dec ebx
        push ebx
        call fib
        pop ebx
        pop eax
        add edx, eax
        ret
    setvalue:
        mov edx, 1
        ret
    end:
        mov [r], edx
    }
    printf("fib(%d) = %d\n", n, r);
    return 0;
}
