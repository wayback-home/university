#include <inttypes.h>
#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>
#include <util/delay.h>
#include <stdio.h>

void interrupt_call(int);
int num = 0;
char seg_data[10] = {0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F};

ISR(TIMER0_COMP_vect)
{
    interrupt_call(num);
    num++;
    if (num == 10)
        num = 0;
}

int main()
{
    DDRA = 0xFF;
    DDRF = 0x10;
    TIMSK = 0x02;
    TCCR0 = 0x0E;
    TCNT0 = 0;
    OCR0 = 250;
    SREG = 0x80;
    while (1)
    {
        ;
    }
    return 0;
}

void interrupt_call(int num)
{
    int i;
    for (i = 0; i < 10; i++)
    {
        PORTF = 0b11100000;
        PORTA = seg_data[num];
        _delay_ms(100);
        PORTF = 0b11110000;
        _delay_ms(100);
    }
}