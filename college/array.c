#include <stdio.h>

int main()
{
    int a[100],i,n;
    printf("enter the range of the array: ");
    scanf("%d",&n);
    printf("Enter the elements of the array");
    for (i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    printf("the element of the array: ");
    for (i=0;i<n;i++){
        printf("%d ",a[i]);
    }

    return 0;
}
