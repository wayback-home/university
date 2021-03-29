//2행을 3행으로 바꾸는 함수 보류

#include <stdio.h>

int arr_func(int (*parr)[5], int data, int line, int row)
{
    int i = 0;
    int k = 0;
    for (i = 0; i < line; i++)
    {
        for (k = 0; k < row; k++)
        {
            parr[i][k] = data;
            printf(" %d", parr[i][k]);
        }
        printf("\n");
    }
}

int main(void)
{
    int get_data = 0;

    int arr[2][5] = {0};

    printf("배열의 원소에 저장할 값?");
    scanf("%d", &get_data);

    int size_line = sizeof(arr) / sizeof(arr[0]);
    int size_row = sizeof(arr[0]) / sizeof(int);

    arr_func(arr, get_data, size_line, size_row);
}