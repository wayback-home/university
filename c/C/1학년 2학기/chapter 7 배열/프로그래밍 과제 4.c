#include <stdio.h>

int main(void)
{
    int arr[10] = {23, 45, 62, 12, 99, 83, 23, 50, 12, 37};
    int find_num = 0;
    int place_num = 0;

    printf("찾을값?");
    scanf("%d", &find_num);

    int i = 0;
    for (i = 0; i < 10; i++)
    {
        if (arr[i] == find_num)
        {
            place_num = i + 1;
            break;
        }
    }
    if (place_num == 0)
    {
        printf("찾는 원소는 배열에 없습니다.\n");
    }
    else
    {
        printf("%d는 %d번째 원소입니다.", find_num, place_num);
    }
}