#include <inttypes.h>
#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>
#include <util/delay.h>

volatile unsigned char SW = 0;

ISR(INT4_vect)
{
    SW = !SW;
    _delay_ms(100);
    EIFR = 0x10;
}

int main(void)
{
    DDRA = 0xFF;
    EIMSK = 0x30; //  ==  0x30
    EICRB = 0x0F; //  ==  0x0F
    SREG = 0x80;  //  ==0x80

    while (1)
    {
        if (SW)
        {
            PORTA = 0xFF;
        }
        else
        {
            PORTA = 0x00;
        }
    }
    return 0;
}