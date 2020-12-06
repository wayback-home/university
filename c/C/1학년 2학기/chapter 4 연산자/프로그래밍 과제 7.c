#include <stdio.h>

int main(void)
{
    float solvent = 0;
    float solute = 0;

    printf("용매(g)\n");
    scanf("%f", &solvent);
    printf("용질(g)\n");
    scanf("%f", &solute);

    float con = solute * 100 / (solvent + solute);

    printf("농도 : %4.2f %%", con);

    return 0;
}