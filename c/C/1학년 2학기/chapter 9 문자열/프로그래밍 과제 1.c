#include <stdio.h>

int main(void)
{
    char get_name[128] = "";
    char get_extension[128] = "";

    printf("파일명? ");
    scanf("%s", get_name);
    printf("확장자? ");
    scanf("%s", get_extension);

    printf("전체 파일명 :");
    printf("%s", get_name);
    printf(".");
    printf("%s", get_extension);
}