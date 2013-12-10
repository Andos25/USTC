#include <stdio.h>
struct ctx{
    int eip,esp,ebx,ebp;
}M,A,B;
int r,n;
int temp1=1,temp2=1;

__declspec(naked) void swtch(struct ctx *from,struct ctx *to)
{
    __asm{
        mov eax,[esp+4]
        pop dword ptr [eax]
        mov [eax+4],esp
        //mov [eax+8],ebx   it is unuseful in this program
        mov [eax+12],ebp
        mov eax,[esp+8]
        mov ecx,[esp+4]
        mov ebp,[ecx+12]
        //mov ebx,[ecx+8]   it is unuseful in this program
        mov esp,[ecx+4]
        push [ecx]
        ret
    }
}

void A_proc()
{
    __asm{
        pop ecx   //clean stack
        pop ecx   //clean stack
        mov edx, [r]
        cmp [n], 2
        js end
        dec [n]
        add [r], ebx
        mov ebx, edx
        lea edx, A
        push edx
        lea edx, B
        push edx
        call swtch
    end:
        lea edx, M
        push edx
        lea edx, B
        push edx
        call swtch
    }
}

void B_proc()
{
    __asm{
        pop ecx  //clean stack
        pop ecx  //clean stack
        mov edx, [r]
        cmp [n], 2
        js end
        dec [n]
        add [r], ebx
        mov ebx, edx
        lea edx, A
        push edx
        lea edx, B
        push edx
        call swtch
    end:
        lea edx, M
        push edx
        lea edx, B
        push edx
        call swtch
    }
}

int main(int argc, char *argv[])
{
    int Astack[1024];
    int Bstack[1024];
    A.eip = (int)A_proc;
    A.esp = (int)(&Astack[1023]);
    B.eip = (int)B_proc;
    B.esp = (int)(&Bstack[1023]);
    if(argc<2){
     printf("Usage:%s number(<40)\n",argv[0]);
     return -1;
    }
    n = atoi(argv[1]);
    __asm{
        mov [r], 1
        mov ebx, 1
    }
    swtch(&M,&A);
    printf("%d\n",r);
    return 0;
}

