#include <inttypes.h>
#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>
#include <util/delay.h>

ISR(INT4_vect) { PORTF = 0x0A; } //직진
ISR(INT5_vect) { PORTF = 0x02; } //우회전
ISR(INT6_vect) { PORTF = 0x08; } //좌회전
ISR(INT7_vect) { PORTF = 0x00; } //정지

int main(void)
{
    DDRF = 0xFF;
    EIMSK = 0xF0;
    EICRB = 0xF0;
    SREG = 0xF0;

    while (1)
    {
        ;
    }
}