#include <stdio.h>

int main(void)
{
    char get_seat[10] = {"OOOOOOOOOO"};
    int get_pas = 0; //예매할 좌석 수

    while (1)
    {

        printf("현재 좌석 : [ ");

        int i = 0;
        for (i = 0; i < 10; i++)
        {
            printf("%c ", get_seat[i]);
        }
        printf("]\n");

        printf("예매할 좌석수? ");
        scanf("%d", &get_pas);

        int k = 0;
        int verify = 0; //현재 예매된 좌석 수
        for (k = 0; k < 10; k++)
        {
            if (get_seat[k] == 'X')
            {
                verify++;
            }
        }

        int j = 0;
        if (10 - verify < get_pas)
        {
            printf("남은 좌석수가 %d이므로 %d좌석을 예매할 수 없습니다.", 10 - verify, get_pas);
            break;
        }
        else
        {
            for (j = verify; j < verify + get_pas; j++)
            {
                get_seat[j] = 'X';
            }
        }
    }
}