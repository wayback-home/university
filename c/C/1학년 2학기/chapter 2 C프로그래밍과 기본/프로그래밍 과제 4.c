#include <stdio.h>

int main(void)
{

    int gettime;
    int getmin;
    int getsec;

    printf("시?\n");
    scanf("%d", &gettime);

    printf("분?\n");
    scanf("%d", &getmin);

    printf("초?\n");
    scanf("%d", &getsec);

    printf("입력한 시간은 %02d시 %02d분 %02d초 입니다.", gettime, getmin, getsec);

    return 0;
}