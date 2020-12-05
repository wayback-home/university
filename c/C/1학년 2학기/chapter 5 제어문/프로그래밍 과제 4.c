#include <stdio.h>

int main(void)
{
    int getYear = 0;

    printf("연도?");
    scanf("%d", &getYear);

    if (getYear % 4 == 0)
        if (getYear % 100 == 0)
            if (getYear % 400 == 0)
                printf("%d년은 윤년입니다.", getYear);
            else
            {
                printf("%d년은 윤년이 아닙니다.", getYear);
            }

        else
        {
            printf("%d년은 윤년입니다.", getYear);
        }

    else
    {
        printf("%d년은 윤년이 아닙니다.", getYear);
    }
}