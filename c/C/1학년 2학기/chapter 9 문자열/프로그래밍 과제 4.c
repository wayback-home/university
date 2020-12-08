#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    char str[128] = "";

    printf("문자열? ");
    fgets(str, sizeof(str), stdin);

    int i = 0;
    char dis_str = ' ';
    for (i = 0; i < sizeof(str); i++)
    {
        dis_str = str[i];
        if (isupper(dis_str) >= 1)
        {
            str[i] = tolower(dis_str);
        }
        else if (islower(dis_str) >= 1)
        {
            str[i] = toupper(dis_str);
        }
        else
        {
            continue;
        }
    }
    puts(str);
}