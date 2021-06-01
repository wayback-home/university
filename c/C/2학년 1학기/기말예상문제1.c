#include <inttypes.h>
#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>
#include <util/delay.h>
/* Timer/Counter0 Overflow */
/*
#define TIMER0_OVF_vect			_VECTOR(16)
#define SIG_OVERFLOW0			_VECTOR(16)
*/

unsigned char seg_data[10] = {0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7f, 0x6f};
unsigned char led = 0xfe;
unsigned char cnt = 0, segment = 0, flag = 1;

ISR(TIMER0_OVF_vect)
{
    cnt++;
    if (cnt == 60)
    {
        if (flag) // 인터럽트 60회 발생시 led 한번 시프트
        {
            cnt = 0;
            segment++;
            PORTB = seg_data[segment]; // segment 출력
                                       // segment++;
            if (segment == 9)
            {
                segment = 9;
                flag = 0;
            }
            PORTE = 0b01100000;
        }
        else // 인터럽트 60회 발생시 led 한번 시프트
        {
            cnt = 0;
            segment--;
            PORTB = seg_data[segment]; // segment 출력

            if (segment == 0)
            {
                segment = 0;
                flag = 1;
            }
            PORTE = 0b01010000;
        }
    }
}

int main()
{
    DDRB = 0xff;
    DDRC = 0xff;
    DDRF = 0xff;
    PORTF = 0b11100000;
    TIMSK = 1;
    TCCR0 = 0b00000111; // 1024분주
    TCNT0 = 0;
    SREG = 0x80;
    PORTC = led;
    // PORTB = seg_data[5];	    // 초기값  5      // 5.1.2.3.4.5.6.7.0.1.2.3...........
    while (1)
        ;

    return 0;
}
