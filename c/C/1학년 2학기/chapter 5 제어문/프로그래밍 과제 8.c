#include <stdio.h>

int main(void)
{
    char ascii = 0;

    for (ascii = 32; ascii < 56; ascii++)
    {
        printf("%C", ascii);
    }
    printf("\n");

    for (ascii = 56; ascii < 80; ascii++)
    {
        printf("%C", ascii);
    }
    printf("\n");

    for (ascii = 80; ascii < 104; ascii++)
    {
        printf("%C", ascii);
    }
    printf("\n");

    for (ascii = 104; ascii < 127; ascii++)
    {
        printf("%C", ascii);
    }

    return 0;
}