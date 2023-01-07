#include <stdio.h>

int main()
{
    int arr[] = { 1,6,3,7,2 };
    int k = 2; //position
    int n = 5; //size of array
    int i, j;
    j = k;
    while (j < n) {
        arr[j] = arr[j + 1];
        j = j + 1;
    }
    n = n - 1;

    printf("new array ");
    for (i = 0;i < n;i++) {
        printf("%d", arr[i]);
    }

    return 0;
}
