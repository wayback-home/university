/* 
컴퓨터정보기술공학부
1826052 최영서
C언어 10주차 과제
*/
#include <stdio.h>
#include <string.h>

void main()
{
    int i, k;
    char str[30];
    printf("문자열?");
    fgets(str, sizeof(str), stdin);

    k = strlen(str);

    printf("역순으로 된 문자열:");

    for (i = k - 1; i >= 0; i--)
    {
        printf("%c", str[i]);
    }
}
