#include <stdio.h>

int printrec(int wid, int hei)
{
    int rec = (wid * 2) + (hei * 2);
    printf("직사각형의 둘레: %d", rec);
}

int main(void)
{
    int width = 0;
    int height = 0;

    printf("가로?");
    scanf("%d", &width);

    printf("세로?");
    scanf("%d", &height);

    printrec(width, height);
}