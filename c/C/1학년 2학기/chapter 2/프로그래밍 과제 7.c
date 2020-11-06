#include <stdio.h>

int main(void)
{
    float first;
    float second;

    printf("실수 2개?\n");
    scanf("%f %f", &first, &second);

    printf("%f + %f = % f\n", first, second, first + second);
    printf("%f - %f = % f", first, second, first - second);

    return 0;
}