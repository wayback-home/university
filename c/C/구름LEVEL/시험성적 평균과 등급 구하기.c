#include <stdio.h>

int main(void)
{
    float kor = 0;
    float eng = 0;
    float math = 0;

    scanf("%f %f %f", &kor, &eng, &math);

    float score = 0;
    score = (kor + eng + math) / 3;

    char grade;
    if (score >= 90)
    {
        grade = 'A';
    }
    else if (score >= 80)
    {
        grade = 'B';
    }
    else if (score >= 70)
    {
        grade = 'C';
    }
    else if (score >= 60)
    {
        grade = 'D';
    }
    else
    {
        grade = 'F';
    }

    printf("%5.2f %c", score, grade);
}