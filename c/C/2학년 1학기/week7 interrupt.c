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

int main(void)
{
    DDRA = 0xFF;
    EIMSK = 0b00110000; //  ==  0x30
    EICRB = 0b00001111; //  ==  0x0F
    SREG = 0b10000000;  //  ==0x80

    while (1)
    {
        ;
    }
    return 0;
}