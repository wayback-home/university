#include <stdio.h>

int main(void)
{
    double arr[5] = {0};
    double num1 = 0, num2 = 0, num3 = 0, num4 = 0, num5 = 0;

    printf("실수 5개를 입력하세요:");
    scanf("%lf %lf %lf %lf %lf", &num1, &num2, &num3, &num4, &num5);

    arr[0] = num1;
    arr[1] = num2;
    arr[2] = num3;
    arr[3] = num4;
    arr[4] = num5;

    int i = 0;
    double get_sum = 0;
    for (i = 0; i < sizeof(arr) / sizeof(double); i++)
    {
        get_sum = get_sum + arr[i];
    }
    printf("합계 : %lf", get_sum);
}