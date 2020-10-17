#include<stdio.h>

int main(void)
{
    int year;
    int month;
    int day;

    printf("연?\n");
    scanf("%d", &year); 

    printf("월?\n");
    scanf("%d", &month);  

    printf("일?\n");
    scanf("%d", &day);

    printf("입력한 날짜는 %d년 %d월 %d일 입니다.", year, month, day);

    return 0;


}