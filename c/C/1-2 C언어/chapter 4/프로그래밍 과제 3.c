#include <stdio.h>

int main(void)
{
    int defaultfee = 2500;
    int usage = 0;
    const int fee = 190;

    printf("기본 요금?\n");
    scanf("%d", &defaultfee);

    printf("월 사용량(kwh)?\n");
    scanf("%d", &usage);

    printf("전기 요금: %d원", usage * fee + defaultfee);

    return 0;
}