#include <stdio.h>

int main() {
    int array[] =  {6, 14, 40, 65, 74, 82, 83, 100, 105, 112, 147, 148, 150, 160, 166, 174, 176, 178, 193, 204, 214, 217, 222, 246, 266, 277, 278, 293, 305, 307, 322, 340, 353, 365, 372, 386, 387, 389, 398, 407, 419, 444, 448, 459, 470, 492, 493, 497, 504, 526, 543, 555, 557, 566, 582, 590, 609, 612, 615, 626, 638, 645, 647, 670, 682, 685, 722, 743, 758, 766, 769, 779, 794, 802, 803, 804, 806, 808, 811, 822, 841, 860, 876, 885, 906, 913, 917, 918, 938, 945, 949, 954, 968, 982, 983, 1000, 1005, 1012, 1022};
    
    int size = sizeof(array) / sizeof(array[0]);  // [1]
    int minVal = array[0];                        // [2]
    int maxVal = array[0];                        // [3]

    for(int i = 0; i < size; i++) {               // [4]
        if(array[i] < minVal) {                   // [5]
            minVal = array[i];                    // [6]
        }
        if(array[i] > maxVal) {                   // [7]
            maxVal = array[i];                    // [8]
        }
    }
    
    printf("Size of array: %d\n", size);          // [9]
    printf("Lowest value: %d\n", minVal);         // [10]
    printf("Highest value: %d\n", maxVal);        // [11]
    return 0;
}

/*  1.  int size = sizeof(array) / sizeof(array[0]);:
    •   This calculates the number of elements in the array by dividing the total size of the array by the size of a single element. The time complexity of this operation is O(1) because it’s a simple arithmetic calculation.
    2.  int minVal = array[0];:
    •   This initializes minVal to the first element of the array. This is a constant-time operation (O(1)).
    3.  int maxVal = array[0];:
    •   This initializes maxVal to the first element of the array. This is also O(1).
    4.  for (int i = 0; i < size; i++) {:
    •   This is the main loop of the program that iterates through the entire array. It runs size times, where size is the number of elements in the array. This makes the loop O(N), where N is the size of the array.
    5.  if (array[i] < minVal) {:
    •   Inside the loop, this if statement checks if the current element (array[i]) is less than the current minimum value (minVal). This is a constant-time operation (O(1)).
    6.  minVal = array[i];:
    •   If the condition is true, it updates minVal to the current element. This assignment operation is O(1).
    7.  if (array[i] > maxVal) {:
    •   Similarly, this statement checks if the current element (array[i]) is greater than the current maximum value (maxVal). This comparison is O(1).
    8.  maxVal = array[i];:
    •   If the condition is true, it updates maxVal to the current element. This assignment operation is also O(1).
    9.  printf("Size of array: %d\n", size);:
    •   This prints the size of the array. The time complexity of this operation is O(1).
    10. printf("Lowest value: %d\n", minVal);:
    •   This prints the minimum value found in the array. This operation is O(1).
    11. printf("Highest value: %d\n", maxVal);:
    •   This prints the maximum value found in the array. This operation is O(1).

Overall Time Complexity

The overall time complexity of the code is determined by the loop (lines [4] to [8]):

    •   The loop runs N times (where N is the number of elements in the array).
    •   Inside the loop, each operation (if statements and assignments) takes O(1) time.

Therefore, the total time complexity is O(N).
*/



