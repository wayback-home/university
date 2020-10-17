#include <stdio.h>

int main(void)
{
    int time = 0;

    printf("재생 시간(초)?\n");
    scanf("%d", &time);

    int hour = time / 3600;
    int min = (time - 3600 * hour) / 60;
    int sec = time - 3600 * hour - 60 * min;

    if (hour != 0)
        printf("%d시간 ", hour);
    if (min != 0)
        printf("%d분 ", min);
    if (sec != 0)
        printf("%d초", sec);
    printf("입니다.");

    return 0;
}