#include <stdio.h>

int main(void)
{
    int get_first = 0;
    int get_unit = 0;
    int sequence[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

    printf("첫 번째 항?");
    scanf("%d", &get_first);

    printf("공차?");
    scanf("%d", &get_unit);

    int i = 0;
    for (i = 0; i < 10; i++)
    {
        sequence[i] = get_first + (get_unit * i);
    }

    printf("등차수열:");

    int k = 0;
    for (k = 0; k < 10; k++)
    {
        printf(" %d", sequence[k]);
    }
}