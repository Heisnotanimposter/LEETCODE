#include <stdio.h>

void print_array(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int my_array[] = {64, 34, 25, 5, 22, 11, 90, 1264, 34, 25, 5, 22, 11, 90, 1264, 34, 25, 5, 22, 11, 90, 1264, 34, 25, 5, 22, 11, 90, 1264, 34, 25, 5, 22, 11, 90, 1264, 34, 25, 5, 22, 11, 90, 1264, 34, 25, 5, 22, 11, 90, 1264, 34, 25, 5, 22, 11, 90, 1264, 34, 25, 5, 22, 11, 90, 12};
    int n = sizeof(my_array) / sizeof(my_array[0]);

    printf("Initial array: ");
    print_array(my_array, n);

    for (int i = 0; i < n-1; i++) {
        int min_index = i;
        for (int j = i+1; j < n; j++) {
            if (my_array[j] < my_array[min_index]) {
                min_index = j;
            }
        }
        int min_value = my_array[min_index];
        for (int k = min_index; k > i; k--) {
            my_array[k] = my_array[k-1];
        }
        my_array[i] = min_value;

        printf("Array after iteration %d: ", i+1);
        print_array(my_array, n);
    }

    printf("Sorted array: ");
    print_array(my_array, n);

    // Big O notation analysis
    printf("Time complexity analysis:\n");
    printf("Outer loop: O(n)\n");
    printf("Inner loop: O(n)\n");
    printf("Nested loop for shifting elements: O(n)\n");
    printf("Overall time complexity: O(n^2)\n");

    return 0;
}
