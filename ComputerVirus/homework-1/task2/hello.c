void my_print(char *s);
int main (int argc, char *argv[])
{
    char* string = "hello\n";
    int address;
    address = (int)string;
    my_print(string);
    sprintf(string, "%x", address);
    my_print(string);
    return 0;
}