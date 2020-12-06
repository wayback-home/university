#include <stdio.h>

int main(void)
{
    int USD = 0;
    double exc = 0;

    printf("USD?\n");
    scanf("%d", &USD);

    printf("원/달러 환율?\n");
    scanf("%lf", &exc);

    printf("USD %d = KRW %8.2lf", USD, USD * exc);

    return 0;
}