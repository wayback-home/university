#include <stdio.h>

int main(void)
{
    float mm2 = 0;
    float exc = 0.3025;

    printf("아파트의 면적(제곱미터)?\n");
    scanf("%f", &mm2);

    printf("%5.2f 제곱미터 = %4.2f 평\n", mm2, mm2 * exc);

    return 0;
}