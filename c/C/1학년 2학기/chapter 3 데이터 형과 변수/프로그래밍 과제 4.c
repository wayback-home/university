#include <stdio.h>

int main(void)
{
    double wid = 0;
    double hei = 0;

    printf("밑변과 높이?\n");
    scanf("%lf %lf", &wid, &hei);

    printf("직각삼각형의 면적 : %4.2lf", (wid * hei) / 2);

    return 0;
}