#include <stdio.h>

int main(void)
{
    float getTem = 0;
    char temtype;

    printf("온도?");
    scanf("%f %c", &getTem, &temtype);

    float exctoC = (getTem - 32) * 5 / 9;
    float exctoF = ((getTem * 9) / 5 + 32);

    if (temtype == 'c')
        printf("%4.2f C == %4.2f F", getTem, exctoF);
    else
        printf("%4.2f F == %4.2f C", getTem, exctoC);

    return 0;
}