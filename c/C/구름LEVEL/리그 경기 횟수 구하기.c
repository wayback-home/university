#include <stdio.h>

int main(void)
{
    int get_team = 0;
    scanf("%d", &get_team);

    int sum = 0;
    int i = 0;
    for (i = 0; i < get_team; i++)
    {
        sum += i;
    }
    printf("%d", sum);
}