#include <stdio.h>

int main(void)
{
    long long int arr[20] = {0};

    int get_num = 0;
    printf("배열의 원소에 저장할 값?");
    scanf("%d", &get_num);

    int i = 0;
    for (i = 0; i < sizeof(arr); i++)
    {
        arr[i] = get_num;
    }

    int k = 0;
    for (k = 0; k < sizeof(arr); k++)
    {
        printf("%lld", arr[k]);
    }
}
