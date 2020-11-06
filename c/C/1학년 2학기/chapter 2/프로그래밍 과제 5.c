#include<stdio.h>

int main(void)
{
    float getdollor;
    int printwon;


    printf("달러?\n");
    scanf("%f", &getdollor);

    printwon = getdollor * 1000;

    printf("$%4.2f는 %d원입니다.",getdollor, printwon);

    return 0;
}