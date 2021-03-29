#include <stdio.h>

int arr_print(int *arr, int size)
{
    int i = 0;
    for (i = 0; i < size; i++)
    {
        printf(" %d", arr[i]);
    }
}

int line_up(int *arr, int size)
{
    int i = 0;
    int k = 0;
    int temp = 0;
    int min = 99;

    for (i = 0; i < size; i++)
    {
        for (k = i; k < size; k++)
        {
            if (min >= arr[k])
            {
                min = arr[k];
                temp = k;
            }
        }
        arr[temp] = arr[i];
        arr[i] = min;
        min = 99;
    }
}

int main(void)
{
    int get_arr[10] = {92, 34, 76, 32, 15, 28, 41, 55, 89, 62};
    int get_size = sizeof(get_arr) / sizeof(int);

    printf("정렬 전:");
    arr_print(get_arr, get_size);

    printf("\n");

    line_up(get_arr, get_size);

    printf("정렬 후:");
    arr_print(get_arr, get_size);
}