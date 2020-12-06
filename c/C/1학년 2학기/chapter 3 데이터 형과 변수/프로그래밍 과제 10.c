#include <stdio.h>

int main(void)
{
    float flo = 0;

    printf("실수?\n");
    scanf("%f", &flo);

    printf("제곱: %e\n", flo * flo);
    printf("세제곱: %e", flo * flo * flo);

    return 0;
}