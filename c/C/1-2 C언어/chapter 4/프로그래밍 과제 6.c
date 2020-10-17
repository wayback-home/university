#include <stdio.h>

int main(void)
{
    float kg = 0;
    float ms = 0;

    printf("질량(kg)?\n");
    scanf("%f", &kg);
    printf("속력(m/s)\n");
    scanf("%f", &ms);

    float energy = kg * ms * ms / 2;

    printf("운동에너지: %4.2f J\n", energy);

    return 0;
}