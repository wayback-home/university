#include <stdio.h>

int calculate(int *width, int *height)
{
    int get_area = *width * *height;
    int get_circum = 2 * (*width + *height);

    printf("넓이: %d", get_area);
    printf(", 둘레: %d", get_circum);
}

int main(void)
{
    int get_width = 0;
    int get_height = 0;

    printf("가로? ");
    scanf("%d", &get_width);
    printf("세로? ");
    scanf("%d", &get_height);

    calculate(&get_width, &get_height);
}