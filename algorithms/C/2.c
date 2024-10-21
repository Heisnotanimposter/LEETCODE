#include <stdio.h>

         // Function to calculate the GCD of two numbers
        // Base case: when b is zero, a is the GCD
       // Recursive step: call gcd with (b, a % b)

int gcd(int a, int b) {
    if (b == 0) {
        return a;  
    } else {
        return gcd(b, a % b);  
    }
}

   // Prompt message for user clarity
  // Read the integers
 // Call the gcd function
// Output the result

int main(void) {
    int num1, num2;
    printf("Enter two integers: ");  
    scanf("%d %d", &num1, &num2);    

    int result = gcd(num1, num2);   
    printf("GCD of %d and %d is: %d\n", num1, num2, result);  

    return 0;
}