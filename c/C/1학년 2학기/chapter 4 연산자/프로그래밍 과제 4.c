#include <stdio.h>

int main(void)
{
    int month = 0;

    printf("몇 월?\n");
    scanf("%d", &month);

    if (month <= 12)
        if (month >= 1)
            printf("올바른 값입니다.\n");
        else
            printf("잘못된 값입니다.\n");
    else
        printf("잘못된 값입니다.\n");

    return 0;
}