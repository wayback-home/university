#include <stdio.h>

void print_arr(int def[][])
{
    int i = 0;
    int k = 0;

    for (i = 0; i < 3; i++)
    {
        for (k = 0; k < 3; k++)
        {
            printf(" %d", def[i][k]);
        }
        printf("\n");
    }
}

int main(void)
{
    int arrx[3][3] = {{10, 20, 30}, {40, 50, 60}, {70, 80, 90}};
    int arry[3][3] = {{9, 8, 7}, {6, 5, 4}, {3, 2, 1}};
    int sum[3][3] = {{0}, {0}, {0}};

    int i = 0;
    int k = 0;

    for (i = 0; i < 3; i++)
    {
        for (k = 0; k < 3; k++)
        {
            sum[i][k] = arrx[i][k] + arry[i][k];
        }
    }

    printf("x 행렬:\n");
    print_arr(arrx);

    printf("y 행렬:\n");
    print_arr(arry);

    printf("x + y 행렬 :\n");
    print_arr(sum);
}