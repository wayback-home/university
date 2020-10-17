#include <stdio.h>

int main(void)
{
    int price = 0;
    int dis = 0;

    printf("제품의 가격?\n");
    scanf("%d", &price);

    printf("할인율(%%)?");
    scanf("%d", &dis);

    printf("할인가: %d원 (%d원 할인)", price * (100 - dis) / 100, price * dis / 100);

    return 0;
}