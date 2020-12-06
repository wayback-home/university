#include <stdio.h>

int main(void)
{
    double arr[3];

    int i = 0;
    for (i = 0; i < sizeof(arr) / sizeof(double); i++)
    {
        printf("x[%d]의 주소 :", i);
        printf(" %p\n", &arr[i]);
    }
}