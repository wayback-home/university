#include <stdio.h>

int main(void)
{
    int getnum;

    printf("8진수로 입력하려면 012, 16진수로 입력하려면 0x12처럼 입력하세요.\n정수?");
    scanf("%i", &getnum);

    printf("8진수  : 0%o\n10진수 : %d\n16진수 : 0x%x", getnum, getnum, getnum);

    return 0;
}