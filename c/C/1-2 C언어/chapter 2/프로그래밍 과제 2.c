#include <stdio.h>

int main(void)
{
    int getinteger;
    printf("10진수 정수?");
    scanf("%d", &getinteger); //변수 이름에 &꼭 붙이기

    printf("10진수 정수 %d는 16진수 정수 %X에 해당합니다.", getinteger, getinteger);

    return 0;
}