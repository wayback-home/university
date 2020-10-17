#include <stdio.h>

int main(void)
{
    float pi = 3.14159265;

    printf("pi = %3.2f\n", pi);
    printf("pi = %5.4f\n", pi);
    printf("pi = %7.6f\n", pi);
    printf("pi = %9.8f\n", pi);
    printf("pi = %e", pi);

    return 0;
}