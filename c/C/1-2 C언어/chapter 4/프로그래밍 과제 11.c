#include <stdio.h>

int main(void)
{
    int red = 0;
    int green = 0;
    int blue = 0;

    printf("red?");
    scanf("%d", &red);

    printf("green?");
    scanf("%d", &green);

    printf("blue?");
    scanf("%d", &blue);

    if (red > 255)
        red = 0;
    if (green > 255)
        green = 0;
    if (blue > 255)
        blue = 0;

    printf("RGB 색상: %02X%02X%02X", blue, green, red);

    return 0;
}