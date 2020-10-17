#include <stdio.h>

int main(void)
{
    double kg = 0;
    double m = 0;

    printf("질량(kg)?\n");
    scanf("%lf", &kg);

    printf("높이(m)?\n");
    scanf("%lf", &m);

    printf("위치에너지 : %5.2lfJ", 9.8 * kg * m);

    return 0;
}