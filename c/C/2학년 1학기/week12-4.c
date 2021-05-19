#include <inttypes.h>
#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>
#include <util/delay.h>
#include <stdio.h>

char seg[10] = {0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7f, 0x6f}; // 0~9

int n1 = 0, n10 = 0, num = 0, i;
char led = 0xFE;

ISR(TIMER0_OVF_vect)
{
    num++;
    n1 = num % 10;
    n10 = num / 10;
    for (i = 0; i < 20; i++)
    {
        PORTE = 0x00;
        PORTF = seg[n10];
        PORTB = seg[n1];
        _delay_ms(100);
        PORTE = 0xFF;
        PORTF = seg[n10];
        PORTB = seg[n1];
        if (num > 99)
            num = 0;
        _delay_ms(100);
    }
    led = (led << 1) | 0x01;
    if (led = 0xFF)
        led = 0xFE;
    PORTC = led;
}

int main()
{
    DDRB = 0xFF; // 방향출력설정 PORTB
    DDRF = 0xFF; // 방향출력설정 PORTF
    DDRC = 0xFF;
    DDRE = 0xFF;
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
