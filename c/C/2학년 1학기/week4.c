#include <inttypes.h>
#include <avr/io.h>
#include <util/delay.h>

int main()
{
    unsigned char led;
    DDRD = 0xFF;
    DDRE = 0xFF;
    DDRF = 0xFF;
    while (1)
    {
        PORTE = 0x00;
        PORTF = 0x00;
        for (led = 0; led < 8; led++)
        {
            PORTD = 0x01 << led;
            _delay_ms(500);
        };
        PORTD = 0x00;
        PORTF = 0x00;
        for (led = 0; led < 8; led++)
        {
            PORTE = 0x01 << led;
            _delay_ms(500);
        };
        PORTD = 0x00;
        PORTE = 0x00;
        for (led = 0; led < 8; led++)
        {
            PORTF = 0x01 << led;
            _delay_ms(500);
        };
        PORTD = 0x00;
        PORTE = 0x00;
        for (led = 0; led < 8; led++)
        {
            PORTF = 0x80 >> led;
            _delay_ms(500);
        };
        PORTD = 0x00;
        PORTF = 0x00;
        for (led = 0; led < 8; led++)
        {
            PORTE = 0x80 >> led;
            _delay_ms(500);
        };
        PORTE = 0x00;
        PORTF = 0x00;
        for (led = 0; led < 8; led++)
        {
            PORTD = 0x80 >> led;
            _delay_ms(500);
        };
    }
    return 0;
}