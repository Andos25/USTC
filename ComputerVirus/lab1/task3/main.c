extern int sum(int);

int main(int argc, char **argv) 
{
    int i;
    char *c = "%d\n";
    if (argc < 2) {
    printf("usage: main number\n");
        return -1;
     }
    i = atoi(argv[1]);
    __asm {
        push [i]
        call sum
        push [c]
        call printf
    }
}