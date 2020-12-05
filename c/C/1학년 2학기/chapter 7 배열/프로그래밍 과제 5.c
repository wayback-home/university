#include <stdio.h>

int main(void)
{
    double arr[10] = {1.2, 3.1, 4.3, 4.5, 6.7, 2.3, 8.7, 9.5, 2.3, 5.8};

    printf("배열:");

    int i = 0;
    for (i = 0; i < 10; i++)
    {
        printf("%2.1lf ", arr[i]);
    }

    printf("\n역순:");

    int k = 0;
    for (k = 9; k >= 0; k--)
    {
        printf("%2.1lf ", arr[k]);
    }
}