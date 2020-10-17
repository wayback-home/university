#include <stdio.h>

int main(void)
{
    int beatA = 0;
    int beatB = 0;
    char cal;

    printf("비트 연산식?");
    scanf("%i %c %i", &beatA, &cal, &beatB);

    if (cal == '&')
        printf("%X & %X = %X", beatA, beatB, beatA & beatB);
    else if (cal == '^')
        printf("%X ^ %X = %X", beatA, beatB, beatA ^ beatB);
    else if (cal == '|')
        printf("%X | %X = %X", beatA, beatB, beatA | beatB);

    return 0;
}