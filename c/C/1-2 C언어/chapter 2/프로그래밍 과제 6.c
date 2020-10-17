#include <stdio.h>

int main(void)
{
    char getsize;
    printf("옷 사이즈(S,M,L)");
    scanf("%c", &getsize);

    printf("%c 사이즈를 선택했습니다.", getsize);

    return 0;
}