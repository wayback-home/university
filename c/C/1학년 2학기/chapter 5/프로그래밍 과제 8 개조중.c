#include <stdio.h>

int main(void)
{
    char ascii = 0;
    int retry = 0;
    for (retry = 0; retry < 4; retry++)
    {
        for (ascii = 32 + (retry * 24); ascii < 56 + (retry * 24); ascii++)
        {
            printf("%C", ascii);
        }
        printf("\n");
    }
    return 0;
}