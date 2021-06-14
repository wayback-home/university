#include <inttypes.h>
#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>
#include <util/delay.h>

void interrupt_call(int);
int num = 0, count = 0;
char seg_data[10] = {0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F};

ISR(TIMER0_COMP_vect)
{
    count++;
    if (count == 250)
    {
        interrupt_call(num);
        num++;
        if (num == 10)
            num = 0;
        count = 0;
    }
}

int main()
{
    DDRA = 0xFF;  // 방향출력설정 PORTB
    DDRF = 0x10;  // 방향출력설정 PORTF
    TIMSK = 0x02; // OCIE0 = 2,0x02
    TCCR0 = 0x1E; // ctc mode, CS02 CS01 CS00 = 256분주 00001 110
    TCNT0 = 0;    // 초기값 0
    OCR0 = 250;
    SREG = 0x80; // 인터럽트 허용

    while (1)
    {
        ;
    }
    return 0;
}

void interrupt_call(int num)
{
    int i;
    for (i = 0; i < 2; i++)
    {
        PORTF = 0b11100000;
        PORTA = seg_data[num];
        _delay_ms(100);
        PORTF = 0b11110000;
        _delay_ms(100);
    }
}
