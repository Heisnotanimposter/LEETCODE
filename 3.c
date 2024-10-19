#include <stdio.h>

int scd(int number)
  {
    if(number < 2)
      {
        return -1;
      }
    for (int i = 2 ; i <= number; i++)
      {
        if (number % i ==0)
          {
            return i;
          }
      }

    return number;
  }

int main()
  {
    int num;
    printf("Input:");
    scanf("%d", &num);

    int result = scd(num);

    if (result == -1)
      {
        printf("-");
      }
    else
      {
        printf("-");
      }
    return 0;
  }