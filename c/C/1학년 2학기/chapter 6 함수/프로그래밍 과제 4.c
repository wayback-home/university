#include <stdio.h>

int calprice(int discount, int price)
{
    printf("할인가: %d원\n", price * (100 - discount) / 100);
}

int main(void)
{
    int getdiscount = 0;
    int getprice;

    printf("할인율(%%)?");
    scanf("%d", &getdiscount);

    while (getprice != 0)
    {

        printf("제품의 가격?");
        scanf("%d", &getprice);
        if (getprice != 0)
        {
            calprice(getdiscount, getprice);
        }

        continue;

        return 0;
    }
}