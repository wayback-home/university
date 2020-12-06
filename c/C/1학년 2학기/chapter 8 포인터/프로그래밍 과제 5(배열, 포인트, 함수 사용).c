#include <stdio.h>

int get_min_max(int *parr, int select)
{
    int max = 0;
    int min = 99;

    int i = 0;
    if (select == 0) //select가 0일경우 max값 산출
    {
        for (i = 0; i < 10; i++)
        {
            if (max <= parr[i])
            {
                max = parr[i];
            }
        }
        return max;
    }

    else //select가 0이 아닐 경우 min값 산출
    {
        for (i = 0; i < 10; i++)
        {
            if (min >= parr[i])
            {
                min = parr[i];
            }
        }
        return min;
    }
}

int main(void)
{
    int arr[10] = {23, 45, 62, 12, 99, 83, 23, 50, 72, 37};
    int max = get_min_max(arr, 0);
    int min = get_min_max(arr, 1);

    printf("최대값: %d\n", max);
    printf("최소값: %d", min);
}
