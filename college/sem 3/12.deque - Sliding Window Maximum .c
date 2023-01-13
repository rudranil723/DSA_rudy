// Output: 3 3 4 5 5 5 6
// Explanation: Maximum of 1, 2, 3 is 3
//                        Maximum of 2, 3, 1 is 3
//                        Maximum of 3, 1, 4 is 4
//                        Maximum of 1, 4, 5 is 5
//                        Maximum of 4, 5, 2 is 5 
//                        Maximum of 5, 2, 3 is 5
//                        Maximum of 2, 3, 6 is 6

// Input: arr[] = {8, 5, 10, 7, 9, 4, 15, 12, 90, 13}, K = 4 
// Output: 10 10 10 15 15 90 90
// Explanation: Maximum of first 4 elements is 10, similarly for next 4 
//                        elements (i.e from index 1 to 4) is 10, So the sequence 
//                        generated is 10 10 10 15 15 90 90


// C program for the above approach
#include <stdio.h>

void printKMax(int arr[], int N, int K)
{
    int j, max;

    for (int i = 0; i <= N - K; i++) {
        max = arr[i];

        for (j = 1; j < K; j++) {
            if (arr[i + j] > max)
                max = arr[i + j];
        }
        printf("%d ", max);
    }
}

// Driver's Code
int main()
{
    int arr[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    int N = sizeof(arr) / sizeof(arr[0]);
    int K = 3;

    // Function call
    printKMax(arr, N, K);
    return 0;
}
