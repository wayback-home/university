#include <stdio.h>
#include <string.h>

char contrastWord(char reverse)
{
    //나중에 작성 예정
    //반복문을 이용해서 문자열을 뒤집게 설정
    int i = 0;
    char reverseWord[sizeof(reverse)];

    for (i = 0; i < sizeof(reverse); i++)
    {
        reverseWord[sizeof(reverse) - i] = reverse[i];
    }
}

int main(void)
{

    int len = 0;
    char getWord[16];

    printf("문자열?");
    fgets(getWord, sizeof(getWord), stdin);

    len = strlen(getWord);

    contrastWord(getWord);

    /*
    printf("역순으로 된 문자열 : %s", )
*/
    return 0;
}