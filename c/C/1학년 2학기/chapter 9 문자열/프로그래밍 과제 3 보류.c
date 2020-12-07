#include <stdio.h>
#include <string.h>

int main(void)
{
    char c_arr[128] = "";

    printf("문자열? ");
    fgets(c_arr, sizeof(c_arr), stdin);

    int sum = strlen(c_arr);

    int i = 0;
    int sum_exist = 0;
    for (i = 0; i < sum; i++)
    {
        if (c_arr[i] == ',')
        {
            sum_exist++;
        }
        else if (c_arr[i] == '.')
        {
            sum_exist++;
        }
        else if (c_arr[i] = ' ') //공백 개수가 아닌 전체 문자열 개수를 세는 오류 발생
        {
            sum_exist++;
        }
    }
    printf("영문자의 개수 : %d", sum - sum_exist);
}