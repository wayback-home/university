#include <stdio.h>

int main(void)
{
    int getLine = 0;

    printf("한 변의 길이?\n");
    scanf("%d", &getLine);

    printf("정사각형의 넓이 : %d\n", getLine * getLine);
    printf("정사각형의 둘레 : %d\n", getLine * 4);

    return 0;
}