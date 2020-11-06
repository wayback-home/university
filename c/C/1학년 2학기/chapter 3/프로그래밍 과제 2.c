#include <stdio.h>

int main(void)
{
    int wid = 0;
    int hei = 0;

    printf("가로의 길이?\n");
    scanf("%d", &wid);
    printf("세로의 길이?\n");
    scanf("%d", &hei);
    printf("직사각형의 넓이 : %d\n직사각형의 둘레 : %d", wid * hei, 2 * (wid + hei));

    return 0;
}