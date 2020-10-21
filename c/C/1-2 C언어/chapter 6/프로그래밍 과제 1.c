#include <stdio.h>

int multi(int num)
{
    if (num > 0)
    {
        int i = 0;
        for (i = 1; i < 21; i++)
        {
            printf("%d ", num * i);
        }
    }
    else if (num <= 0)
    {
        ;
    }
}

int main(void)
{
    int integer = 0;

    printf("정수?");
    scanf("%d", &integer);

    multi(integer);

    return 0;
}