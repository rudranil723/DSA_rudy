#include <stdio.h>
int main()
{
    int array[100], position, i, n, value;
    printf("Enter number of elements in array\n");
    scanf("%d", &n);
    printf("Enter array elements:\n", n);
    for (i = 0; i < n; i++)
        scanf("%d", &array[i]);
    printf("Enter the location where you wish to insert an element\n");
    scanf("%d", &position);
    
    printf("Enter the value to insert\n");
    scanf("%d", &value);

    if (position > n + 1 || position < 1)
    {
        printf("The position entered is invalid\n");
    }
    else
    {
        for (i = n - 1; i >= position - 1; i--)
            array[i + 1] = array[i];
        array[position - 1] = value;  //inserting value at the required location
        printf("Resultant array is:\n");
        for (i = 0; i <= n; i++)
            printf("%d\n", array[i]);
    }
    return 0;
}