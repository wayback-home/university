#include <stdio.h>

int main(void)
{
    int usage = 0;
    const int fee = 190;

    printf("월 사용량(Kwh)?\n");
    scanf("%d", &usage);

    printf("전기 요금: %d원", usage * fee);

    return 0;
}