#include <stdio.h>
#include <string.h>
#include <ctype.h>

int strcmp_ic(char *lhs, char *rhs);
int str_print(int get_return, char *lhs, char *rhs);

int main(void)
{
    char get_str1[128] = "";
    char get_str2[128] = "";

    printf("첫 번째 문자열 ? ");
    fgets(get_str1, sizeof(get_str1), stdin);
    printf("두 번째 문자열 ? ");
    fgets(get_str2, sizeof(get_str2), stdin);

    strcmp_ic(get_str1, get_str2);
}

int strcmp_ic(char *lhs, char *rhs)
{

    int get_return = 0;

    char temp1[sizeof(lhs)] = "";
    char temp2[sizeof(rhs)] = "";

    int i = 0;
    for (i = 0; i < sizeof(lhs); i++)
    {
        temp1[i] = tolower(lhs[i]);
        temp2[i] = tolower(rhs[i]);
    }

    if (temp1 > temp2)
    {
        get_return = 1;
    }
    else if (temp1 == temp2)
    {
        get_return = 0;
    }
    else
    {
        get_return = -1;
    }

    return get_return;
}

int str_print(int get_return, char *lhs, char *rhs)
{
    if (get_return == 1;)
    {
    }
}