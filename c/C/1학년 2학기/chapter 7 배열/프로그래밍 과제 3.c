#include <stdio.h>

int main(void)
{
    int arr[10] = {23, 45, 62, 12, 99, 83, 23, 50, 72, 37};
    int max = 0;
    int min = 99;

    int i = 0;
    for (i = 0; i < 10; i++)
    {
        if (max <= arr[i])
        {
            max = arr[i];
        }
    }

    for (i = 0; i < 10; i++)
    {
        if (min >= arr[i])
        {
            min = arr[i];
        }
    }

    printf("최댓값 : %d\n", max);
    printf("최솟값 : %d", min);
}