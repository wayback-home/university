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
/* Timer/Counter0 Compare Match  
#define TIMER0_COMP_vect		_VECTOR(15)
#define SIG_OUTPUT_COMPARE0		_VECTOR(15)
*/

unsigned int time = 0;

SIGNAL(SIG_OUTPUT_COMPARE0)
{
    if (time == 1000)
    {
        PORTE = (~PORTE);
        time = 0;
    }
    else
    {
        time++;
    }
}

int main(void)
{
    TCCR0 = 0x1d; // 0000 1 101   분주비 128  1/18MHz  *128  = 8uS  TCNTn 1증가
    TIMSK = 0x02;
    OCR0 = 124; // 0.001초마다 compare match   0.001/8uS =125    -> TCNTn 값이 0~124까지 도달하면  0.001초
    SREG = 0x80;
    DDRE = 0xff;
    DDRB = 0xff;

    while (1)
        ;
    return 0;
}
