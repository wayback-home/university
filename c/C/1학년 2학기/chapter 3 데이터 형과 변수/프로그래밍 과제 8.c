#include <stdio.h>

int main(void)
{
    float inch = 0;
    float exc = 2.54;

    printf("길이(in)?\n");
    scanf("%f", &inch);

    printf("%4.2f = %4.2f cm\n", inch, inch * exc);

    return 0;
}