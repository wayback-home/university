#include <stdio.h>
#include <string.h>
#include <ctype.h>

int encoding(char *password, int key);

int main(void)
{
    char get_password[32] = "";
    int get_key = 0;

    printf("문자열? ");
    fgets(get_password, sizeof(get_password), stdin);
    printf("암호 키(정수)? ");
    scanf("%d", &get_key);

    encoding(get_password, get_key);
}

int encoding(char *password, int key)
{
    int length = strlen(password);
    char encoding_password[length];

    int i = 0;
    for (i = 0; i < strlen(password); i++)
    {
        encoding_password[i] = password[i] + key;
    }
    printf("암호화된 문자열: %s", encoding_password);
}
