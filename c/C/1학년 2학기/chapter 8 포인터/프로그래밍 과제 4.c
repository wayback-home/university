#include <stdio.h>

int main(void)
{
    float get_num[5] = {0};
    float *parr = get_num;

    float num1 = 0, num2 = 0, num3 = 0, num4 = 0, num5 = 0;
    printf("실수 5개를 입력하세요:");
    scanf("%f %f %f %f %f", &num1, &num2, &num3, &num4, &num5);

    get_num[0] = num1, get_num[1] = num2, get_num[2] = num3, get_num[3] = num4, get_num[4] = num5;

    float get_sum = 0;
    int i = 0;
    for (i = 0; i < sizeof(get_num) / sizeof(float); i++)
    {
        get_sum = get_sum + parr[i];
    }
    printf("합계: %.6f", get_sum);
}