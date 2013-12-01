#include <stdio.h>

void my_print(char *s);
int main (int argc, char *argv[])
{
    char* string = "hello\n";
    int address;

    address = (int)main;
    my_print("address of main:");
    sprintf(string, "%x", address);
    my_print(string);

    address = (int)my_print;
    my_print("\naddress of my_print:");
    sprintf(string, "%x", address);
    my_print(string);

    address = (int)printf;
    my_print("\naddress of printf:");
    sprintf(string, "%x", address);
    my_print(string);
    return 0;
}