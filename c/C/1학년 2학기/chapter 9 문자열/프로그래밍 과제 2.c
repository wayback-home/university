#include <stdio.h>

int main(void)
{
    char name_1[10] = "";
    char name_2[10] = "";
    char name_3[10] = "";

    printf("영문 이름? ");
    scanf("%s %s %s", name_1, name_2, name_3);

    char name_11;
    char name_22;
    char name_33;

    name_11 = name_1[0];
    name_22 = name_2[0];
    name_33 = name_3[0];

    printf("%c", name_11);
    printf("%c", name_22);
    printf("%c", name_33);
}

//나중에 토큰을 이용해 나누는 기능 사용해보기