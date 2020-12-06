#include <stdio.h>

int main(void)
{
    float arr[10] = {0.10, 2.00, 3.40, 5.20, 4.50, 7.80, 9.70, 1.40, 6.60, 7.20};
    float *parr;

    int i = 0;

    for (i = 0; i < sizeof(arr) / sizeof(float); i++)
    {
        parr = &arr[i];
        printf("%3.2f ", *parr);
    }
}