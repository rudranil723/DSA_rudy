#include <stdio.h>

int main() {
    int arr[] = { 1,5,6,8,7,2 };
    int i, item, k;
    int n = sizeof(arr) / sizeof(arr[0]);
    scanf("enter new item and position %d", &item);
    scanf("%d", &k);
    arr[k - 1] = item;
    for (i = 0;i < n;i++) {
        printf("%d", arr[i]);
    }

    return 0;
}