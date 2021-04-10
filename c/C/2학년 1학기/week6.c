#include <inttypes.h>
#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>

int main(void)
{
    unsigned char key[16] = {0xE1, 0xE2, 0xE4, 0xE8, 0xD1, 0xD2, 0xD4, 0xD8, 0xB1, 0xB2, 0xB4, 0xB8, 0x71, 0x72, 0x74, 0x78};
    DDRE = 0xFF;
    PORTE = 0xF0;
    while (1)
    {
        int i;
        for (i = 0; i < 16; i++)
        {
            PORTE = key[i];
            _delay_ms(500);
        }
    }
    return 0;
}
