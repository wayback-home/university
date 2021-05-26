#include <inttypes.h>
#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>
#include <util/delay.h>
#include <stdio.h>

unsigned char led = 0xFE, ledB = 0x01;

// ISR(TIMER0_OVF_vect)
// {
//     led = led << 1;
//     led = led | 0x01;
//     if (led == 0xFF)
//         led = 0xFE;
//     PORTC = led;
// }

ISR(TIMER0_COMP_vect)
{
    // OCR0 = OCR0 - 1;
    // if (OCR0 < 0x1F)
    //     OCR0 = 0xFF;
    led = led << 1;
    led = led | 0x01;
    if (led == 0xFF)
        led = 0xFE;
    PORTC = led;
}

int main()
{
    DDRC = 0xFF;
    DDRE = 0xFF;
    PORTC = led;
    TIMSK = 0x02;
    TCCR0 = 0x1F;
    OCR0 = 240;  // 출력 비교 레지스터값
    TCNT0 = 0;   // T/C 0 레지스터 초기값
    SREG = 0x80; // 인터럽트 허용
    while (1)
    {
        PORTE = 0xFF;
        _delay_ms(100);
        PORTE = 0x00;
        _delay_ms(100);
    }
    return 0;
}