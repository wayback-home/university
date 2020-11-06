#include <stdio.h>

int main(void)
{
    float gram = 0;
    float cm3 = 0;

    printf("질량(g)?\n");
    scanf("%f", &gram);

    printf("부피(세제곱센티미터)?\n");
    scanf("%f", &cm3);

    printf("밀도: %f", gram / cm3);

    return 0;
}