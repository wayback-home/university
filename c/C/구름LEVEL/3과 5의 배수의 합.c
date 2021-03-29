#include <stdio.h>

int main(void)
{
    int get_limit = 0;
    scanf("%d", &get_limit);

    int sum = 0;
    int sum_3 = 0;
    int sum_5 = 0;
    int sum_15 = 0;

    int i = 0;
    for (i = 0; i <= get_limit / 3; i++)
    {
        sum_3 += i * 3;
    }

    int j = 0;
    for (j = 0; j <= get_limit / 5; j++)
    {
        sum_5 += j * 5;
    }

    int k = 0;
    for (k = 0; k <= get_limit / 15; k++)
    {
        sum_15 += k * 15;
    }

    sum = sum_3 + sum_5 - sum_15;

    printf("%d", sum);
}