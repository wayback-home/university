#include <stdio.h>

int main(void)
{
    int yard = 0;
    double exc = 0.9144;

    printf("길이(yd)?\n");
    scanf("%d", &yard);

    printf("%d yd = %8.6lf\n", yard, yard * exc);

    return 0;
}