#include <stdio.h>

int swap_array(int *parr_a, int *parr_b)
{
    int swap[5] = {0};

    int i = 0;
    for (i = 0; i < 5; i++)
    {
        swap[i] = parr_a[i];
        parr_a[i] = parr_b[i];
        parr_b[i] = swap[i];
    }
}

int arr_print(int *arr)
{
    int i = 0;
    for (i = 0; i < 5; i++)
    {
        printf("%2d", arr[i]);
    }
    printf("\n");
}

int main(void)
{
    int arr_a[5] = {1, 3, 5, 7, 9};
    int arr_b[5] = {0, 2, 4, 6, 8};

    printf("a 배열:");
    arr_print(arr_a);
    printf("b 배열:");
    arr_print(arr_b);

    swap_array(arr_a, arr_b);

    printf("<< swap_array 호출 후 >>\n");

    printf("a 배열:");
    arr_print(arr_a);
    printf("b 배열:");
    arr_print(arr_b);
}