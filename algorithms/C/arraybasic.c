#include <stdio.h>

int main() {
    int array[] =  {6, 14, 40, 65, 74, 82, 83, 100, 105, 112, 147, 148, 150, 160, 166, 174, 176, 178, 193, 204, 214, 217, 222, 246, 266, 277, 278, 293, 305, 307, 322, 340, 353, 365, 372, 386, 387, 389, 398, 407, 419, 444, 448, 459, 470, 492, 493, 497, 504, 526, 543, 555, 557, 566, 582, 590, 609, 612, 615, 626, 638, 645, 647, 670, 682, 685, 722, 743, 758, 766, 769, 779, 794, 802, 803, 804, 806, 808, 811, 822, 841, 860, 876, 885, 906, 913, 917, 918, 938, 945, 949, 954, 968, 982, 983, 1000, 1005, 1012, 1022};
    
    int size = sizeof(array) / sizeof(array[0]);
    int minVal = array[0];
    int maxVal = array[0];

    for(int i = 0; i < size; i++) {
        if(array[i] < minVal) {
            minVal = array[i];
        }
        if(array[i] > maxVal) {
            maxVal = array[i];
        }
    }
    
    printf("Size of array: %d\n", size);
    
    printf("Lowest value: %d\n", minVal);
    
    printf("Highest value: %d\n", maxVal);
    return 0;
}
