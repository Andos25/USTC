#include "stdio.h"
/* sum.c */
int sum(int i) 
{
    __asm {
        mov ecx, [i]
        mov eax, 0
    calc:
        add eax, [i]
        dec [i]
        loop calc
        mov [i], eax
    }
    return i;
}
