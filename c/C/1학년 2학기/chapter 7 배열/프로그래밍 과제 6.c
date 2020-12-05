#include <stdio.h>

int main(void)
{
    int arr[20] = {0};

    int get_num = 0;
    printf("배열의 원소에 저장할 값?");
    scanf("%d", &get_num);

    int i = 0;
    for (i = 0; i < sizeof(arr) / sizeof(int); i++)
    {
        arr[i] = get_num;
    }

    int k = 0;
    for (k = 0; k < sizeof(arr) / sizeof(int); k++)
    {
        printf(" %d", arr[k]);
    }
}
