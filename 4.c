#include <stdio.h>
#include <math.h>

double euclidean_distance(int x1, int y1, int x2, int y2)
  {
    double distance;  
    distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));  
    return distance;
  }

int main()
  {
    int x1, y1, x2, y2;
    printf("Enter coordinates for the first point (x1, y1): ");
    scanf("%d %d", &x1, &y1);

    printf("Enter coordinates for the second point (x2, y2): ");
    scanf("%d %d", &x2, &y2);

    double result = euclidean_distance(x1, y1, x2, y2);  
    printf("The Euclidean distance between the points is: %lf\n", result);

    return 0;
  }