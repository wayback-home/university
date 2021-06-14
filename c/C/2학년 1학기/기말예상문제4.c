#include <inttypes.h>
#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>
#include <util/delay.h>

// 7seg제어를 위한 리스트(0~9)
char seg[10] = {0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7C, 0x27, 0x7F, 0x67};
int n1 = 0, n10 = 0, num = 0, i = 0;
char led = 0xFE; // 1111 1110

SIGNAL(SIG_OUTPUT_COMPARE0)
{
    num++;
    n1 = num % 10;
    n10 = num / 10;
    for (i = 0; i < 49; i++)
    {

        PORTA = seg[n1];
        _delay_ms(10);

        PORTF = seg[n10];
        if (num > 99)
            num = 0;
        _delay_ms(10);
    }
    led = led << 1;
    led = led | 0x01; // or 연산
    if (led == 255)
        led = 0xFE;
    PORTE = led;
}

int main(void)
{

    TIMSK = 0x02; // TOIE0 = 1
    TCCR0 = 0x6F; // Fast PWM모드  1024분주 15625hs 64uS
    TCNT0 = 0;    // 시작점
    OCR0 = 127;   // 오버플로우 시점 0.001초마다 compare match   0.001/8uS =125    -> TCNTn 값이 0~124까지 도달하면  0.001초
    SREG = 0x80;  // 인터럽트 허용

    DDRA = 0xFF;
    DDRF = 0xFF;
    DDRE = 0xFF;
    DDRB = 0xFF;

    while (1)
        ;
    return 0;
}
