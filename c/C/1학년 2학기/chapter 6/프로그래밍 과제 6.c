#include <stdio.h>

int calcolor(int hexto10)
{
    int blue = hexto10 / 65536;
    int green = (hexto10 - (blue * 65536)) / 256;
    int red = hexto10 - blue * 65536 - green * 256;

    printf("RGB %X의 red: %d, green: %d, blue: %d", hexto10, red, green, blue);
}

int main(void)
{
    int getcolor = 0;

    printf("RGB 색상?");
    scanf("%i", &getcolor);

    calcolor(getcolor);
    return 0;
}
