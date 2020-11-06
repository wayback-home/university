#include <stdio.h>

int main(void)
{
    int rank = 0;
    int totalPeople = 0;

    printf("등수?");
    scanf("%d", &rank);

    printf("전체 인원수?");
    scanf("%d", &totalPeople);

    int percent = rank * 100 / totalPeople;

    printf("학점 :");
    if (percent <= 10)
        printf("A");
    else if (percent <= 30)
        printf("B");
    else if (percent <= 60)
        printf("C");
    else if (percent <= 90)
        printf("D");
    else
    {
        printf("F");
    }

    return 0;
}