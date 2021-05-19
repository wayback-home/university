#include <inttypes.h>
#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>
#include <stdio.h>
#include <util/delay.h>

unsigned char led = 0xFE;

ISR(TIMER0_OVF_vect)
{
    led <<= 1;
    led |= 1;
    if (led == 0xFF)
        led = 0xFE;
    PORTC = led;
}

int main()
{
    DDRC = 0xFF;
    PORTC = led;

    TCNT0 = 0;
    TIMSK = 1;
    TCCR0 = 7;
    SREG = 0x80;
    while (1)
    {
        ;
    }
    return 0;
}