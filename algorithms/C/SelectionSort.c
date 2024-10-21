#include <stdio.h>

// Function to find the index of the largest element in A[0] to A[last-1]
int theLargest(int A[], int last) {
    int largest = 0;
    for (int i = 1; i < last; i++) {
        if (A[i] > A[largest]) {
            largest = i;
        }
    }
    return largest;
}

// Function to perform Selection Sort on array A of size n
void selectionSort(int A[], int n) {
    for (int last = n; last > 1; last--) {
        int k = theLargest(A, last);
        // Swap A[k] and A[last-1]
        int temp = A[k];
        A[k] = A[last-1];
        A[last-1] = temp;
    }
}

// Main function to test the selectionSort
int main() {
    int A[] = {5, 2, 9, 1, 5, 6};
    int n = sizeof(A) / sizeof(A[0]);
    
    printf("Original array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", A[i]);
    }
    printf("\n");

    selectionSort(A, n);

    printf("Sorted array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", A[i]);
    }
    printf("\n");

    return 0;
}