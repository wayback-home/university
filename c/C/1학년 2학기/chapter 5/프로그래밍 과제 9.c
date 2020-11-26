#include <stdio.h>

int main(void)
{
    int integer = 0;
    int count = 0;
    int i = 0;

    printf("양의 정수?");
    scanf("%d", &integer);
    printf("배수의 개수?");
    scanf("%d", &count);

    for (i = 0; i < count; i++)
    {
        printf("%d ", integer * (i + 1));
    }
    return 0;
}