#include <inttypes.h>
#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>
#include <util/delay.h>
#include <stdio.h>

// 7 segment//
void interrupt_call(int);
int num = 0;
char seg_data[10] = {0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7f, 0x6f}; // 0~9

ISR(TIMER0_OVF_vect)
{
    interrupt_call(num);
    num++;
    if (num == 10)
        num = 0;
}

int main()
{
    DDRB = 0xff; // 방향출력설정 PORTB
    DDRF = 0x10; // 방향출력설정 PORTF
    TIMSK = 1;   // TOIE0 = 1
    TCCR0 = 7;   // normal mode, CS02 CS01 CS00 = 1024분주
    TCNT0 = 0;   // 초기값 0
    SREG = 0x80; // 인터럽트 허용

    while (1)
    {
        ;
    }
    return 0;
}

void interrupt_call(int num)
{ // 함수 정의
    int i;
    for (i = 0; i < 10; i++)
    {
        PORTF = 0b1111000;
        PORTB = seg_data[num];
        _delay_ms(100);
        PORTF = 0b11110000;
        _delay_ms(100);
    }
}