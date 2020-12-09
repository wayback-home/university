#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int judg_time(char *time);

int main(void)
{
    char get_time[7] = "";

    printf("시간(.입력 시 종료)? ");
    fgets(get_time, sizeof(get_time), stdin);

    judge_time(get_time);
}

int judge_time(char *time)
{
    if (time[0] == '.')
    {
        return 0;
    }
    int get_time[6] = {0};

    int k = 0;
    for (k = 0; k < strlen(time); k++)
    {
        get_time[k] = time[k];
    }

    int hour[2] = {0};
    int min[2] = {0};
    int sec[2] = {0};

    int i = 0;
    for (i = 0; i < sizeof(get_time) / sizeof(int); i++)
    {
        if (i <= 1)
        {
            hour[i] = get_time[i];
        }
        else if (i > 1 && i <= 3)
        {
            min[i - 2] = get_time[i];
        }
        else if (i > 3)
        {
            sec[i - 4] = get_time[i];
        }
    }

    int get_hour = 0;
    int get_min = 0;
    int get_sec = 0;

    int j = 0;
    for (j = 0; j < 2; j++)
    {
        if (j == 0)
        {
            get_hour = (hour[j] - 48) * 10;
            get_min = (min[j] - 48) * 10;
            get_sec = (sec[j] - 48) * 10;
        }
        else if (j == 1)
        {
            get_hour = get_hour + (hour[j] - 48);
            get_min = get_min + (min[j] - 48);
            get_sec = get_sec + (sec[j] - 48);
        }
    }

    if (get_hour > 24 || get_min > 60 || get_sec > 60)
    {
        printf("잘못 입력했습니다. hhmmss형식으로 입력하세요.");
    }
    else
    {
        printf("%d:%d:%d는 유효한 시간입니다.", get_hour, get_min, get_sec);
    }
}