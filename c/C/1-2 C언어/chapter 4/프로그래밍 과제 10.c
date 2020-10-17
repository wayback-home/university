#include <stdio.h>

int main(void)
{
    int getData = 0;

    printf("16진수로 데이터를 입력하세요 : \n");
    scanf("%i", &getData);

    unsigned int byte0 = 0x000000ff;
    unsigned int byte1 = 0x0000ff00;
    unsigned int byte2 = 0x00ff0000;
    unsigned int byte3 = 0xff000000;

    printf("byte 0 : %x\n", getData & byte0);
    printf("byte 1 : %x\n", ((getData & byte1) >> 8));
    printf("byte 2 : %x\n", ((getData & byte2) >> 16));
    printf("byte 3 : %x", ((getData & byte3) >> 24));

    return 0;
}