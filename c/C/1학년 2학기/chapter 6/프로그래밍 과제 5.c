#include <stdio.h>

int setmenu(int menu)
{
    switch (menu)
    {
    case 1:
        printf("파일 열기를 수행합니다.\n");
        break;
    case 2:
        printf("파일 저장을 수행합니다.\n");
        break;
    case 3:
        printf("인쇄를 수행합니다.\n");
        break;
    case 4:
        printf("종료합니다.\n");
        break;

    default:
        break;
    }
}

int main(void)
{
    int select = 0;
    while (select != 4)
    {
        printf("[1.파일 열기  2.파일 저장  3.인쇄  0.종료] 선택?");
        scanf("%d", &select);
        if (select >= 4)
        {
            printf("잘못 입력하셨습니다.");
            break;
        }
        else if (select == 0)
        {
            select += 4;
        }
        setmenu(select);

        continue;
    }

    return 0;
}