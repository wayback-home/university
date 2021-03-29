#include <stdio.h>

int main(void)
{
    float Ftem = 0;
    float Ctem = 0;

    printf("화씨온도?\n");
    scanf("%f", &Ftem);

    Ctem = (Ftem - 32) * 5 / 9;

    printf("%2.0f F = %4.2f C\n", Ftem, Ctem);

    return 0;
}