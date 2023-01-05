#include <stdio.h>

int main() {
    int i, j, temp, n, arr[10];

    printf("Enter the number of elements in your array: \n");
    scanf("%d", &n);

    printf("Enter the array elements: \n");
    for (i = 0; i < n; ++i) {
        scanf("%d", &arr[i]);
    }

    for (i = 0; i < n; ++i) {
        for (j = i + 1; j < n; ++j) {
            if (arr[i] > arr[j]) { //to check if current element greater than i+1th element, if yes; perform swap.
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }

    printf("\nThe array sorted in ascending order is as given below: \n");
    for (i = 0; i < n; ++i) {
        printf("%d\n", arr[i]);
    }

    return 0;
}