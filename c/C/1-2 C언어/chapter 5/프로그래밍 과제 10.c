#include <stdio.h>

#include <stdio.h>

int main(void)
{
    int monuse = 0;
    int deffee = 0;
    int fee = 0;

    printf("월 사용량 (kwh)?");
    scanf("%d", &monuse);

    while (monuse != 0)
    {
        if (monuse <= 300)
        {
            deffee = 1000;
            fee = monuse * 100;
        }
        else
        {
            deffee = 5000;
            fee = (monuse - 300) * 200 + 30000;
        }

        printf("전기 요금 합계: %d\n  - 기본요금:    %d\n  - 전력량요금: %d\n", deffee + fee, deffee, fee);
        printf("월 사용량 (kwh)?");
        scanf("%d", &monuse);
        continue;
    }

    return 0;
}