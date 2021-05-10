#include <inttypes.h>
#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>
#include <util/delay.h>

unsigned int i = 0;

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

    if (PORTA == 0xAA)
    {
        PORTA = 0x00;
    }
    else
    {
        PORTA = 0xAA;
    }
}
ISR(INT7_vect)
{
    for (i = 0; i < 3; i++)
    {
        PORTA = 0xFF;
        _delay_ms(50);
        PORTA = 0x00;
        _delay_ms(50);
    }
}

int main(void)
{
    DDRA = 0xFF;
    EIMSK = 0xF0;
    EICRB = 0xFA;
    SREG = 0x80;

    while (1)
    {
        ;
    }
    return 0;
}