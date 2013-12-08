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
        mov eax, [n]
    fib:
        mov ebx, 1
        sub ebx, eax
        push eax
        jns finish
        sub eax, 1
        loop fib
    finish:
        mov [r], 1
        mov ebx, 1
    calc:
        pop eax
        mov edx, [r]
        cmp eax, [n]
        je end
        add [r], ebx
        mov ebx, edx
        loop calc
    end:
    }
    printf("fib(%d) = %d\n", n, r);
    return 0;
}
