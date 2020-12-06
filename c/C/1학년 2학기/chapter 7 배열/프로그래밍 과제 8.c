#include <stdio.h>

int main(void)
{
    int arr[5] = {0};
    int sale_price0 = 0, sale_price1 = 0, sale_price2 = 0, sale_price3 = 0, sale_price4 = 0;
    int sale_per = 0;

    printf("상품가 5개를 입력하세요:");
    scanf("%d %d %d %d %d", &sale_price0, &sale_price1, &sale_price2, &sale_price3, &sale_price4);
    printf("할인율(%%)?");
    scanf("%d", &sale_per);

    arr[0] = sale_price0;
    arr[1] = sale_price1;
    arr[2] = sale_price2;
    arr[3] = sale_price3;
    arr[4] = sale_price4;

    int i = 0;
    for (i = 0; i < sizeof(arr) / sizeof(int); i++)
    {
        printf("가격:    %5d -->  할인가:    %d\n", arr[i], arr[i] * (100 - sale_per) / 100);
    }
}