#include <inttypes.h>
#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>
#include <util/delay.h>
#include <avr/lcd4.h>
#include <stdio.h>

void EEPROM_write(unsigned int addr, unsigned char data);
unsigned char EEPROM_read(unsigned int addr);
char check_EEPROM();
void set_EEPROM();

int main(void)
{
    unsigned int addr_EEPROM = 0x0002;
    unsigned char data_EEPROM, interruptNo = 0;
    char msg[20];
    DDRB = 0xff;
    DDRE = 0x00;
    PORTE = 0xFF;

    EIMSK = 0xF0;
    EICRB = 0xD2;

    init_lcd4();
    if (check_EEPROM())
    {
        data_EEPROM = EEPROM_read(addr_EEPROM);
    }
    else
    {
        set_EEPROM();
        data_EEPROM = 0;
    }

    sprintf(msg, "Current now : %d ", data_EEPROM);
    writeString_lcd4(0, 0, msg);
    delay(1);
    writeString_lcd4(0, 1, "Program restart");

    while (1)
    {
        interruptNo = EIFR;

        if (interruptNo)
        {
            switch (interruptNo)
            {
            case 0x10:
                interruptNo = 4;
                EIFR |= 0x10;
                data_EEPROM++;
                EEPROM_write(0x0002, data_EEPROM);
                sprintf(msg, "Current now : %d ", data_EEPROM);
                writeString_lcd4(0, 0, msg);
                break;

            case 0x20:
                interruptNo = 5;
                EIFR |= 0x20;
                break;

            case 0x40:
                interruptNo = 6;
                EIFR |= 0x40;
                break;

            case 0x80:
                interruptNo = 7;
                EIFR |= 0x80;
                break;
            }

            sprintf(msg, "   %d checked ", interruptNo);
            interruptNo = 0;
            writeString_lcd4(0, 1, msg);
        }
    }
    return 0;
}

char check_EEPROM()
{
    char code0 = '1', code1 = '2', data0, data1;
    data0 = EEPROM_read(0x0000);
    delay(1);
    data1 = EEPROM_read(0x0001);
    if (data0 == '1' && data1 == '2')
        return 1;
    else
        return 0;
}

void set_EEPROM()
{
    EEPROM_write(0x0000, '1');
    delay(1);
    EEPROM_write(0x0001, '2');
    delay(1);
    EEPROM_write(0x0002, 0x00);
}

void EEPROM_write(unsigned int addr, unsigned char data)
{
    while (EECR & (1 << EEWE))
        ;
    EEAR = addr;
    EEDR = data;
    EECR |= (1 << EEMWE);
    EECR |= (1 << EEWE);
}

unsigned char EEPROM_read(unsigned int addr)
{
    while (EECR & (1 << EEWE))
        ;
    EEAR = addr;
    EECR |= (1 << EERE);
    return EEDR;
}