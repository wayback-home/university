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
        PORTA = ~PORTA;
    }
    else if (PORTA == 0x55)
    {
        PORTA = ~PORTA;
    }
    else
    {
        PORTA = 0xAA;
    }
}
ISR(INT7_vect)
{
    for (i = 0; i < 5; i++)
    {
        PORTA = 0xFF;
        _delay_ms(30);
        PORTA = 0x00;
        _delay_ms(30);
    }
}

int main(void)
{
    DDRA = 0xFF;
    EIMSK = 0xF0;
    EICRB = 0x0F;
    SREG = 0b10000000;

    //1, 2번 (led 켜기, led 끄기:4, 5번 포트)
    while (1)
    {
        ;
    }
    return 0;
}