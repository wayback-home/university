#include <stdio.h>

int find_num(int *parr, int key, int size)
{
    int i = 0;
    int sum = 0;
    for (i = 0; i < size; i++)
    {
        if (parr[i] == key)
        {
            sum++;
        }
    }
    return sum;
}

int find_index(int *parr, int key, int size)
{
    int index[size];
    int repeat = 0;
    for (repeat = 0; repeat < size; repeat++)
    {
        index[repeat] = -1;
    }

    int stop = 0;

    int i = 0;
    int k = 0;
    for (i = 0; i < size; i++)
    {
        if (parr[i] == key)
        {
            index[k] = i;
            k++;
        }
    }

    int j = 0;
    for (j = 0; j < size; j++)
    {
        if (index[j] == -1)
        {
            stop = j - 1;
            break;
        }
    }

    if (stop != -1)
    {
        printf("찾은 항목의 인덱스:");
        int l = 0;
        for (l = 0; l < stop + 1; l++)
        {
            printf(" %d", index[l]);
        }
    }
    else
    {
        return 0;
    }
}

int main(void)
{
    int arr[] = {12, 45, 62, 12, 99, 83, 23, 12, 72, 37};
    int get_key = 0;
    int get_size = 0;

    get_size = sizeof(arr) / sizeof(int);

    printf("찾을 값? ");
    scanf("%d", &get_key);

    printf("찾은 항목은 모두 %d개 입니다.\n", find_num(arr, get_key, get_size));
    find_index(arr, get_key, get_size);
}