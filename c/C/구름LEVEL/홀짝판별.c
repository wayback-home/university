#include <stdio.h>

int main(void)
{
    int get_num = 0;

    scanf("%d", &get_num);
    if (get_num % 2 == 0)
    {
        printf("even");
    }
    else
    {
        printf("odd");
    }
}