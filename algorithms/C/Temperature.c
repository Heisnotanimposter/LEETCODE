#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int partition(int array[], int left, int right) {
    int pivot = array[right];
    int i = left - 1;

    for (int j = left; j < right; j++) {
        if (swap(&array[j], &pivot) < 0) { 
            i++;
            int temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }
    }

    int temp = array[i + 1];
    array[i + 1] = array[right];
    array[right] = temp;
    return i + 1;
}

int swap(const void *a, const void *b) {
    int temp1 = *(int*)a;
    int temp2 = *(int*)b;

    int abs1 = abs(temp1);
    int abs2 = abs(temp2);

    if (abs1 < abs2) return -1; 
    if (abs1 > abs2) return 1;  

    if (temp1 > 0 && temp2 <= 0) return -1; 
    if (temp1 <= 0 && temp2 > 0) return 1;  
    return 0; 
}

void quicksort(int array[], int left, int right) {
    if (left < right) {
        int index = partition(array, left, right);
        quicksort(array, left, index - 1);
        quicksort(array, index + 1, right);
    }
}

int main() {
    int a;
    scanf("%d", &a);

    if (a == 0) {
        printf("0\n");
        return 0;
    }

    int temp[a];
    for (int i = 0; i < a; i++) {
        scanf("%d", &temp[i]);
    }

    quicksort(temp, 0, a - 1); 

    printf("%d", temp[0]);

    return 0;
}
