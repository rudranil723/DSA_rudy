#include <stdio.h>

int main() {
    int array[10], n, i, temp, end;

    printf("Enter length of array:\n");
    scanf("%d", &n);
    end = n - 1;

    printf("Enter array elements: \n");
    for (i = 0; i < n; i++) {
        scanf("%d", &array[i]);
    }

    for (i = 0; i < n / 2; i++) {
        temp = array[i];
        array[i] = array[end];
        array[end] = temp;
        end--;
    }

    printf("\nReversed array elements are:\n");
    for (i = 0; i < n; i++) {
        printf("%d\n", array[i]);
    }

    return 0;
}