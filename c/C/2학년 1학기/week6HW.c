#include <inttypes.h>
#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>

int main(void)
{
    unsigned char led[16] = {0xE1, 0xE2, 0xE4, 0xE8, 0xD1, 0xD2, 0xD4, 0xD8, 0xB1, 0xB2, 0xB4, 0xB8, 0x71, 0x72, 0x74, 0x78};
    DDRE = 0xFF;
    PORTE = 0xF0;
    DDRF = 0x0F;
    PORTF = 0x0F;

    int keyinput;

    while (1)
    {
        //40 50 60 70

        PORTF = 0x01;
        _delay_ms(5);
        keyinput = PINF;

        if (keyinput == 0x11)
        {
            PORTE = led[0];
            _delay_ms(5);
            keyinput = 0x00;
            PORTE = 0xF0;
        }

        else if (keyinput == 0x21)
        {
            PORTE = led[4];
            _delay_ms(5);
            keyinput = 0x00;
            PORTE = 0xF0;
        }

        else if (keyinput == 0x41)
        {
            PORTE = led[8];
            _delay_ms(5);
            keyinput = 0x00;
            PORTE = 0xF0;
        }

        else if (keyinput == 0x81)
        {
            PORTE = led[12];
            _delay_ms(5);
            keyinput = 0x00;
            PORTE = 0xF0;
        }

        //41 51 61 71
        PORTF = 0x02;
        _delay_ms(5);
        keyinput = PINF;

        if (keyinput == 0x12)
        {
            PORTE = led[1];
            _delay_ms(5);
            keyinput = 0x00;
            PORTE = 0xF0;
        }

        else if (keyinput == 0x22)
        {
            PORTE = led[5];
            _delay_ms(5);
            keyinput = 0x00;
            PORTE = 0xF0;
        }

        else if (keyinput == 0x42)
        {
            PORTE = led[9];
            _delay_ms(5);
            keyinput = 0x00;
            PORTE = 0xF0;
        }

        else if (keyinput == 0x82)
        {
            PORTE = led[13];
            _delay_ms(5);
            keyinput = 0x00;
            PORTE = 0xF0;
        }

        //42 52 62 72
        PORTF = 0x04;
        _delay_ms(5);
        keyinput = PINF;

        if (keyinput == 0x14)
        {
            PORTE = led[2];
            _delay_ms(5);
            keyinput = 0x00;
            PORTE = 0xF0;
        }

        else if (keyinput == 0x24)
        {
            PORTE = led[6];
            _delay_ms(5);
            keyinput = 0x00;
            PORTE = 0xF0;
        }

        else if (keyinput == 0x44)
        {
            PORTE = led[10];
            _delay_ms(5);
            keyinput = 0x00;
            PORTE = 0xF0;
        }

        else if (keyinput == 0x84)
        {
            PORTE = led[14];
            _delay_ms(5);
            keyinput = 0x00;
            PORTE = 0xF0;
        }

        //43 53 63 73
        PORTF = 0x08;
        _delay_ms(5);
        keyinput = PINF;

        if (keyinput == 0x18)
        {
            PORTE = led[3];
            _delay_ms(5);
            keyinput = 0x00;
            PORTE = 0xF0;
        }

        else if (keyinput == 0x28)
        {
            PORTE = led[7];
            _delay_ms(5);
            keyinput = 0x00;
            PORTE = 0xF0;
        }

        else if (keyinput == 0x48)
        {
            PORTE = led[11];
            _delay_ms(5);
            keyinput = 0x00;
            PORTE = 0xF0;
        }

        else if (keyinput == 0x88)
        {
            PORTE = led[15];
            _delay_ms(5);
            keyinput = 0x00;
            PORTE = 0xF0;
        }
    }

    return 0;
}
