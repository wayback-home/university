#include <stdio.h>

int main()
{
    int age;
    float height;
    float weight;

    printf("나이, 키, 몸무게를 입력하세요 :");
    scanf("%d %f %f", &age, &height, &weight);
    //#define _CRT_SECURE_NO_WARINGS를 정의하지 않았는데도 오류가 뜨지 않았음. 리눅스 환경이라 가능한건지는 의문

    printf("나이   : %5d\n", age);
    printf("키     : %5.1f\n", height);
    printf("몸무게 : %5.1f\n", weight);
    /*
    printf("나이   : %5d\n키     : %5.1f\n몸무게 : %5.1f\n", age, height, weight); //예제와 별개로 한번에 쓰는것도 가능함
    */
    return 0;
}