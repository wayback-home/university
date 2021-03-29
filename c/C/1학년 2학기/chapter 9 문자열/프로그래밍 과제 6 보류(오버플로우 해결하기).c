#include <stdio.h>
#include <string.h>
#include <ctype.h>

int strcmp_ic(char *lhs, char *rhs);
int str_print(int get_return, char *lhs, char *rhs);

int main(void)
{
    char get_str1[32] = "";
    char get_str2[32] = "";

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
    for (i = 0; i < strlen(lhs); i++)
    {
        temp1[i] = tolower(lhs[i]);
    }

    int k = 0;
    for (k = 0; k < strlen(rhs); k++)
    {
        temp2[k] = tolower(rhs[k]);
    }

    get_return = strcmp(temp1, temp2);
    /* 
    if (temp1 > temp2)
    {
        get_return = 1;
    }
    else if (temp1 == temp2)
    {
        get_return = 0;
    }
    else if (temp1 < temp2)
    {
        get_return = -1;
    } */

    return get_return;
}

int str_print(int get_return, char *lhs, char *rhs)
{
    if (get_return == 0)
    {
        printf("%s == %s", lhs, rhs);
    }
    else
    {
        printf("%s != %s", lhs, rhs);
    }
}
