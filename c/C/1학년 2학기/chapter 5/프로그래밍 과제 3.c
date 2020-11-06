#include <stdio.h>

int main(void)
{
    int x = 0;
    int y = 0;

    printf("점의 좌표 (x, y)?");
    scanf("%d %d", &x, &y);

    if (x > 0)
        if (y < 0)
            printf("4사분면에 있습니다.");
        else
            printf("1사분면에 있습니다.");
    if (x < 0)
        if (y < 0)
            printf("3사분면에 있습니다.");
        else
            printf("2사분면에 있습니다.");

    return 0;
}