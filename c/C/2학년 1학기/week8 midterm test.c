#include <inttypes.h>
#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>
#include <util/delay.h>

volatile unsigned char SW = 0;

ISR(INT4_vect)
{
    PORTA = 0xFF;
}
ISR(INT5_vect)
{
    PORTA = 0x00;
}
ISR(INT6_vect)
{
    SW = !SW;
    _delay_ms(100);
    EIFR = 0x40;
}
ISR(INT7_vect)
{
    PORTA = 0x00;
}

int main(void)
{
    DDRA = 0xFF;
    EIMSK = 0b00110000;
    EICRB = 0b00001111;
    SREG = 0b10000000;

    //1, 2번 (led 켜기, led 끄기:4, 5번 포트)
    while (1)
    {
        ;
    }

    //3번 (led 홀 짝 점멸:6번포트)
    while (1)
    {
        if (SW)
        {
            PORTA = 0xAA;
        }
        else
        {
            PORTA = 0x55;
        }
    }

    //4번 (LED 0.3초 간격으로 3번 점멸하기)
    int i = 0;
    for (i = 0; i < 5; i++)
    {
        PORTA = 0xFF;
        _delay_ms(300);
        PORTA = 0x00;
        _delay_ms(300);
    }

    return 0;
}
/*
21.4.13
이상적인 포트제어는 메인함수에 while만 돌리기
void형태의 함수로 만들어 제어하기

참고링크
https://webnautes.tistory.com/984

https://miobot.tistory.com/25

https://konkuk-curry.tistory.com/entry/AVR-ATmega128-Interrupt-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0


21.4.14 완성시킬예정
*/
