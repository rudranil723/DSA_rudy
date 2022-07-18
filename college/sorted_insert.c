//Write a program in C to insert an element in a sorted array so that after insertion array should be sorted.

#include <stdio.h>

int main(){
    int a[50],n,i,item;
    printf("enter the range: ");
    scanf("%d",&n);
    printf("enter a sorted array: ");
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    printf("enter the element to be entered: ");
    scanf("%d",&item);
    for(i=0;i<n;i++){
        if (item>a[i]){
            a[i+1]=item;
            a[i+1]=a[i+2];
        }
    }
    printf("new array: ");
    for(i=0;i<n;i++)
    {
        printf("%d ",a[i]);
    }
    return 0;
}
