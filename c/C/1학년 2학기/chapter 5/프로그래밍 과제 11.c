#include <stdio.h>

int main(void)
{
    int get = 0;
    int num = 0;
    int sum = 0;

    printf("양의 정수?");
    scanf("%d", &get);

    for (num = 2; num < get; num++)
    {
        if (get % num != 0)
            ;
        else if (get % num == 0)
        {
            sum += 1;
        }
    }
    if (sum == 0)
        printf("%d는 소수입니다.", get);
    else if (sum != 0)
        printf("%d는 소수가 아닙니다.", get);
    return 0;
}