#include <stdio.h>

// Function to find the location of x in list S
int findLocation(int S[], int n, int x) {
    for (int i = 0; i < n; i++) {
        if (S[i] == x) {
            return i + 1; // Return the subscript (1-based index)
        }
    }
    return 0; // Return 0 if x is not found
}

int main() {
    int n, x;
    printf("Enter the number of elements (n): ");
    scanf("%d", &n);
    
    int S[n];
    printf("Enter %d integers for the list S: ", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &S[i]);
    }
    
    printf("Enter the integer to find (x): ");
    scanf("%d", &x);
    
    int location = findLocation(S, n, x);
    if (location != 0) {
        printf("The integer %d is located at position: %d\n", x, location);
    } else {
        printf("The integer %d is not in the list.\n", x);
    }
    
    return 0;
}