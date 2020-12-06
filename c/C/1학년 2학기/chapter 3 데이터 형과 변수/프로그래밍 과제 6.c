#include <stdio.h>

int main(void)
{
    double getWon = 0;
    int exc = 0;

    printf("KRW?\n");
    scanf("%lf", &getWon);

    printf("원/달러 환율?\n");
    scanf("%d", &exc);

    printf("KRW %6.0f = USD %5.2lf", getWon, getWon / exc);

    return 0;
}