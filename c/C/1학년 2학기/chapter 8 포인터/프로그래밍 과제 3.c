#include <stdio.h>

int main(void)
{
    int arr[10] = {12, 54, 23, 43, 87, 31, 67, 92, 79, 7};
    int *parr = arr;

    int get_num = 0;
    printf("정수?");
    scanf("%d", &get_num);

    int i = 0;
    for (i = 0; i < sizeof(arr) / sizeof(int); i++)
    {
        arr[i] = arr[i] - get_num;
        printf(" %d", parr[i]);
    }
}