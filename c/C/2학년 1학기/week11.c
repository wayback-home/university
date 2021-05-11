#include <inttypes.h>
#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>
#include <stdio.h>

volatile unsigned char a = 0;

SIGNAL(SIG_OVERFLOW0)
{
    TCNT0 = 100;
    if (a == 0)
        a = 0xFF;
    else
        a = 0;
}

int main(void)
{
    DDRD = 0xFF;
    TCCR0 = 0x07; //1024분주
    TIMSK = 0x01; //overflow interrupt
    TCNT0 = 100;
    sei();
    while (1)
    {
        PORTD = a;
    }
    return 0;
}