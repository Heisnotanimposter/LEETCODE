#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main() {
    while (1) {
        int data[7];
        int target = 0;
        for (int i = 0; i <=7; i++) {
            scanf("%d", &data[i]);
            if (data[i] > data[target]) {
                target = i;
            }
        }
        printf("%d\n", target);
    }
    return 0;
}
