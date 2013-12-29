#include "windows.h"
#pragma comment (lib, "user32.lib")

char code[] = {0x33, 0xC0};
int main(int argc, char const *argv[])
{
    DWORD pid = 11140,hproc;
    LPDWORD numx;
    PBYTE pRemote = (PBYTE)0x0040101A;
    int write;
    hproc = OpenProcess(
          PROCESS_CREATE_THREAD  | PROCESS_QUERY_INFORMATION
        | PROCESS_VM_OPERATION   | PROCESS_VM_WRITE 
        | PROCESS_VM_READ, FALSE, pid);
    VirtualProtect(hproc, 2, PAGE_EXECUTE_READWRITE, &numx);
    WriteProcessMemory(hproc, pRemote, code, 2, &write);
    return 0;
}