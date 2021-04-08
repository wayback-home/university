#include <inttypes.h>
#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>

int main(void)
{
    unsigned char key;
    DDRA = 0xff;
    DDRB = 0xff;
    DDRC = 0x00;
    PORTA = 0x00;
    PORTB = 0xff;
    while (1)
    {
        key = PINC;
        PORTB = key;
        PORTA = ~key;
        _delay_ms(500);
    }
    return 0;
}
