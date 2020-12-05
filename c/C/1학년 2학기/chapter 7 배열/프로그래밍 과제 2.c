#include <stdio.h>

int main(void)
{
    int get_first = 0;
    int get_ratio = 0;
    long long int sequence[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

    printf("첫 번째 항?");
    scanf("%d", &get_first);

    printf("공비?");
    scanf("%d", &get_ratio);

    sequence[0] = get_first;

    int i = 0;
    for (i = 0; i < 10; i++)
    {
        sequence[i + 1] = sequence[i] * get_ratio;
    }

    printf("등비수열 :");

    int k = 0;
    for (k = 0; k < 10; k++)
    {
        printf(" %lld", sequence[k]);
    }
}