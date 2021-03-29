#include <stdio.h>

int get_arr(int *parr, int term, int unit, int size)
{
    int i = 0;
    int k = 0;

    for (i = 0; i < size; i++)
    {
        parr[i] = term + (unit * i); //parr[i+1] = parr[i] + unit과 같이
    }                                //일반항을 사용할 경우
                                     //오버플로우 발생
    printf("등차수열:");

    for (k = 0; k < size; k++) //일반항 사용시 여기에서 오버플로우가 생긴다
    {
        printf(" %d", parr[k]);
    }
}

int main(void)
{
    int arr[10] = {0};

    int get_size = sizeof(arr) / sizeof(int);

    int get_term = 0;
    int get_unit = 0;

    printf("첫번째 항? ");
    scanf("%d", &get_term);
    printf("공차? ");
    scanf("%d", &get_unit);

    get_arr(arr, get_term, get_unit, get_size);
}